import sys
import unittest
from pathlib import Path

import bpy

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
        print("\n--- Test Cleanup on Refresh ---")

        # 1. Setup History and Version
        # SavePointsTestCase creates test_project.blend, so history dir is .test_project_history
        history_dir = self.test_dir / ".test_project_history"
        version_id = "v001"
        version_dir = history_dir / version_id
        version_dir.mkdir(parents=True)

        # 2. Create the temp file (simulating a leftover)
        # Using the constant from core to ensure we are testing the right filename
        temp_file_name = RESCUE_TEMP_FILENAME
        temp_file_path = version_dir / temp_file_name

        # Just create an empty file
        temp_file_path.touch()

        self.assertTrue(temp_file_path.exists(), "Temp file should exist before refresh")

        # 3. Call Refresh
        print("Calling savepoints.refresh()...")
        bpy.ops.savepoints.refresh()

        # 4. Verify deletion
        if temp_file_path.exists():
            self.fail(f"Temp file {temp_file_name} was NOT deleted after refresh.")
        else:
            print(f"Success: Temp file {temp_file_name} was deleted.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
