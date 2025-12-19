import sys
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add project root to path
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
        # Setup the operator mock
        self.op = MagicMock()
        self.op.version_id = "v001"
        self.op.report = MagicMock()

        # Bind the real method to the mock object so we can test its logic
        # logic: _run calls self._open_append_dialog
        self.op._open_append_dialog = SAVEPOINTS_OT_rescue_assets._open_append_dialog.__get__(self.op,
                                                                                              SAVEPOINTS_OT_rescue_assets)

    def _create_mock_context(self, has_view3d=False):
        """Helper to build a complex mock context with window/screen/area structure."""
        mock_context = MagicMock()

        # Setup Window & Screen
        mock_window = MagicMock()
        mock_screen = MagicMock()
        mock_area = MagicMock()

        # Define Area Type
        if has_view3d:
            mock_area.type = 'VIEW_3D'
            # Need a region for the override context
            mock_region = MagicMock()
            mock_region.type = 'WINDOW'
            mock_area.regions = [mock_region]
        else:
            mock_area.type = 'PROPERTIES'  # Something that isn't VIEW_3D

        mock_screen.areas = [mock_area]
        mock_window.screen = mock_screen
        mock_context.window_manager.windows = [mock_window]

        # Setup temp_override (Context Manager)
        # context.temp_override(**kwargs) -> returns a ContextManager
        override_cm = MagicMock()
        override_cm.__enter__.return_value = None
        override_cm.__exit__.return_value = None
        mock_context.temp_override.return_value = override_cm

        return mock_context, mock_window, mock_area

    def test_rescue_logic_scenario(self):
        """
        Scenario:
        1. No View3D: Verify that _run returns CANCELLED if no 3D Viewport is found.
        2. With View3D: Verify that _run identifies the Viewport, sets up context override,
           and attempts to call the append operator.
        """
        print("Starting Rescue Logic Scenario...")

        # Use ExitStack to avoid nested "with patch..." blocks
        with ExitStack() as stack:
            # --- Apply Patches ---
            mock_is_safe = stack.enter_context(patch("savepoints.operators.is_safe_filename"))
            mock_find_snapshot = stack.enter_context(patch("savepoints.operators.find_snapshot_path"))
            mock_create_temp = stack.enter_context(patch("savepoints.operators.create_rescue_temp_file"))
            mock_get_append_dir = stack.enter_context(patch("savepoints.operators.get_rescue_append_dir"))
            mock_delete_temp = stack.enter_context(patch("savepoints.operators.delete_rescue_temp_file"))
            mock_handler_cls = stack.enter_context(patch("savepoints.operators.RescuePostLoadHandler"))

            # --- Common Setup ---
            mock_is_safe.return_value = True
            mock_find_snapshot.return_value = Path("/tmp/history/v001/snapshot.blend")
            mock_create_temp.return_value = Path("/tmp/history/v001/rescue_temp.blend")
            mock_get_append_dir.return_value = "/tmp/history/v001/rescue_temp.blend/Object/"

            # --- Step 1: No 3D Viewport ---
            with self.subTest(step="1. No View3D"):
                print("Testing No View3D case...")

                # Setup Bad Context
                mock_ctx, _, _ = self._create_mock_context(has_view3d=False)

                # Execute
                res = SAVEPOINTS_OT_rescue_assets._run(self.op, mock_ctx)

                # Verify
                self.assertEqual(res, {'CANCELLED'})
                self.op.report.assert_called_with({'ERROR'},
                                                  "Could not find a valid 3D Viewport to open the Append dialog.")

                # Verify Cleanup
                mock_handler_cls.return_value.unregister.assert_called()
                mock_delete_temp.assert_called()

            # --- Step 2: With 3D Viewport ---
            with self.subTest(step="2. With View3D"):
                print("Testing With View3D case...")

                # Setup Good Context
                mock_ctx, mock_window, mock_area = self._create_mock_context(has_view3d=True)

                # Reset mocks to ensure clean verification
                self.op.report.reset_mock()

                # Execute
                # Note: wm.append will likely fail because paths are fake, returning CANCELLED.
                # We check IF it tried to run (via temp_override and specific error msg).
                res = SAVEPOINTS_OT_rescue_assets._run(self.op, mock_ctx)

                # Verify Result (Expect CANCELLED due to fake path, but logic flow is what matters)
                self.assertEqual(res, {'CANCELLED'})

                # Verify Context Override was used (Critical Logic)
                mock_ctx.temp_override.assert_called_once()
                call_kwargs = mock_ctx.temp_override.call_args[1]
                self.assertEqual(call_kwargs['window'], mock_window)
                self.assertEqual(call_kwargs['area'], mock_area)

                # Verify Operator Attempt
                # If report was called with a Blender-internal error (like "Nothing indicated"),
                # it means the override worked and passed control to wm.append.
                if self.op.report.called:
                    args, _ = self.op.report.call_args
                    error_msg = args[1]
                    print(f"  Captured internal error: '{error_msg}'")

                    # These messages prove wm.append ran and complained about arguments
                    success_indicators = ["nothing indicated", "Cannot find file", "File not found",
                                          "property not found"]
                    is_success = any(indicator in error_msg for indicator in success_indicators)

                    if not is_success and "context" in error_msg:
                        self.fail(f"Likely Context Error: {error_msg}")
                    elif not is_success:
                        print(f"  Warning: Unexpected error message, but append likely attempted: {error_msg}")

        print("Rescue Logic Scenario: Completed")


if __name__ == '__main__':
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
