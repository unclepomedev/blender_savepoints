import sys
import unittest
from pathlib import Path

import bpy

# Add project root to path so we can import the addon modules
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.storage import RESCUE_TEMP_FILENAME
from savepoints_test_case import SavePointsTestCase


class TestCleanupOnRefresh(SavePointsTestCase):
    def test_cleanup_on_refresh(self):
        """
        Scenario:
        Simulate a leftover temporary file in a version directory and verify
        that the refresh operator correctly cleans it up.
        """
        print("Starting Cleanup on Refresh Test...")

        # Setup paths
        # SavePointsTestCase creates test_project.blend, so history dir is .test_project_history
        history_dir = self.test_dir / ".test_project_history"
        version_id = "v001"
        version_dir = history_dir / version_id

        # Ensure parent directories exist
        version_dir.mkdir(parents=True, exist_ok=True)

        temp_file_path = version_dir / RESCUE_TEMP_FILENAME

        # --- Step 1: Setup Dirty State (Create leftover file) ---
        with self.subTest(step="1. Simulate Leftover Temp File"):
            # Create an empty file to simulate a crash residue or temp file
            temp_file_path.touch()
            self.assertTrue(temp_file_path.exists(), "Setup failed: Temp file should exist before refresh")

        # --- Step 2: Action & Verification (Refresh and Check Deletion) ---
        with self.subTest(step="2. Refresh and Verify Cleanup"):
            print("Executing savepoints.refresh()...")

            # Execute the operator
            bpy.ops.savepoints.refresh()

            # Verify the file is gone
            self.assertFalse(
                temp_file_path.exists(),
                f"Cleanup failed: Temp file '{RESCUE_TEMP_FILENAME}' was NOT deleted after refresh."
            )

        print("Cleanup on Refresh Test: Completed")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
