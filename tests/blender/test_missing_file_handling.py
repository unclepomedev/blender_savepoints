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


class TestMissingFileHandling(SavePointsTestCase):

    def test_missing_file_handling_scenario(self):
        """
        Scenario:
        1. Create a valid version (v001).
        2. Sabotage: Manually delete the snapshot file from the disk.
        3. Attempt Checkout: Verify that the operator fails gracefully (raises RuntimeError).
        4. Safety Check: Verify that the current file path has NOT changed (Blender didn't crash or load an empty state).
        """
        print("Starting Missing File Handling Scenario...")

        # Setup expected paths
        history_dir = self.test_dir / ".test_project_history"
        # Assuming v001 is the first version created
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"

        # --- Step 1: Create Version ---
        with self.subTest(step="1. Create Version"):
            print("Creating version v001...")

            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="To be broken")
            self.assertIn('FINISHED', res, "Commit failed")

            # Verify snapshot file exists
            self.assertTrue(snapshot_path.exists(), "Setup failed: Snapshot file was not created.")

        # --- Step 2: Sabotage (Delete File) ---
        with self.subTest(step="2. Sabotage"):
            print("Deleting snapshot file...")

            snapshot_path.unlink()
            self.assertFalse(snapshot_path.exists(), "Failed to delete snapshot file for test")

        # --- Step 3: Attempt Checkout (Expect Failure) ---
        with self.subTest(step="3. Attempt Checkout"):
            print("Attempting Checkout on missing file...")

            # Set target to the broken version
            bpy.context.scene.savepoints_settings.active_version_index = 0

            # In headless mode, operators that report {'ERROR'} raise a RuntimeError.
            # We assert that this error IS raised.
            with self.assertRaises(RuntimeError, msg="Checkout should raise RuntimeError when file is missing"):
                bpy.ops.savepoints.checkout('EXEC_DEFAULT')

        # --- Step 4: Verify Safety State ---
        with self.subTest(step="4. Verify Safety"):
            print("Verifying fail-safe state...")

            # The operator should abort loading and leave us in the original file.
            current_path = Path(bpy.data.filepath)

            self.assertEqual(
                current_path,
                self.blend_path,
                f"Safety check failed: Filepath changed to {current_path} despite error"
            )

        print("Missing File Handling Scenario: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
