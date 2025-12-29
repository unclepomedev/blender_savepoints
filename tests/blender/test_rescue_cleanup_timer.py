import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services import rescue
from savepoints_test_case import SavePointsTestCase


class TestRescueCleanupTimer(SavePointsTestCase):
    def test_delete_rescue_temp_file_registers_timer(self):
        """
        Verify that delete_rescue_temp_file registers a timer 
        and that the callback actually deletes the file.
        """
        print("Starting Rescue Cleanup Timer Test...")

        # Create a dummy file
        temp_file = self.test_dir / "temp_rescue.blend"
        temp_file.touch()

        with patch("bpy.app.timers.register") as mock_register:
            # Execute with specific delay
            rescue.delete_rescue_temp_file(temp_file, delay=5.0)

            # Verify timer registered
            mock_register.assert_called_once()
            args, kwargs = mock_register.call_args
            callback_func = args[0]
            delay_arg = kwargs.get('first_interval')

            self.assertEqual(delay_arg, 5.0)
            self.assertTrue(callable(callback_func))

            print("Timer registered successfully.")

            # Now verify the callback logic itself (Success case)
            print("Verifying callback execution (Success case)...")
            result = callback_func()  # Should delete file and return None
            self.assertIsNone(result)
            self.assertFalse(temp_file.exists(), "File should be deleted by callback")

    def test_delete_retry_logic(self):
        """
        Verify that the callback retries on PermissionError and eventually gives up.
        """
        print("Starting Retry Logic Test...")
        temp_file = self.test_dir / "temp_retry.blend"
        temp_file.touch()

        # Use 2 retries for this test
        with patch("bpy.app.timers.register") as mock_register:
            rescue.delete_rescue_temp_file(temp_file, delay=1.0, max_retries=2)
            callback_func = mock_register.call_args[0][0]

            # Simulate Lock (failure) using mock
            with patch("os.remove", side_effect=PermissionError("Locked")):
                # Attempt 1 (Retries left: 2 -> 1)
                retry_delay = callback_func()
                self.assertEqual(retry_delay, 1.0, "Should return retry delay (1.0) on first failure")

                # Attempt 2 (Retries left: 1 -> 0)
                retry_delay_2 = callback_func()
                self.assertEqual(retry_delay_2, 1.0, "Should return retry delay (1.0) on second failure")

                # Attempt 3 (Retries left: 0 -> give up)
                final_result = callback_func()
                self.assertIsNone(final_result, "Should return None (give up) after retries exhausted")

        # Clean up the file manually since logic gave up
        if temp_file.exists():
            temp_file.unlink()


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
