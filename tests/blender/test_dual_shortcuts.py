import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

# Add project root to path so we can import the addon modules
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import savepoints.operators
from savepoints_test_case import SavePointsTestCase


class TestDualShortcuts(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        # Target the specific operator class and its invoke method directly
        self.OpClass = savepoints.operators.SAVEPOINTS_OT_commit
        self.invoke_func = self.OpClass.invoke

    def _create_mock_context(self, show_dialog=True):
        """Helper to simulate Blender's Context behavior using MagicMock."""
        context = MagicMock()

        # Mock access to savepoints_settings
        context.scene.savepoints_settings.show_save_dialog = show_dialog

        # Set the return value for the window manager dialog method
        # logic: if a dialog opens, it returns {'RUNNING_MODAL'}
        context.window_manager.invoke_props_dialog.return_value = {'RUNNING_MODAL'}

        return context

    def _create_mock_op(self, force_quick=False, note=""):
        """Helper to mock the operator instance (self)."""
        op = MagicMock()
        op.force_quick = force_quick
        op.note = note

        # If execute is called, it should return {'FINISHED'}
        op.execute.return_value = {'FINISHED'}

        return op

    def test_dual_shortcuts_logic(self):
        """
        Unit Test:
        Validates the branching logic inside the Operator's invoke method.
        Uses MagicMock to simulate Blender's context and UI manager interactions
        without needing a full UI environment.
        """
        print("Starting Dual Shortcuts Logic Test...")

        # --- Case 1: Dialog should behave normally (Show Dialog) ---
        with self.subTest(case="1. Dialog Enabled (force_quick=False)"):
            context = self._create_mock_context(show_dialog=True)
            op = self._create_mock_op(force_quick=False, note="Original")

            # Execute invoke
            res = self.invoke_func(op, context, None)

            # Verification:
            # It should attempt to open a dialog (RUNNING_MODAL)
            # execute() should NOT be called yet.
            self.assertEqual(res, {'RUNNING_MODAL'})
            context.window_manager.invoke_props_dialog.assert_called_once_with(op)
            op.execute.assert_not_called()

        # --- Case 2: Force Quick (Skip Dialog) ---
        with self.subTest(case="2. Force Quick (force_quick=True)"):
            context = self._create_mock_context(show_dialog=True)
            op = self._create_mock_op(force_quick=True, note="Should Be Cleared")

            # Execute invoke
            res = self.invoke_func(op, context, None)

            # Verification:
            # It should bypass the dialog, clear the note, and call execute immediately.
            self.assertEqual(res, {'FINISHED'})
            self.assertEqual(op.note, "")  # Note should be cleared for quick save
            op.execute.assert_called_once_with(context)
            context.window_manager.invoke_props_dialog.assert_not_called()

        # --- Case 3: Dialog Disabled in Settings (Skip Dialog) ---
        with self.subTest(case="3. Dialog Disabled Setting"):
            context = self._create_mock_context(show_dialog=False)
            op = self._create_mock_op(force_quick=False, note="Should Be Cleared")

            # Execute invoke
            res = self.invoke_func(op, context, None)

            # Verification:
            # Even if force_quick is False, if the global setting disables the dialog,
            # it should behave like a quick save.
            self.assertEqual(res, {'FINISHED'})
            self.assertEqual(op.note, "")
            op.execute.assert_called_once_with(context)
            context.window_manager.invoke_props_dialog.assert_not_called()

        print("Dual Shortcuts Logic Test: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
