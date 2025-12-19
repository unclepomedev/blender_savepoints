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

# Import specific module for explicit function call verification
from savepoints import ui_utils
from savepoints_test_case import SavePointsTestCase


class TestNoAutomaticHistory(SavePointsTestCase):

    def test_no_automatic_history_scenario(self):
        """
        Scenario:
        1. Verify that simply enabling the addon or starting Blender does not create a history folder.
        2. Verify that loading a project file does not trigger automatic folder creation.
        3. Verify that internal sync functions (UI updates) do not create the folder.
        """
        print("Starting No Automatic History Creation Scenario...")

        # Setup expected path
        # SavePointsTestCase creates 'test_project.blend'
        history_dir = self.test_dir / ".test_project_history"

        # --- Step 1: Initial State Check ---
        with self.subTest(step="1. Initial State"):
            # Check immediately after setup/registration
            self.assertFalse(
                history_dir.exists(),
                f"History directory created automatically on startup! {history_dir}"
            )

        # --- Step 2: File Load Simulation ---
        with self.subTest(step="2. File Load Simulation"):
            print("Simulating file load...")

            # Explicitly reload the file to trigger load_post handlers
            bpy.ops.wm.open_mainfile(filepath=str(self.blend_path))

            # Verify directory still doesn't exist
            self.assertFalse(
                history_dir.exists(),
                f"History directory created automatically after file load! {history_dir}"
            )

        # --- Step 3: Explicit Sync Call ---
        with self.subTest(step="3. Explicit Sync Check"):
            print("Calling sync_history_to_props()...")

            # Manually call the function that updates the UI list
            # This ensures that listing versions doesn't accidentally initialize storage
            ui_utils.sync_history_to_props(bpy.context)

            self.assertFalse(
                history_dir.exists(),
                f"History directory created by sync_history_to_props! {history_dir}"
            )

        print("No Automatic History Scenario: Completed")


if __name__ == "__main__":
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
