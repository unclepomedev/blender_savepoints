import sys
import unittest
from pathlib import Path

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.asset_path import remap_snapshot_paths
from savepoints_test_case import SavePointsTestCase


class TestRemapSnapshotPaths(SavePointsTestCase):
    def test_remap_snapshot_paths(self):
        print("Starting Remap Snapshot Paths Test...")
        # test_dir is provided by SavePointsTestCase
        project_dir = self.test_dir

        # Paths setup
        history_dir = project_dir / ".project_history"
        version_dir = history_dir / "v001"
        version_dir.mkdir(parents=True)

        # Create a dummy library file to link against
        lib_dir = project_dir / "Lib"
        lib_dir.mkdir()
        lib_path = lib_dir / "library.blend"

        # Create dummy image file location (file doesn't need to exist for logic test, but path does)
        tex_dir = project_dir / "Textures"
        tex_dir.mkdir()
        img_path = tex_dir / "image.png"

        # Create dummy object to link and save lib
        bpy.ops.wm.read_factory_settings(use_empty=True)
        ob = bpy.data.objects.new("DummyObj", None)
        ob.use_fake_user = True
        bpy.ops.wm.save_as_mainfile(filepath=str(lib_path))

        # --- Setup Data Blocks ---
        # Start with a clean slate
        bpy.ops.wm.read_factory_settings(use_empty=True)

        # 1. Image
        img = bpy.data.images.new("TestImage", 128, 128)

        # 2. Library
        with bpy.data.libraries.load(str(lib_path), link=True) as (data_from, data_to):
            if "DummyObj" in data_from.objects:
                data_to.objects = ["DummyObj"]

        if not bpy.data.libraries:
            self.fail(f"Failed to load library. Libs: {list(bpy.data.libraries)}")

        lib = bpy.data.libraries[0]

        # 3. VSE
        scene = bpy.context.scene
        if not scene.sequence_editor:
            scene.sequence_editor_create()

        # Add an image strip
        with open(img_path, 'wb') as f:
            f.write(b'fake png')

        print(f"DEBUG: SequenceEditor attributes: {dir(scene.sequence_editor)}")
        # Check if sequences exists or if we need to use something else
        if hasattr(scene.sequence_editor, "sequences"):
            seq = scene.sequence_editor.sequences.new_image("TestSeq", str(img_path), channel=1, frame_start=1)
        elif hasattr(scene.sequence_editor, "strips"):
            seq = scene.sequence_editor.strips.new_image("TestSeq", str(img_path), channel=1, frame_start=1)
        else:
            print("WARNING: 'sequences' and 'strips' not found in SequenceEditor.")
            seq = None

        print("\n--- Test 1: Valid Snapshot Remapping ---")
        # 1. Move file to snapshot location
        snapshot_path = version_dir / "snapshot.blend_snapshot"
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

        # 2. Set broken relative paths (simulate they are relative to project root)
        img.filepath = "//Textures/image.png"
        lib.filepath = "//Lib/library.blend"

        # Check what property seq has
        seq_has_filepath = hasattr(seq, "filepath")
        seq_has_directory = hasattr(seq, "directory")

        if seq_has_filepath:
            seq.filepath = "//Textures/image.png"
        elif seq_has_directory:
            seq.directory = "//Textures/"

        # Verify setup
        print(f"Current Filepath: {bpy.data.filepath}")

        # RUN REMAP
        remap_snapshot_paths(None)

        # ASSERT
        expected_prefix = "//../../"

        img_path_normalized = img.filepath.replace("\\", "/")
        self.assertTrue(img_path_normalized.startswith(expected_prefix),
                        f"Image path not remapped! Got: {img.filepath}")

        lib_path_normalized = lib.filepath.replace("\\", "/")
        self.assertTrue(lib_path_normalized.startswith(expected_prefix),
                        f"Library path not remapped! Got: {lib.filepath}")

        if seq:
            if seq_has_filepath:
                seq_path_normalized = seq.filepath.replace("\\", "/")
                self.assertTrue(seq_path_normalized.startswith(expected_prefix),
                                f"Sequence filepath not remapped! Got: {seq.filepath}")
            elif seq_has_directory:
                seq_dir_normalized = seq.directory.replace("\\", "/")
                self.assertTrue(seq_dir_normalized.startswith(expected_prefix),
                                f"Sequence directory not remapped! Got: {seq.directory}")

        print("Test 1 Passed: All paths remapped correctly.")

        print("\n--- Test 2: Double Remapping Prevention ---")
        # Paths are now //../../...
        # Run remap again
        remap_snapshot_paths(None)

        img_path_normalized = img.filepath.replace("\\", "/")
        self.assertFalse(img_path_normalized.startswith("//../../../../"),
                         f"Double remapping detected! Got: {img.filepath}")

        print("Test 2 Passed: Paths remained stable.")

        print("\n--- Test 3: Not a Snapshot (Normal .blend) ---")
        # Move to normal project location
        project_blend = project_dir / "project.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(project_blend), check_existing=False)

        # Reset paths
        img.filepath = "//Textures/image.png"

        remap_snapshot_paths(None)

        self.assertEqual(img.filepath, "//Textures/image.png",
                         f"Remapped unexpectedly in normal file! Got: {img.filepath}")

        print("Test 3 Passed: Normal file ignored.")

        print("\n--- Test 4: Snapshot outside History folder ---")
        # Move to snapshot outside history
        outside_snapshot = project_dir / "copy.blend_snapshot"
        bpy.ops.wm.save_as_mainfile(filepath=str(outside_snapshot), check_existing=False)

        # Reset paths
        img.filepath = "//Textures/image.png"

        remap_snapshot_paths(None)

        self.assertEqual(img.filepath, "//Textures/image.png",
                         f"Remapped unexpectedly outside history! Got: {img.filepath}")

        print("Test 4 Passed: Snapshot outside history ignored.")

        print("\n--- Test 5: Absolute Paths ---")
        # Move back to valid snapshot location to test exclusion logic
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), check_existing=False)

        # Set absolute path
        abs_path = str(img_path)
        img.filepath = abs_path

        remap_snapshot_paths(None)

        # On Windows/some setups, abs_path format might vary slightly, but checking if it was NOT remapped to relative is key.
        self.assertFalse(img.filepath.startswith("//"), f"Absolute path was remapped to relative! Got: {img.filepath}")

        print("Test 5 Passed: Absolute path ignored.")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
