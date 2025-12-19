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


class TestForkCollision(SavePointsTestCase):

    def test_fork_collision_handling(self):
        """
        Scenario:
        1. Create version v001.
        2. Checkout v001.
        3. Create a dummy file that conflicts with the expected fork name (test_project_v001.blend).
        4. Execute Fork -> Expect test_project_v001_001.blend.
        5. Create a dummy file that conflicts with the first fallback (test_project_v001_001.blend).
        6. Execute Fork again -> Expect test_project_v001_002.blend.
        """
        print("Starting Fork Collision Handling Scenario...")

        # --- Step 1: Create Base Version ---
        with self.subTest(step="1. Create Base Version"):
            bpy.ops.mesh.primitive_cube_add()
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Base Version")
            self.assertIn('FINISHED', res, "Commit failed")

        # --- Step 2: Checkout ---
        with self.subTest(step="2. Checkout Snapshot"):
            bpy.context.scene.savepoints_settings.active_version_index = 0
            res = bpy.ops.savepoints.checkout()
            self.assertIn('FINISHED', res, "Checkout failed")

        # --- Step 3: Simulate Collision 1 ---
        # The default fork name logic is {project_name}_{version_id}.blend
        # Our test project is "test_project.blend", so expected fork name is "test_project_v001.blend"

        expected_base_name = "test_project_v001.blend"
        collision_path_1 = self.test_dir / expected_base_name

        print(f"Creating collision file: {collision_path_1}")
        collision_path_1.touch()  # Create empty file

        # Execute Fork
        with self.subTest(step="3. Fork with Collision 1"):
            res = bpy.ops.savepoints.fork_version('EXEC_DEFAULT')
            self.assertIn('FINISHED', res, "Fork failed")

            current_path = Path(bpy.data.filepath)
            print(f"Forked to: {current_path.name}")

            # Expect incremented name
            expected_name_1 = "test_project_v001_001.blend"
            self.assertEqual(current_path.name, expected_name_1,
                             f"Expected {expected_name_1}, got {current_path.name}")

        # --- Return to Snapshot Mode for next test ---
        # Fork switches to the new file, so we are no longer in snapshot mode.
        # We need to open the snapshot again to test another fork from the same source snapshot.

        # Actually, simpler: load the original project, then checkout v001 again.
        bpy.ops.wm.open_mainfile(filepath=str(self.blend_path))
        bpy.context.scene.savepoints_settings.active_version_index = 0
        bpy.ops.savepoints.checkout()

        # --- Step 5: Simulate Collision 2 (Base + 001 exists) ---
        expected_name_001 = "test_project_v001_001.blend"
        collision_path_2 = self.test_dir / expected_name_001

        # Ensure the first collision file also still exists
        if not collision_path_1.exists():
            collision_path_1.touch()

        print(f"Collision files existing: {collision_path_1.name}, {collision_path_2.name}")

        with self.subTest(step="5. Fork with Collision 2"):
            res = bpy.ops.savepoints.fork_version('EXEC_DEFAULT')
            self.assertIn('FINISHED', res, "Fork failed")

            current_path = Path(bpy.data.filepath)
            print(f"Forked to: {current_path.name}")

            expected_name_2 = "test_project_v001_002.blend"
            self.assertEqual(current_path.name, expected_name_2,
                             f"Expected {expected_name_2}, got {current_path.name}")


if __name__ == "__main__":
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
