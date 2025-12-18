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


class TestCommitSelectionPersistence(SavePointsTestCase):

    def test_selection_persistence(self):
        """
        Scenario:
        1. Create objects and select specific ones.
        2. Enter a specific mode (e.g., EDIT).
        3. Perform Commit.
        4. Verify that the selection and mode are preserved.
        """
        print("Starting Selection Persistence Scenario...")

        # --- Step 1: Setup Objects and Selection ---
        with self.subTest(step="1. Setup Selection"):
            # Create Cube (Active)
            bpy.ops.mesh.primitive_cube_add()
            cube = bpy.context.active_object
            cube.name = "ActiveCube"

            # Create Sphere (Selected, not active)
            bpy.ops.mesh.primitive_uv_sphere_add(location=(2, 0, 0))
            sphere = bpy.context.active_object
            sphere.name = "SelectedSphere"

            # Set selection: Cube Active, Sphere Selected
            bpy.ops.object.select_all(action='DESELECT')
            cube.select_set(True)
            sphere.select_set(True)
            bpy.context.view_layer.objects.active = cube

            self.assertEqual(bpy.context.active_object, cube)
            self.assertTrue(cube.select_get())
            self.assertTrue(sphere.select_get())

        # --- Step 2: Enter Mode ---
        with self.subTest(step="2. Enter Mode"):
            # Enter EDIT mode on the active object (Cube)
            bpy.ops.object.mode_set(mode='EDIT')
            self.assertEqual(bpy.context.object.mode, 'EDIT')

        # --- Step 3: Perform Commit ---
        with self.subTest(step="3. Perform Commit"):
            print("Executing Commit...")
            # Commit usually triggers thumbnail capture (render.opengl) which might reset mode/selection
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Testing Persistence")
            self.assertIn('FINISHED', res, "Commit failed")

        # --- Step 4: Verify Persistence ---
        with self.subTest(step="4. Verify Persistence"):
            print("Verifying state...")

            # 1. Check Mode
            # Note: In some headless environments, render.opengl might fail or behave differently,
            # but our logic should attempt to restore the mode regardless.
            self.assertEqual(bpy.context.object.mode, 'EDIT', "Mode was reset after commit")

            # 2. Check Active Object
            # Need to switch to OBJECT mode to check selection reliably if needed,
            # but checking active object name works in EDIT mode too.
            self.assertEqual(bpy.context.active_object.name, "ActiveCube", "Active object changed")

            # 3. Check Selection
            # To check selection of other objects, we might need to be in OBJECT mode or check graph.
            # Let's switch to OBJECT for robust verification.
            bpy.ops.object.mode_set(mode='OBJECT')

            cube = bpy.data.objects["ActiveCube"]
            sphere = bpy.data.objects["SelectedSphere"]

            self.assertTrue(cube.select_get(), "ActiveCube lost selection")
            self.assertTrue(sphere.select_get(), "SelectedSphere lost selection")
            self.assertEqual(bpy.context.view_layer.objects.active, cube, "Active object mismatch in Object Mode")

        print("Selection Persistence Scenario: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
