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

from savepoints_test_case import SavePointsTestCase
from savepoints.services import retrieve


class TestRetrieveObjectsPathFix(SavePointsTestCase):
    def test_retrieve_fixes_relative_paths(self):
        print("Starting Retrieve Path Fix Test...")

        # 1. Setup: Create a texture and an object using it with relative path //texture.png
        tex_name = "test_texture.png"
        tex_path = self.test_dir / tex_name
        with open(tex_path, "wb") as f:
            f.write(b"fake image data")

        # Create Image datablock
        img = bpy.data.images.new("TestImage", width=64, height=64)
        img.filepath = f"//{tex_name}"
        img.source = 'FILE'
        img.use_fake_user = True

        # Save project to establish root
        bpy.ops.wm.save_mainfile()

        # Verify initial path
        self.assertEqual(img.filepath, f"//{tex_name}")

        # 2. Commit (Create Snapshot)
        # This will create .history/v001/snapshot.blend_snapshot
        # Blender should remap the path in snapshot to //../../test_texture.png
        bpy.ops.savepoints.commit(note="v1")

        # 3. Verify Snapshot Path (Optional but good for debugging)

        # 4. Clear Scene
        bpy.ops.wm.read_factory_settings(use_empty=True)
        retrieve_target = self.test_dir / "retrieve_target.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(retrieve_target))

        # 5. Retrieve
        # We need the snapshot path
        history_dir = self.test_dir / ".test_project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"

        self.assertTrue(snapshot_path.exists(), "Snapshot must exist")

        # Create temp file (simulating what operator does)
        temp_path = retrieve.create_retrieve_temp_file(snapshot_path)

        try:
            pass
        finally:
            # We will restart the test logic to include an object
            pass

    def test_retrieve_fixes_relative_paths_full(self):
        print("Starting Full Retrieve Path Fix Test...")

        # 1. Setup Texture
        tex_name = "test_texture.png"
        tex_path = self.test_dir / tex_name
        with open(tex_path, "wb") as f:
            f.write(b"fake image data")

        # 2. Create "Snapshot" file manually with deep path
        history_dir = self.test_dir / ".test_project_history"
        version_dir = history_dir / "v001"
        version_dir.mkdir(parents=True, exist_ok=True)
        snapshot_path = version_dir / "snapshot.blend_snapshot"

        bpy.ops.wm.read_factory_settings(use_empty=True)

        # Create Image with deep relative path
        img = bpy.data.images.new("TestImage", width=64, height=64)
        # version_dir is .history/v001 (2 levels down)
        img.filepath = f"//../../{tex_name}"

        # Create Object using this image
        bpy.ops.object.empty_add(type='IMAGE')
        obj = bpy.context.object
        obj.name = "ImageUser"
        obj.data = img

        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path))
        print(f"Created manual snapshot with path: {img.filepath}")

        # 3. Prepare Target Project
        retrieve_target = self.test_dir / "retrieve_target.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(retrieve_target))

        # Clear current objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        bpy.data.images.remove(bpy.data.images["TestImage"])  # Clear image

        # 4. Retrieve
        temp_path = retrieve.create_retrieve_temp_file(snapshot_path)

        try:
            # Execute append_objects
            print("Executing append_objects...")
            retrieve.append_objects(temp_path, ["ImageUser"])

            # 5. Verify
            new_obj = bpy.data.objects.get("ImageUser")
            self.assertIsNotNone(new_obj)
            new_img = new_obj.data
            self.assertIsNotNone(new_img)

            print(f"Retrieved Image Path: {new_img.filepath}")

            # Normalized check
            path_norm = new_img.filepath.replace("\\", "/")

            self.assertEqual(path_norm, f"//{tex_name}",
                             f"Path was not fixed! Got: {path_norm}")

        finally:
            retrieve.delete_retrieve_temp_file(temp_path)


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
