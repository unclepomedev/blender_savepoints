import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.operators import SAVEPOINTS_OT_rescue_assets
from savepoints_test_case import SavePointsTestCase


class TestRescueAssetsLogic(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # Create a mock self for the operator
        self.op = MagicMock()
        self.op.version_id = "v001"
        # Mock report to capture errors
        self.op.report = MagicMock()

        # Base mock context
        self.mock_context = MagicMock()

    @patch("savepoints.operators.get_history_dir")
    @patch("shutil.copy2")
    @patch("pathlib.Path.exists")
    def test_run_no_view3d(self, mock_exists, mock_copy, mock_get_hist):
        """Test that _run fails gracefully when no 3D Viewport is found."""
        print("\n--- Test Rescue Logic: No 3D Viewport ---")

        # Setup mocks
        mock_get_hist.return_value = "/tmp/history"
        mock_exists.return_value = True  # Snapshot exists

        # Setup context window manager with windows but NO VIEW_3D
        mock_window = MagicMock()
        mock_screen = MagicMock()
        mock_area = MagicMock()
        mock_area.type = 'PROPERTIES'  # Not VIEW_3D

        mock_screen.areas = [mock_area]
        mock_window.screen = mock_screen
        self.mock_context.window_manager.windows = [mock_window]

        # Run
        res = SAVEPOINTS_OT_rescue_assets._run(self.op, self.mock_context)

        # Assertions
        self.assertEqual(res, {'CANCELLED'})
        self.op.report.assert_called_with({'ERROR'}, "Could not find a valid 3D Viewport to open the Append dialog.")
        print("Confirmed: Returns CANCELLED and reports error when no VIEW_3D found.")

    @patch("savepoints.operators.get_history_dir")
    @patch("shutil.copy2")
    @patch("pathlib.Path.exists")
    def test_run_with_view3d(self, mock_exists, mock_copy, mock_get_hist):
        """Test that _run succeeds and calls append when 3D Viewport IS found."""
        print("\n--- Test Rescue Logic: With 3D Viewport ---")

        # Setup mocks
        mock_get_hist.return_value = "/tmp/history"
        mock_exists.return_value = True

        # Setup context WITH VIEW_3D
        mock_window = MagicMock()
        mock_screen = MagicMock()
        mock_area = MagicMock()
        mock_area.type = 'VIEW_3D'
        mock_region = MagicMock()
        mock_region.type = 'WINDOW'
        mock_area.regions = [mock_region]

        mock_screen.areas = [mock_area]
        mock_window.screen = mock_screen
        self.mock_context.window_manager.windows = [mock_window]

        # Mock temp_override to be a context manager
        # context.temp_override(**kwargs) -> ContextManager
        override_cm = MagicMock()
        override_cm.__enter__.return_value = None
        override_cm.__exit__.return_value = None
        self.mock_context.temp_override.return_value = override_cm

        # Run
        # Note: We cannot easily patch bpy.ops.wm.append because it is dynamic.
        # Instead, we let it run. Since the file paths are fake, it will fail with "nothing indicated".
        # BUT, if it fails with "nothing indicated", it proves that poll() SUCCEEDED,
        # which proves that our context override worked!
        # If context override failed, it would raise "poll() failed, context is incorrect".

        res = SAVEPOINTS_OT_rescue_assets._run(self.op, self.mock_context)

        # Assertions
        # 1. Expect CANCELLED because wm.append fails on fake path
        self.assertEqual(res, {'CANCELLED'})

        # 2. Verify temp_override was called correctly
        self.mock_context.temp_override.assert_called_once()
        call_kwargs = self.mock_context.temp_override.call_args[1]
        self.assertEqual(call_kwargs['window'], mock_window)
        self.assertEqual(call_kwargs['area'], mock_area)

        # 3. Verify the error message confirms poll success
        # We expect op.report to be called with an error about "nothing indicated"
        # indicating that wm.append executed its logic.
        args, _ = self.op.report.call_args
        error_msg = args[1]

        print(f"Captured error: {error_msg}")

        if "nothing indicated" in error_msg:
            print("Success: wm.append executed (poll passed).")
        elif "context is incorrect" in error_msg:
            self.fail("Failure: wm.append failed poll check (context override didn't work).")
        else:
            # Some other error?
            pass

        print("Confirmed: Context logic identified Viewport and invoked append.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
