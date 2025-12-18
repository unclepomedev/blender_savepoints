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


class TestGhostReference(SavePointsTestCase):

    def test_ghost_reference_scenario(self):
        """
        Scenario:
        1. Create a version with initial content (OriginalCube).
        2. Modify the scene (move the cube) to diverge from the saved state.
        3. Toggle Ghost ON: Verify the ghost collection appears with correct visual properties (Wireframe, Unselectable).
        4. Toggle Ghost OFF: Verify the ghost collection is cleanly removed.
        """
        print("Starting Ghost Reference Scenario...")

        # Variable to store the target version ID
        version_id = None

        # --- Step 1: Create Content & Commit ---
        with self.subTest(step="1. Create Content & Commit"):
            print("Creating initial content...")

            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            cube = bpy.context.active_object
            cube.name = "OriginalCube"

            # Save Snapshot (bypass dialog)
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Initial")
            self.assertIn('FINISHED', res, "Commit failed")

            # Retrieve the ID of the created version
            settings = bpy.context.scene.savepoints_settings
            self.assertTrue(len(settings.versions) > 0, "Version should be created")

            # Note: We established in previous turns that the property is 'version_id'
            version_id = settings.versions[0].version_id
            print(f"Created version ID: {version_id}")

        # --- Step 2: Modify Scene ---
        with self.subTest(step="2. Modify Scene"):
            # Move the live cube so it visually differs from where the ghost will appear
            cube = bpy.data.objects.get("OriginalCube")
            self.assertIsNotNone(cube, "OriginalCube should exist")
            cube.location.x += 5.0

        # --- Step 3: Toggle Ghost ON ---
        with self.subTest(step="3. Toggle Ghost ON"):
            print(f"Toggling Ghost ON for {version_id}...")

            res = bpy.ops.savepoints.toggle_ghost(version_id=version_id)
            self.assertIn('FINISHED', res)

            # Verify Collection Existence
            col_name = f"Ghost_Reference_{version_id}"
            ghost_col = bpy.data.collections.get(col_name)
            self.assertIsNotNone(ghost_col, f"Ghost collection '{col_name}' missing")

            # Verify Ghost Objects
            self.assertGreater(len(ghost_col.objects), 0, "Ghost collection is empty")
            ghost_obj = ghost_col.objects[0]

            # Verify Visual Properties (Ghost should be a non-intrusive reference)
            self.assertEqual(ghost_obj.display_type, 'WIRE', "Ghost object not set to WIRE display")
            self.assertTrue(ghost_obj.hide_select, "Ghost object is selectable (should be unselectable)")

            print(f"Verified Ghost Object: {ghost_obj.name}")

        # --- Step 4: Toggle Ghost OFF ---
        with self.subTest(step="4. Toggle Ghost OFF"):
            print(f"Toggling Ghost OFF for {version_id}...")

            # Toggling again should remove it
            res = bpy.ops.savepoints.toggle_ghost(version_id=version_id)
            self.assertIn('FINISHED', res)

            # Verify Cleanup
            col_name = f"Ghost_Reference_{version_id}"
            self.assertNotIn(col_name, bpy.data.collections, "Ghost collection was not removed")

        print("Ghost Reference Scenario: Completed")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
