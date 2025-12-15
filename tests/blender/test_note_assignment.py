import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints.operators


class MockWindowManager:
    def __init__(self):
        self.invoke_props_dialog_called = False

    def invoke_props_dialog(self, operator, width=300):
        self.invoke_props_dialog_called = True
        return {'RUNNING_MODAL'}


class MockContext:
    def __init__(self, real_context):
        self._real_context = real_context
        self.window_manager = MockWindowManager()

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


class TestNoteAssignment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            savepoints.register()
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            savepoints.unregister()
        except Exception:
            pass

    def setUp(self):
        # Reset scene
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "MyCube"

        # Reset settings
        if hasattr(bpy.context.scene, "savepoints_settings"):
            bpy.context.scene.savepoints_settings.show_save_dialog = False

    def test_invoke_force_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = True

        res = op.invoke(bpy.context, None)

        self.assertEqual(op.note, "Object: MyCube")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_standard_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = False
        op = MockOperator()
        op.force_quick = False

        res = op.invoke(bpy.context, None)

        self.assertEqual(op.note, "")
        self.assertEqual(res, {'FINISHED'})

    def test_invoke_dialog_on_force_quick(self):
        bpy.context.scene.savepoints_settings.show_save_dialog = True
        op = MockOperator()
        op.force_quick = True

        res = op.invoke(bpy.context, None)

        self.assertEqual(op.note, "Object: MyCube")
        self.assertEqual(res, {'FINISHED'})


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
