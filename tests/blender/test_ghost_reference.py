import shutil
import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints


class TestGhostReference(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_ghost_env"
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

        # Start with empty scene before saving
        bpy.ops.wm.read_homefile(use_empty=True)

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

    def test_ghost_reference_toggle(self):
        print("\n--- Test Ghost Reference Toggle ---")

        # 1. Create content for snapshot

        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
        cube = bpy.context.active_object
        cube.name = "OriginalCube"

        # 2. Save Snapshot v001
        # Use EXEC_DEFAULT to bypass invoke dialog
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Initial")

        # Verify v001 created
        settings = bpy.context.scene.savepoints_settings
        # Need to sync? commit calls sync_history_to_props
        self.assertTrue(len(settings.versions) > 0, "Version should be created")
        v1_id = settings.versions[0].version_id
        print(f"Created version: {v1_id}")

        # 3. Modify Scene
        # Move the cube so we can visually distinguish (conceptually)
        cube.location.x += 5.0

        # 4. Toggle Ghost ON
        print(f"Toggling Ghost ON for {v1_id}...")
        res = bpy.ops.savepoints.toggle_ghost(version_id=v1_id)
        self.assertIn('FINISHED', res)

        # Verify Collection
        col_name = f"Ghost_Reference_{v1_id}"
        ghost_col = bpy.data.collections.get(col_name)
        self.assertIsNotNone(ghost_col, f"Ghost collection '{col_name}' should exist")

        # Verify Objects in Ghost
        self.assertTrue(len(ghost_col.objects) > 0, "Ghost collection should have objects")
        ghost_obj = ghost_col.objects[0]

        # Check properties
        self.assertEqual(ghost_obj.display_type, 'WIRE')
        self.assertTrue(ghost_obj.hide_select)

        print(f"Ghost Object Name: {ghost_obj.name}")

        # 5. Toggle Ghost OFF
        print(f"Toggling Ghost OFF for {v1_id}...")
        res = bpy.ops.savepoints.toggle_ghost(version_id=v1_id)
        self.assertIn('FINISHED', res)

        # Verify Collection Gone
        ghost_col = bpy.data.collections.get(col_name)
        self.assertIsNone(ghost_col, "Ghost collection should be removed")

        print("Ghost Reference Test Passed.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
