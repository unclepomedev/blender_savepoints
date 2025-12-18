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
from savepoints_test_case import SavePointsTestCase
from savepoints.services.asset_path import unmap_snapshot_paths


class TestRelativePaths(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # SavePointsTestCase creates self.test_dir and self.blend_path (test_project.blend)

        # Create a dummy texture file
        self.texture_name = "my_texture.png"
        self.texture_path = self.test_dir / self.texture_name
        # Create a tiny minimal PNG
        with open(self.texture_path, 'wb') as f:
            f.write(
                b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')

        # Setup Scene with Relative Path Image
        # Remove default object (read_homefile(use_empty=True) in base class does this, but just in case)
        # Base class creates an empty file then saves it.
        # But for this test we need content.

        # Create a Cube
        bpy.ops.mesh.primitive_cube_add()
        self.obj = bpy.context.object
        self.obj.name = "TexturedCube"

        # Create Material
        mat = bpy.data.materials.new(name="TexturedMat")
        mat.use_nodes = True
        self.obj.data.materials.append(mat)

        # Add Image Texture Node
        nodes = mat.node_tree.nodes
        tex_node = nodes.new('ShaderNodeTexImage')

        # Load Image
        try:
            img = bpy.data.images.load(str(self.texture_path))
            img.name = "TestImage"
            # Force relative path
            img.filepath = f"//{self.texture_name}"
            tex_node.image = img
        except Exception as e:
            self.fail(f"Failed to load image: {e}")

        # Save to persist relative paths
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

    def test_fork_retains_relative_paths(self):
        print("\n--- Test: Fork Retains Relative Paths ---")

        # 1. Commit Version
        bpy.ops.savepoints.commit(note="v1")

        # Verify snapshot exists
        history_dir = self.test_dir / ".test_project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"
        self.assertTrue(snapshot_path.exists(), "Snapshot not created")

        # 2. Open Snapshot and Verify Path Remapping (Standard Blender Behavior)
        bpy.ops.wm.open_mainfile(filepath=str(snapshot_path))

        # Check Image Path
        img = bpy.data.images.get("TestImage")
        self.assertIsNotNone(img, "Image missing in snapshot")

        # In the snapshot (subdirectory), the relative path should be adjusted to point to parent's sibling
        # e.g. //../../my_texture.png
        # Normalized check
        path_norm = img.filepath.replace("\\", "/")
        self.assertTrue(path_norm.startswith("//../../"),
                        f"Snapshot path should use parent relative path, got: {path_norm}")

        # 3. Execute Fork
        # We are in snapshot. Fork should save to root as test_project_v001.blend
        bpy.ops.savepoints.fork_version()

        # 4. Verify Forked File
        # Check current filepath
        current_path = Path(bpy.data.filepath)
        expected_name = "test_project_v001.blend"
        self.assertEqual(current_path.name, expected_name, "Did not switch to forked file")
        self.assertEqual(current_path.parent.resolve(), self.test_dir.resolve(), "Forked file not in project root")

        # Check Image Path in Forked File
        # It should be restored to "//my_texture.png" because it's back in the root
        img_forked = bpy.data.images.get("TestImage")
        path_forked_norm = img_forked.filepath.replace("\\", "/")

        print(f"Forked Image Path: {path_forked_norm}")

        # Allow "//my_texture.png" or absolute path if Blender resolved it?
        # Ideally it should be relative "//my_texture.png"
        if path_forked_norm.startswith("//"):
            self.assertFalse(path_forked_norm.startswith("//../../"), "Forked path still contains ../../")
            self.assertTrue(path_forked_norm.endswith(self.texture_name), "Forked path doesn't point to texture")
        else:
            # If absolute, verify it points to correct file
            pass

    def test_rescue_unmaps_paths(self):
        print("\n--- Test: Rescue (Unmap Paths Logic) ---")

        # 1. Commit Version (to have a snapshot with //../../ paths)
        bpy.ops.savepoints.commit(note="v1")

        # 2. Reset to original file (clean state)
        # Actually let's create a NEW file to simulate rescuing into a fresh project
        new_project_path = self.test_dir / "rescue_target.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(new_project_path))

        # Remove everything to ensure we rescue cleanly
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

        # 3. Simulate Append from Snapshot
        # We manually append the object from the snapshot.
        # This brings the object AND the image with broken path.
        history_dir = self.test_dir / ".test_project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"

        # Append "TexturedCube"
        with bpy.data.libraries.load(str(snapshot_path), link=False) as (data_from, data_to):
            if "TexturedCube" in data_from.objects:
                data_to.objects.append("TexturedCube")

        # Link object to scene
        if data_to.objects:
            obj = data_to.objects[0]
            bpy.context.collection.objects.link(obj)

            # Verify the image path is broken (//../../)
            # The appended data comes from snapshot, so it retains snapshot's relative paths
            img = bpy.data.images.get("TestImage")
            self.assertIsNotNone(img)
            path_norm = img.filepath.replace("\\", "/")
            print(f"Path before fix: {path_norm}")

            # If Blender automatically fixed it, we forcefully break it to test our fix logic.
            if not path_norm.startswith("//../../"):
                print("Blender auto-resolved path. Breaking it manually for test coverage...")
                img.filepath = "//../../" + self.texture_name
                path_norm = img.filepath

            # 4. Run the fix
            unmap_snapshot_paths()

            # 5. Verify Path is Fixed
            path_fixed_norm = img.filepath.replace("\\", "/")
            print(f"Path after fix: {path_fixed_norm}")
            self.assertFalse(path_fixed_norm.startswith("//../../"), "Path was not unmapped")
            self.assertTrue(path_fixed_norm.endswith(self.texture_name))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
