import sys
import unittest
import bpy
from pathlib import Path

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints_test_case import SavePointsTestCase
from savepoints.services.ghost import load_ghost, unload_ghost, get_ghost_collection_name


class TestGhost(SavePointsTestCase):
    def test_ghost_lifecycle(self):
        print("Starting Ghost Lifecycle Test...")

        # 1. Setup: Create a simple object and a version
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.object
        cube.name = "GhostCube"

        # Move cube so we can distinguish it
        cube.location = (2, 0, 0)

        # Save changes to main file first (required before commit usually)
        bpy.ops.wm.save_mainfile()

        # Create version v001
        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Version with Cube")
        self.assertIn('FINISHED', res)

        version_id = "v001"  # Assuming first version is v001

        # 2. Modify current scene (delete cube) so ghost is meaningful
        bpy.data.objects.remove(cube)

        # 3. Load Ghost
        print(f"Loading ghost for {version_id}...")
        count = load_ghost(version_id, bpy.context)
        self.assertGreater(count, 0, "Ghost should load at least one object")

        col_name = get_ghost_collection_name(version_id)
        self.assertIn(col_name, bpy.data.collections, "Ghost collection should exist")

        ghost_col = bpy.data.collections[col_name]
        self.assertTrue(len(ghost_col.objects) > 0, "Ghost collection should have objects")

        # Verify object properties
        ghost_obj = ghost_col.objects[0]
        self.assertEqual(ghost_obj.display_type, 'WIRE')
        self.assertTrue(ghost_obj.hide_select)

        # 4. Unload Ghost
        print(f"Unloading ghost for {version_id}...")
        unload_ghost(version_id, bpy.context)

        # 5. Verify Cleanup
        self.assertNotIn(col_name, bpy.data.collections, "Ghost collection should be gone")

        # Verify no linked libraries left (simple check)
        # Note: Depending on how Blender handles library cleanup, it might take a moment or need explicit gc, 
        # but our unload_ghost forces removal.
        for lib in bpy.data.libraries:
            # Check if any library points to our snapshot
            if version_id in lib.filepath:
                self.fail(f"Library {lib.filepath} was not cleaned up")

        print("Ghost Lifecycle Test Passed!")


if __name__ == "__main__":
    res = unittest.main(argv=[''], exit=False)
    sys.exit(not res.result.wasSuccessful())
