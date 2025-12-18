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
from savepoints.services.ghost import load_ghost, unload_ghost, get_ghost_collection_name


class TestGhost(SavePointsTestCase):

    def test_ghost_lifecycle_scenario(self):
        """
        Scenario:
        1. Create a version containing a specific object ("GhostCube").
        2. Delete the object from the current scene (to make the ghost useful).
        3. Load the Ghost (Link from snapshot) and verify its properties (Wireframe, Unselectable).
        4. Unload the Ghost and verify cleanup (Collections and Libraries removed).
        """
        print("Starting Ghost Lifecycle Scenario...")

        # Variable to hold the version ID we create
        version_id = "v001"

        # --- Step 1: Create Base Version ---
        with self.subTest(step="1. Create Base Version"):
            print("Creating version with GhostCube...")

            # Create a simple object
            bpy.ops.mesh.primitive_cube_add()
            cube = bpy.context.object
            cube.name = "GhostCube"
            # Move cube so we can distinguish it from origin
            cube.location = (2, 0, 0)

            # Save changes to main file first
            bpy.ops.wm.save_mainfile()

            # Create version
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Version with Cube")
            self.assertIn('FINISHED', res, "Commit failed")

        # --- Step 2: Modify Current Scene ---
        with self.subTest(step="2. Modify Current Scene"):
            # Delete the cube so the ghost is meaningful (showing past state)
            cube = bpy.data.objects.get("GhostCube")
            if cube:
                bpy.data.objects.remove(cube)

            self.assertNotIn("GhostCube", bpy.data.objects, "Cube should be deleted from current scene")

        # --- Step 3: Load Ghost & Verify Properties ---
        with self.subTest(step="3. Load Ghost"):
            print(f"Loading ghost for {version_id}...")

            count = load_ghost(version_id, bpy.context)
            self.assertGreater(count, 0, "Ghost should load at least one object")

            col_name = get_ghost_collection_name(version_id)
            self.assertIn(col_name, bpy.data.collections, "Ghost collection should exist")

            ghost_col = bpy.data.collections[col_name]
            self.assertTrue(len(ghost_col.objects) > 0, "Ghost collection should contain objects")

            # Verify visualization properties (Ghosts should be non-intrusive)
            ghost_obj = ghost_col.objects[0]
            self.assertEqual(ghost_obj.display_type, 'WIRE', "Ghost object should be displayed as WIRE")
            self.assertTrue(ghost_obj.hide_select, "Ghost object should be non-selectable")

        # --- Step 4: Unload Ghost ---
        with self.subTest(step="4. Unload Ghost"):
            print(f"Unloading ghost for {version_id}...")
            unload_ghost(version_id, bpy.context)

        # --- Step 5: Verify Cleanup ---
        with self.subTest(step="5. Verify Cleanup"):
            col_name = get_ghost_collection_name(version_id)
            self.assertNotIn(col_name, bpy.data.collections, "Ghost collection should be gone")

            # Verify no linked libraries left
            # We check if any library path contains our version ID, implying a leak
            for lib in bpy.data.libraries:
                if lib.filepath and version_id in lib.filepath:
                    self.fail(f"Library {lib.filepath} was not cleaned up after unloading ghost")

        print("Ghost Lifecycle Scenario: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
