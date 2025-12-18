import shutil
import sys
import unittest
from pathlib import Path

import bpy

from savepoints.services.storage import RESCUE_TEMP_FILENAME

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints


class TestCleanupOnRefresh(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_cleanup_refresh_env"
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

        # Save current blend file there
        self.blend_path = self.test_dir / "test.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

        savepoints.register()

    def tearDown(self):
        savepoints.unregister()
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_cleanup_on_refresh(self):
        print("\n--- Test Cleanup on Refresh ---")

        # 1. Setup History and Version
        history_dir = self.test_dir / ".test_history"
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
