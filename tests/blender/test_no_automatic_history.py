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

from savepoints_test_case import SavePointsTestCase


class TestNoAutomaticHistory(SavePointsTestCase):
    def test_no_automatic_history(self):
        print("Starting No Automatic History Creation Test...")
        # SavePointsTestCase creates test_project.blend
        # And registers the addon (which might trigger load_post)

        history_dir = self.test_dir / ".test_project_history"

        # 1. Verify history dir does NOT exist immediately after setup/registration
        if history_dir.exists():
            self.fail(f"History directory created automatically! {history_dir}")

        print("History directory correctly missing.")

        # 2. Simulate loading the file (which triggers load_post handler)
        print("Simulating file load...")
        # Note: save_as_mainfile might not trigger load_post in background mode in the same way,
        # but we can explicitly call the handler or reload the file.
        bpy.ops.wm.open_mainfile(filepath=str(self.blend_path))

        # Verify history dir does NOT exist
        if history_dir.exists():
            self.fail(f"History directory created automatically after load! {history_dir}")

        # 3. Verify that calling sync_history_to_props manually also doesn't create it
        from savepoints import ui_utils
        ui_utils.sync_history_to_props(bpy.context)

        if history_dir.exists():
            self.fail(f"History directory created by sync_history_to_props! {history_dir}")

        print("History directory still missing after sync.")
        print("Test Passed!")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
