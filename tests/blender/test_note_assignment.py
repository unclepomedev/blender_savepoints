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

import savepoints.operators
from savepoints_test_case import SavePointsTestCase


class MockWindowManager:
    def __init__(self):
        self.invoke_props_dialog_called = False

    def invoke_props_dialog(self, operator, width=300):
        self.invoke_props_dialog_called = True
        return {'RUNNING_MODAL'}


class MockContext:
    def __init__(self, real_context, active_object_override=None, simulate_error=False, use_override=False):
        self._real_context = real_context
        self.window_manager = MockWindowManager()
        self._active_object_override = active_object_override
        self._simulate_error = simulate_error
        self._use_override = use_override

    @property
    def active_object(self):
        if self._simulate_error:
            raise RuntimeError("Simulated Context Error")
        if self._use_override:
            return self._active_object_override
        return getattr(self._real_context, "active_object", None)

    def __getattr__(self, name):
        return getattr(self._real_context, name)


class MockOperator:
    def __init__(self):
        self.note = ""
        self.force_quick = False

    def report(self, type, message):
        pass

    def execute(self, context):
        return {'FINISHED'}

    # Bind methods from the real class
    _get_default_note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note
    invoke = savepoints.operators.SAVEPOINTS_OT_commit.invoke


class TestNoteAssignment(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # Reset scene (SavePointsTestCase does read_homefile(use_empty=True) but let's just add the cube)
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "MyCube"

        # Reset settings
        if hasattr(bpy.context.scene, "savepoints_settings"):
            bpy.context.scene.savepoints_settings.show_save_dialog = False

    def test_invoke_force_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = True

        # Use MockContext even here to be safe, though not strictly needed for this path
        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "Object: MyCube")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_standard_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = False

        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "Object: MyCube")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_dialog_on_force_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = True
        op = MockOperator()
        op.force_quick = True

        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "Object: MyCube")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_dialog_path(self):
        """Test the path where dialog is shown (show_save_dialog=True, force_quick=False)"""
        bpy.context.scene.savepoints_settings.show_save_dialog = True
        op = MockOperator()
        op.force_quick = False

        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        # 1. Note should be pre-populated
        self.assertEqual(op.note, "Object: MyCube")

        # 2. Should return RUNNING_MODAL from invoke_props_dialog
        self.assertEqual(res, {'RUNNING_MODAL'})

        # 3. Verify invoke_props_dialog was called
        self.assertTrue(mock_ctx.window_manager.invoke_props_dialog_called)

    def test_invoke_force_quick_with_explicit_note(self):
        """Test that explicit note is preserved in force_quick mode"""
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = True
        op.note = "Explicit Note"

        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "Explicit Note")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_standard_quick_with_explicit_note(self):
        """Test that explicit note is preserved in standard quick mode"""
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = False
        op.note = "Explicit Note"

        mock_ctx = MockContext(bpy.context)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "Explicit Note")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_no_active_object(self):
        """Test correct handling when no object is active (should get empty note)"""
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = True

        # active_object = None
        mock_ctx = MockContext(bpy.context, active_object_override=None, use_override=True)
        res = op.invoke(mock_ctx, None)

        self.assertEqual(op.note, "")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_exception_handling(self):
        """Test robustness when context access raises exception"""
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = True

        # Simulate exception
        mock_ctx = MockContext(bpy.context, simulate_error=True)
        res = op.invoke(mock_ctx, None)

        # Should handle gracefully and set empty note
        self.assertEqual(op.note, "")
        self.assertEqual(res, {'FINISHED'})


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
