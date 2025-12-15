import shutil
import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import core


class TestTagging(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_tagging_env"
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

        # Save current blend file
        self.blend_path = self.test_dir / "test.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

        savepoints.register()

    def tearDown(self):
        try:
            savepoints.unregister()
        except Exception:
            pass
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_set_tag(self):
        print("\n--- Test Set Tag ---")

        # 1. Create Version
        # Ensure we have active object for thumbnail (not strictly needed but good practice)
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Initial")

        settings = bpy.context.scene.savepoints_settings
        self.assertTrue(len(settings.versions) > 0, "Version should be created")

        # Get latest version
        v1 = settings.versions[0]
        v1_id = v1.version_id

        # Verify default tag
        print(f"Checking default tag for {v1_id}...")
        self.assertEqual(v1.tag, 'NONE', "Default tag should be NONE")

        # 2. Set Tag to STABLE
        print(f"Setting tag for {v1_id} to STABLE...")
        bpy.ops.savepoints.set_tag('EXEC_DEFAULT', version_id=v1_id, tag='STABLE')

        # 3. Verify in Props (Immediate update via sync)
        v1_updated = settings.versions[0]
        self.assertEqual(v1_updated.tag, 'STABLE', "Tag property should be STABLE")

        # 4. Verify in Manifest (Persistence)
        manifest = core.load_manifest()
        v_data = manifest["versions"][0]
        self.assertEqual(v_data["tag"], 'STABLE', "Manifest tag should be STABLE")

        # 5. Set Tag to BUG
        print(f"Setting tag for {v1_id} to BUG...")
        bpy.ops.savepoints.set_tag('EXEC_DEFAULT', version_id=v1_id, tag='BUG')

        v1_updated = settings.versions[0]
        self.assertEqual(v1_updated.tag, 'BUG', "Tag property should be BUG")

        manifest = core.load_manifest()
        v_data = manifest["versions"][0]
        self.assertEqual(v_data["tag"], 'BUG', "Manifest tag should be BUG")

        print("Tagging Test Passed.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
