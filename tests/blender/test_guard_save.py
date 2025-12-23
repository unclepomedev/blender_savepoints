import sys
import time
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


class TestGuardSaveScenario(SavePointsTestCase):

    def test_guard_save_flow_scenario(self):
        """
        Scenario:
        1. Open a normal .blend file and trigger 'guard_save'.
           -> Verify that the file IS saved (mtime updates).
        2. Save as a .blend_snapshot file.
        3. Trigger 'guard_save' on the snapshot.
           -> Verify that the operation is BLOCKED (returns CANCELLED, mtime unchanged).
        """
        print("Starting Guard Save Scenario...")

        # --- Step 1: Normal File Save ---
        with self.subTest(step="1. Guard Save on Normal File"):
            print("Testing Normal File Save...")

            # Ensure we are in the standard setup file
            self.assertTrue(str(self.blend_path).endswith(".blend"))

            # Get initial mtime
            initial_mtime = self.blend_path.stat().st_mtime

            # Wait a bit to ensure mtime difference if saved
            # (Filesystem mtime resolution can be coarse)
            time.sleep(1.1)

            # Execute operator
            # In a normal file, this invokes standard save
            bpy.ops.savepoints.guard_save()

            # Check if file updated
            current_mtime = self.blend_path.stat().st_mtime

            # It should have saved
            self.assertNotEqual(initial_mtime, current_mtime,
                                "Normal .blend file should have been saved (mtime updated)")

        # --- Step 2: Snapshot File Block ---
        with self.subTest(step="2. Guard Save on Snapshot File"):
            print("Testing Snapshot File Guard...")

            # Create a fake snapshot file by saving the current one
            snapshot_path = self.test_dir / "test_project.blend_snapshot"
            bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path))

            # Verify context
            self.assertTrue(bpy.data.filepath.endswith(".blend_snapshot"),
                            "Context did not switch to .blend_snapshot")

            # Get initial mtime
            initial_mtime = snapshot_path.stat().st_mtime

            # Wait a bit
            time.sleep(1.1)

            # Execute operator
            # This should be blocked
            res = bpy.ops.savepoints.guard_save()

            # Verify Result
            self.assertIn('CANCELLED', res, "Operator should return CANCELLED on snapshot")

            # Verify File was NOT touched
            current_mtime = snapshot_path.stat().st_mtime
            self.assertEqual(initial_mtime, current_mtime,
                             "Snapshot file should NOT have been saved (mtime unchanged)")

        print("Guard Save Scenario: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
