import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.storage import get_history_dir
from savepoints_test_case import SavePointsTestCase


class TestRescueAssets(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        # SavePointsTestCase sets up a file named "test_project.blend"
        self.history_dir = self.test_dir / ".test_project_history"

        # Verify environment matches expectation
        computed_dir = get_history_dir()
        if str(computed_dir) != str(self.history_dir):
            self.fail(f"Environment mismatch: Expected {self.history_dir}, got {computed_dir}")

    def test_rescue_assets_scenario(self):
        """
        Scenario:
        1. Standard Snapshot: Create a .blend_snapshot file, run operator.
           Verify it creates a temp file and attempts to open the append dialog.
        2. Legacy Snapshot: Create a .blend file (old format), run operator.
           Verify it handles it correctly as above.
        3. Invalid Version: Run operator with non-existent ID.
           Verify it fails gracefully (CANCELLED).
        """
        print("Starting Rescue Assets Scenario...")

        # We patch the method that actually calls 'wm.append' (UI).
        # This prevents RuntimeError in headless mode and allows us to inspect the path passed to it.
        # Note: We patch the class method, so the instance created by bpy.ops uses the mock.
        with patch("savepoints.operators.SAVEPOINTS_OT_rescue_assets._open_append_dialog") as mock_open_dialog:

            # --- Step 1: Standard Snapshot (.blend_snapshot) ---
            with self.subTest(step="1. Standard Snapshot"):
                version_id = "v001"
                version_dir = self.history_dir / version_id
                version_dir.mkdir(parents=True, exist_ok=True)

                # Create dummy snapshot
                snapshot_path = version_dir / "snapshot.blend_snapshot"
                bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)

                # Execute Operator
                res = bpy.ops.savepoints.rescue_assets(version_id=version_id)

                # Verification
                self.assertEqual(res, {'FINISHED'}, "Operator should finish successfully when mocked")

                # Check if temp file was generated (Real IO check)
                temp_file = version_dir / "snapshot_rescue_temp.blend"
                self.assertTrue(temp_file.exists(), "Temp rescue file should be created on disk")

                # Check if UI dialog was requested with correct path
                mock_open_dialog.assert_called()
                args, _ = mock_open_dialog.call_args
                directory_arg = args[-1]  # Assuming directory is the last arg based on typical usage

                expected_part = f"{version_id}/snapshot_rescue_temp.blend/Object"
                # Normalize path for Windows/Mac
                self.assertIn(expected_part.replace("/", os.sep), str(directory_arg).replace("/", os.sep))

                # Cleanup for next step
                mock_open_dialog.reset_mock()

            # --- Step 2: Legacy Snapshot (.blend) ---
            with self.subTest(step="2. Legacy Snapshot"):
                version_id = "v002"
                version_dir = self.history_dir / version_id
                version_dir.mkdir(parents=True, exist_ok=True)

                # Create legacy snapshot
                snapshot_path = version_dir / "snapshot.blend"
                bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)

                # Execute Operator
                res = bpy.ops.savepoints.rescue_assets(version_id=version_id)

                # Verification
                self.assertEqual(res, {'FINISHED'})

                # Check temp file logic
                temp_file = version_dir / "snapshot_rescue_temp.blend"
                self.assertTrue(temp_file.exists(), "Temp file should be created from legacy snapshot")

                # Check UI call
                mock_open_dialog.assert_called_once()

                # Cleanup
                mock_open_dialog.reset_mock()

            # --- Step 3: Invalid Version ---
            with self.subTest(step="3. Invalid Version"):
                # Execute with missing version
                # In headless mode via bpy.ops, if an operator returns {'CANCELLED'},
                # it raises a RuntimeError.
                try:
                    bpy.ops.savepoints.rescue_assets(version_id="v999")
                    self.fail("Operator should fail for missing version")
                except RuntimeError:
                    # Expected behavior for CANCELLED operator
                    pass

                # Ensure UI was NOT called
                mock_open_dialog.assert_not_called()

        print("Rescue Assets Scenario: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
