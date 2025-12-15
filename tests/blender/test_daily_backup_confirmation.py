import sys
import tempfile
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints


class TestDailyBackupConfirmation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a dummy file to ensure context is valid
        cls.test_dir = tempfile.mkdtemp()
        cls.test_file = Path(cls.test_dir) / "test_daily_backup.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(cls.test_file))
        savepoints.register()

    @classmethod
    def tearDownClass(cls):
        savepoints.unregister()
        test_file = ROOT / "test_daily_backup.blend"
        if test_file.exists():
            test_file.unlink()

    def setUp(self):
        self.settings = bpy.context.scene.savepoints_settings
        # Ensure clean state: Default to False (as defined in properties)
        # But for test, we want to test disabling it, so we start with True.
        # Note: setting to True triggers update, but logic only cares if it becomes False.
        self.settings.keep_daily_backups = True

        # Ensure flag is cleared
        wm = bpy.context.window_manager
        if "savepoints_daily_backup_confirmed" in wm:
            del wm["savepoints_daily_backup_confirmed"]

    def test_direct_disable_reverts(self):
        print("\n--- Test: Direct Disable Reverts ---")
        # Attempt to disable directly
        self.settings.keep_daily_backups = False

        # Should have reverted to True because flag was missing
        self.assertTrue(self.settings.keep_daily_backups,
                        "Property should revert to True when disabled without confirmation")
        print("Passed: Property reverted successfully.")

    def test_operator_disable_succeeds(self):
        print("\n--- Test: Operator Disable Succeeds ---")
        # Run the confirmation operator
        # We use EXEC_DEFAULT to simulate 'OK' click (skips invoke)
        res = bpy.ops.savepoints.confirm_disable_daily_backups('EXEC_DEFAULT')

        self.assertIn('FINISHED', res)

        # Should be False now
        self.assertFalse(self.settings.keep_daily_backups, "Property should be False after confirmed operator")

        # Flag should be consumed (reset to False)
        wm = bpy.context.window_manager
        flag = wm.get("savepoints_daily_backup_confirmed", False)
        self.assertFalse(flag, "Confirmation flag should be reset after use")

        print("Passed: Operator disabled property successfully.")

    def test_enable_succeeds(self):
        print("\n--- Test: Enable Succeeds ---")
        # First ensure it is False
        # We can force it by setting flag manually if we wanted, or use operator.
        # Let's use the operator to get to False state cleanly
        bpy.ops.savepoints.confirm_disable_daily_backups('EXEC_DEFAULT')
        self.assertFalse(self.settings.keep_daily_backups)

        # Now enable
        self.settings.keep_daily_backups = True

        # Should be True
        self.assertTrue(self.settings.keep_daily_backups)
        print("Passed: Re-enabling works without confirmation.")


if __name__ == '__main__':
    # Use a custom test runner or just main
    unittest.main(argv=[''], exit=False)
