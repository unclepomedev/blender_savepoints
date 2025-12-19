import sys
import unittest
from pathlib import Path

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.asset_path import remap_snapshot_paths
from savepoints_test_case import SavePointsTestCase


class TestRemapSnapshotPaths(SavePointsTestCase):

    def _setup_dummy_assets(self, project_dir):
        """Helper to create dummy Image, Library, and VSE strip for testing."""
        # 1. Setup Directories
        lib_dir = project_dir / "Lib"
        lib_dir.mkdir(parents=True, exist_ok=True)
        tex_dir = project_dir / "Textures"
        tex_dir.mkdir(parents=True, exist_ok=True)

        lib_path = lib_dir / "library.blend"
        img_path = tex_dir / "image.png"

        # 2. Create Dummy Library File
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.data.objects.new("DummyObj", None).use_fake_user = True
        bpy.ops.wm.save_as_mainfile(filepath=str(lib_path), check_existing=False)

        # 3. Reset to clean slate for the actual test file
        bpy.ops.wm.read_factory_settings(use_empty=True)

        # 4. Create Image Datablock
        img = bpy.data.images.new("TestImage", 128, 128)

        # 5. Link Library
        with bpy.data.libraries.load(str(lib_path), link=True) as (data_from, data_to):
            if "DummyObj" in data_from.objects:
                data_to.objects = ["DummyObj"]

        lib = bpy.data.libraries[0] if bpy.data.libraries else None

        # 6. Setup VSE
        scene = bpy.context.scene
        if not scene.sequence_editor:
            scene.sequence_editor_create()

        # Create real dummy image file
        # img datablock is already created above
        img.filepath_raw = str(img_path)
        img.file_format = 'PNG'
        img.save()

        # Add Strip
        # API compatibility check
        sequences = getattr(scene.sequence_editor, "sequences",
                            getattr(scene.sequence_editor, "strips", None))

        seq = None
        if sequences is not None:
            seq = sequences.new_image("TestSeq", str(img_path), channel=1, frame_start=1)

        return img, lib, seq, img_path

    def test_remap_scenario(self):
        """
        Scenario:
        1. Valid Snapshot: Verify paths are remapped (deepened) when saved as a snapshot.
        2. Idempotency: Verify remapping doesn't compound if run twice.
        3. Normal Blend: Verify normal .blend files are ignored.
        4. Outside History: Verify snapshots outside the history folder are ignored.
        5. Absolute Paths: Verify absolute paths are not converted to relative.
        """
        print("Starting Remap Snapshot Paths Scenario...")

        project_dir = self.test_dir
        history_dir = project_dir / ".project_history"
        version_dir = history_dir / "v001"
        version_dir.mkdir(parents=True, exist_ok=True)

        # Setup Assets
        img, lib, seq, real_img_path = self._setup_dummy_assets(project_dir)

        # Verify setup success
        self.assertIsNotNone(lib, "Library setup failed")
        self.assertIsNotNone(seq, "VSE setup failed")

        # --- Step 1: Valid Snapshot Remapping ---
        with self.subTest(step="1. Valid Snapshot"):
            # Move file to snapshot location (deep inside history)
            snapshot_path = version_dir / "snapshot.blend_snapshot"
            bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

            # Set paths to "Project Root Relative" (//Lib/...)
            # This simulates a file that was just copied from root to deep history
            img.filepath = "//Textures/image.png"
            lib.filepath = "//Lib/library.blend"

            # VSE handling
            if hasattr(seq, "filepath"):
                seq.filepath = "//Textures/image.png"
            elif hasattr(seq, "directory"):
                seq.directory = "//Textures/"

            # Run Remap
            remap_snapshot_paths(None)

            # Assert: Should now be relative from deep history (//../../)
            expected_prefix = "//../../"

            self.assertTrue(img.filepath.replace("\\", "/").startswith(expected_prefix),
                            f"Image path failed: {img.filepath}")
            self.assertTrue(lib.filepath.replace("\\", "/").startswith(expected_prefix),
                            f"Library path failed: {lib.filepath}")

            if hasattr(seq, "filepath"):
                self.assertTrue(seq.filepath.replace("\\", "/").startswith(expected_prefix),
                                f"Sequence path failed: {seq.filepath}")

        # --- Step 2: Idempotency ---
        with self.subTest(step="2. Idempotency"):
            # Run again on already remapped paths
            remap_snapshot_paths(None)

            # Assert: Should NOT become //../../../../
            path_norm = img.filepath.replace("\\", "/")
            self.assertFalse(path_norm.startswith("//../../../../"),
                             f"Double remapping detected: {img.filepath}")
            self.assertTrue(path_norm.startswith("//../../"),
                            "Path should remain correctly remapped")

        # --- Step 3: Normal .blend File ---
        with self.subTest(step="3. Normal .blend"):
            # Save as normal project file
            project_blend = project_dir / "project.blend"
            bpy.ops.wm.save_as_mainfile(filepath=str(project_blend), check_existing=False)

            # Reset path
            img.filepath = "//Textures/image.png"

            # Run Remap
            remap_snapshot_paths(None)

            # Assert: Should NOT change
            self.assertEqual(img.filepath, "//Textures/image.png", "Normal .blend file should be ignored")

        # --- Step 4: Snapshot Outside History ---
        with self.subTest(step="4. Snapshot Outside History"):
            # Save as snapshot but in root (not in history folder like .project_history)
            outside_snapshot = project_dir / "copy.blend_snapshot"
            bpy.ops.wm.save_as_mainfile(filepath=str(outside_snapshot), check_existing=False)

            # Reset path
            img.filepath = "//Textures/image.png"

            # Run Remap
            remap_snapshot_paths(None)

            # Assert: Should NOT change
            self.assertEqual(img.filepath, "//Textures/image.png", "Snapshot outside history should be ignored")

        # --- Step 5: Absolute Paths ---
        with self.subTest(step="5. Absolute Paths"):
            # Move back to valid snapshot location
            bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

            # Set Absolute Path
            abs_path = str(real_img_path)
            img.filepath = abs_path

            # Run Remap
            remap_snapshot_paths(None)

            # Assert: Should stay absolute (not start with //)
            self.assertFalse(img.filepath.startswith("//"),
                             f"Absolute path was incorrectly remapped: {img.filepath}")

        print("Remap Snapshot Paths Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
