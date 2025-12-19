import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, PropertyMock

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Import the actual operator class to access its methods directly
import savepoints.operators
from savepoints_test_case import SavePointsTestCase


class TestNoteAssignment(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        # Add a cube for successful note generation context
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "MyCube"

        # Prepare the real invoke function we want to test
        # We access the unbound method directly from the class
        self.invoke_func = savepoints.operators.SAVEPOINTS_OT_commit.invoke

    def _create_mock_context(self, show_dialog=False, active_object=None, simulate_error=False):
        """Helper to create a MagicMock that behaves like bpy.context"""
        mock_ctx = MagicMock()

        # Mock Settings
        mock_ctx.scene.savepoints_settings.show_save_dialog = show_dialog

        # Mock WindowManager
        # invoke_props_dialog should return 'RUNNING_MODAL' when called
        mock_ctx.window_manager.invoke_props_dialog.return_value = {'RUNNING_MODAL'}

        # Mock Active Object logic
        if simulate_error:
            # Setup a property that raises RuntimeError when accessed
            type(mock_ctx).active_object = PropertyMock(side_effect=RuntimeError("Simulated Context Error"))
        else:
            # Normal behavior
            if active_object:
                mock_ctx.active_object = active_object
            else:
                # Fallback to real context object if not explicitly provided,
                # or just Mock it. Here we use the real one for the happy path.
                mock_ctx.active_object = bpy.context.active_object

        return mock_ctx

    def _create_mock_op(self, force_quick=False, note=""):
        """Helper to create a Mock Operator instance"""
        op = MagicMock()
        op.force_quick = force_quick
        op.note = note
        op.execute.return_value = {'FINISHED'}

        # Important: Attach the real _get_default_note logic if it's called internally via self
        # Or, rely on the fact that invoke calls savepoints.operators.generate_default_note directly.
        # Looking at your previous code, generate_default_note is imported.
        # If the operator calls `self.report`, the mock handles it automatically.

        return op

    def test_invoke_force_quick(self):
        """Case: Force Quick = True -> FINISHED, Note auto-filled"""
        mock_ctx = self._create_mock_context(show_dialog=False)
        op = self._create_mock_op(force_quick=True)

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'FINISHED'})
        self.assertEqual(op.note, "Object: MyCube")
        mock_ctx.window_manager.invoke_props_dialog.assert_not_called()

    def test_invoke_standard_quick(self):
        """Case: Force Quick = False but Dialog Disabled -> FINISHED"""
        mock_ctx = self._create_mock_context(show_dialog=False)
        op = self._create_mock_op(force_quick=False)

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'FINISHED'})
        self.assertEqual(op.note, "Object: MyCube")
        mock_ctx.window_manager.invoke_props_dialog.assert_not_called()

    def test_invoke_dialog_path(self):
        """Case: Dialog Enabled -> RUNNING_MODAL"""
        mock_ctx = self._create_mock_context(show_dialog=True)
        op = self._create_mock_op(force_quick=False)

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'RUNNING_MODAL'})
        self.assertEqual(op.note, "Object: MyCube")
        # Verify dialog was opened
        mock_ctx.window_manager.invoke_props_dialog.assert_called_once_with(op)

    def test_invoke_explicit_note_preserved(self):
        """Case: Note already set -> Should not be overwritten"""
        mock_ctx = self._create_mock_context(show_dialog=False)
        op = self._create_mock_op(force_quick=True, note="Explicit Note")

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'FINISHED'})
        self.assertEqual(op.note, "Explicit Note")

    def test_invoke_no_active_object(self):
        """Case: No active object -> 'No Active Object'"""
        # Deselect everything to simulate no active object in real context
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = None

        mock_ctx = self._create_mock_context(show_dialog=False, active_object=None)
        # Force None just to be sure
        type(mock_ctx).active_object = PropertyMock(return_value=None)

        op = self._create_mock_op(force_quick=True)

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'FINISHED'})
        self.assertEqual(op.note, "No Active Object")

    def test_invoke_exception_handling(self):
        """Case: Context Error -> Graceful failure (Empty Note)"""
        mock_ctx = self._create_mock_context(show_dialog=False, simulate_error=True)
        op = self._create_mock_op(force_quick=True)

        res = self.invoke_func(op, mock_ctx, None)

        self.assertEqual(res, {'FINISHED'})
        self.assertEqual(op.note, "")


if __name__ == '__main__':
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
