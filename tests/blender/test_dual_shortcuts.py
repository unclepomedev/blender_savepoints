import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add project root to path
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
        self.OpClass = savepoints.operators.SAVEPOINTS_OT_commit
        self.invoke_func = self.OpClass.invoke

    def _create_mock_context(self, show_dialog=True):
        """Helper to simulate Blender's Context behavior using MagicMock."""
        context = MagicMock()
        context.scene.savepoints_settings.show_save_dialog = show_dialog
        context.window_manager.invoke_props_dialog.return_value = {'RUNNING_MODAL'}
        return context

    def _create_mock_op(self, force_quick=False, note=""):
        """Helper to mock the operator instance (self)."""
        op = MagicMock()
        op.force_quick = force_quick
        op.note = note
        op.execute.return_value = {'FINISHED'}
        return op

    def test_dual_shortcuts_logic(self):
        """
        Unit Test:
        Validates the branching logic inside the Operator's invoke method.
        Mocks 'generate_default_note' to ensure predictable behavior regardless of
        actual Blender context.
        """
        print("Starting Dual Shortcuts Logic Test...")

        # Mock 'generate_default_note' within savepoints.operators module
        # We force it to return "Fixed Auto Note" so we can verify the assignment logic.
        with patch('savepoints.operators.generate_default_note') as mock_gen_note:
            mock_gen_note.return_value = "Fixed Auto Note"

            # --- Case 1: Dialog Enabled (force_quick=False) ---
            with self.subTest(case="1. Dialog Enabled"):
                context = self._create_mock_context(show_dialog=True)
                # Pass an empty note so the logic triggers default generation
                op = self._create_mock_op(force_quick=False, note="")

                res = self.invoke_func(op, context, None)

                # Verification:
                # 1. Logic should assign default note.
                # 2. Logic should open dialog.
                self.assertEqual(res, {'RUNNING_MODAL'})
                self.assertEqual(op.note, "Fixed Auto Note")
                context.window_manager.invoke_props_dialog.assert_called_once_with(op)
                op.execute.assert_not_called()

            # --- Case 2: Force Quick (force_quick=True) ---
            with self.subTest(case="2. Force Quick"):
                context = self._create_mock_context(show_dialog=True)
                op = self._create_mock_op(force_quick=True, note="")

                res = self.invoke_func(op, context, None)

                # Verification:
                # 1. Logic should assign default note (even for quick save).
                # 2. Logic should SKIP dialog and execute immediately.
                self.assertEqual(res, {'FINISHED'})
                self.assertEqual(op.note, "Fixed Auto Note")
                op.execute.assert_called_once_with(context)
                context.window_manager.invoke_props_dialog.assert_not_called()

            # --- Case 3: Dialog Disabled Setting ---
            with self.subTest(case="3. Dialog Disabled Setting"):
                context = self._create_mock_context(show_dialog=False)
                op = self._create_mock_op(force_quick=False, note="")

                res = self.invoke_func(op, context, None)

                # Verification:
                # 1. Logic should assign default note.
                # 2. Logic should SKIP dialog because setting is False.
                self.assertEqual(res, {'FINISHED'})
                self.assertEqual(op.note, "Fixed Auto Note")
                op.execute.assert_called_once_with(context)
                context.window_manager.invoke_props_dialog.assert_not_called()

            # --- Case 4: Manual Note Provided (Should NOT Overwrite) ---
            with self.subTest(case="4. Manual Note Exists"):
                context = self._create_mock_context(show_dialog=True)
                # If operator already has a note (e.g. passed from redo panel or script)
                op = self._create_mock_op(force_quick=False, note="User Input")

                res = self.invoke_func(op, context, None)

                # Verification:
                # The existing note "User Input" should NOT be replaced by "Fixed Auto Note"
                self.assertEqual(res, {'RUNNING_MODAL'})
                self.assertEqual(op.note, "User Input")

        print("Dual Shortcuts Logic Test: Completed")


if __name__ == "__main__":
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
