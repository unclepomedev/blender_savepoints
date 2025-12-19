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

from savepoints.services.asset_path import unmap_snapshot_paths
from savepoints_test_case import SavePointsTestCase


class TestRelativePaths(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        # SavePointsTestCase creates self.test_dir and self.blend_path

        # --- Common Setup: Create Texture & Material ---
        self.texture_name = "my_texture.png"
        self.texture_path = self.test_dir / self.texture_name

        # Create a tiny minimal PNG
        with open(self.texture_path, 'wb') as f:
            f.write(
                b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')

        # Setup Scene
        bpy.ops.mesh.primitive_cube_add()
        self.obj = bpy.context.object
        self.obj.name = "TexturedCube"

        # Material & Texture Setup
        mat = bpy.data.materials.new(name="TexturedMat")
        mat.use_nodes = True
        self.obj.data.materials.append(mat)

        # Node Setup
        tex_node = mat.node_tree.nodes.new('ShaderNodeTexImage')

        try:
            img = bpy.data.images.load(str(self.texture_path))
            img.name = "TestImage"
            # Force relative path (//my_texture.png)
            img.filepath = f"//{self.texture_name}"
            tex_node.image = img
        except Exception as e:
            self.fail(f"Failed to load image during setup: {e}")

        # Save to persist the relative path setting in the .blend file
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

    def test_fork_retains_relative_paths_scenario(self):
        """
        Scenario:
        1. Commit a version: The snapshot file is created in a subdirectory.
           (Blender automatically remaps relative paths to ../../ when saving to subdir).
        2. Open Snapshot: Verify paths are indeed remapped (//../../).
        3. Fork Version: Create a new project file back in the root directory.
        4. Verify Fork: Ensure the paths are "unmapped" back to simple relative paths (//).
        """
        print("Starting Fork Relative Paths Scenario...")

        # --- Step 1: Commit ---
        with self.subTest(step="1. Commit Version"):
            bpy.ops.savepoints.commit(note="v1")

            history_dir = self.test_dir / ".test_project_history"
            snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"
            self.assertTrue(snapshot_path.exists(), "Snapshot not created")

        # --- Step 2: Open Snapshot & Verify Remapping ---
        with self.subTest(step="2. Verify Snapshot Path Remapping"):
            bpy.ops.wm.open_mainfile(filepath=str(snapshot_path))

            img = bpy.data.images.get("TestImage")
            self.assertIsNotNone(img, "Image missing in snapshot")

            # Snapshot is deep in history folder, so path should look up 2 levels
            path_norm = img.filepath.replace("\\", "/")
            self.assertTrue(path_norm.startswith("//../../"),
                            f"Snapshot path expected to start with //../../, got: {path_norm}")

        # --- Step 3: Fork Version ---
        with self.subTest(step="3. Execute Fork"):
            bpy.ops.savepoints.fork_version()

        # --- Step 4: Verify Forked File Paths ---
        with self.subTest(step="4. Verify Fork Path Restoration"):
            current_path = Path(bpy.data.filepath)

            # File Check
            self.assertEqual(current_path.name, "test_project_v001.blend")
            self.assertEqual(current_path.parent.resolve(), self.test_dir.resolve())

            # Path Check
            img_forked = bpy.data.images.get("TestImage")
            path_forked_norm = img_forked.filepath.replace("\\", "/")
            print(f"Forked Image Path: {path_forked_norm}")

            # Ideally it returns to "//my_texture.png"
            if path_forked_norm.startswith("//"):
                self.assertFalse(path_forked_norm.startswith("//../../"),
                                 "Forked path failed to unmap, still contains ../../")
                self.assertTrue(path_forked_norm.endswith(self.texture_name),
                                "Forked path doesn't point to correct texture name")

        print("Fork Relative Paths Scenario: Completed")

    def test_rescue_unmaps_paths_scenario(self):
        """
        Scenario:
        1. Prepare a snapshot containing an object with a remapped path (//../../).
        2. Simulate a 'Rescue' operation by appending that object into a fresh file.
        3. Verify the appended object has the broken (deep) path.
        4. Run `unmap_snapshot_paths` (the logic used by Rescue operator).
        5. Verify the path is fixed to be relative to the new project root.
        """
        print("Starting Rescue Unmap Logic Scenario...")

        history_dir = self.test_dir / ".test_project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"

        # --- Step 1: Create Snapshot ---
        with self.subTest(step="1. Create Snapshot"):
            # Ensure we are in the original file setup in setUp()
            bpy.ops.wm.open_mainfile(filepath=str(self.blend_path))
            bpy.ops.savepoints.commit(note="v1")

        # --- Step 2: Setup Clean Rescue Target ---
        with self.subTest(step="2. Setup Rescue Target"):
            new_project_path = self.test_dir / "rescue_target.blend"
            bpy.ops.wm.save_as_mainfile(filepath=str(new_project_path))

            # Clean scene
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()

        # --- Step 3: Append from Snapshot ---
        with self.subTest(step="3. Append Data"):
            # Manually append to simulate what the rescue operator does
            with bpy.data.libraries.load(str(snapshot_path), link=False) as (data_from, data_to):
                if "TexturedCube" in data_from.objects:
                    data_to.objects.append("TexturedCube")

            # Link to scene
            if data_to.objects:
                obj = data_to.objects[0]
                bpy.context.collection.objects.link(obj)

        # --- Step 4: Verify Broken Path & Fix ---
        with self.subTest(step="4. Verify & Fix Paths"):
            img = bpy.data.images.get("TestImage")
            self.assertIsNotNone(img)

            path_norm = img.filepath.replace("\\", "/")
            print(f"Path before fix: {path_norm}")

            # If Blender didn't break it automatically, we force it to ensure our logic runs
            if not path_norm.startswith("//../../"):
                print("Note: Manually breaking path for test coverage...")
                img.filepath = "//../../" + self.texture_name

            # Execute the fix logic
            unmap_snapshot_paths()

            # Verify Fix
            path_fixed_norm = img.filepath.replace("\\", "/")
            print(f"Path after fix: {path_fixed_norm}")

            self.assertFalse(path_fixed_norm.startswith("//../../"), "Path should not contain deep relative steps")
            self.assertTrue(path_fixed_norm.endswith(self.texture_name), "Path should point to texture")

        print("Rescue Unmap Logic Scenario: Completed")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
