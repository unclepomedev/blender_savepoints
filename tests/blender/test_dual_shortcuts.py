import sys
import unittest
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
import savepoints.operators
from savepoints_test_case import SavePointsTestCase


# Mock classes
class MockSettings:
    def __init__(self):
        self.show_save_dialog = True


class MockScene:
    def __init__(self):
        self.savepoints_settings = MockSettings()


class MockWindowManager:
    def invoke_props_dialog(self, op):
        return {'RUNNING_MODAL'}


class MockContext:
    def __init__(self):
        self.scene = MockScene()
        self.window_manager = MockWindowManager()


class MockOp:
    def __init__(self):
        self.force_quick = False
        self.note = ""
        self.execute_called = False

    def execute(self, context):
        self.execute_called = True
        return {'FINISHED'}


class TestDualShortcuts(SavePointsTestCase):
    def test_dual_shortcuts(self):
        print("Starting Dual Shortcuts Unit Test (Unbound Method Verification)...")

        # Get the invoke method directly from the class
        OpClass = savepoints.operators.SAVEPOINTS_OT_commit
        invoke_func = OpClass.invoke

        print("\n--- Test 1: Dialog logic (force_quick=False) ---")
        op = MockOp()
        op.force_quick = False
        op.note = "Original Note"

        context = MockContext()
        context.scene.savepoints_settings.show_save_dialog = True

        # Call invoke manually
        res = invoke_func(op, context, None)
        print(f"Result: {res}")

        if res != {'RUNNING_MODAL'}:
            self.fail(f"Expected RUNNING_MODAL, got {res}")

        if op.execute_called:
            self.fail("execute() called unexpectedly")

        print("Test 1 Passed.")

        print("\n--- Test 2: Force Quick Logic (force_quick=True) ---")
        op = MockOp()
        op.force_quick = True
        op.note = "Should Be Cleared"

        context = MockContext()
        context.scene.savepoints_settings.show_save_dialog = True

        res = invoke_func(op, context, None)
        print(f"Result: {res}")

        if res != {'FINISHED'}:
            self.fail(f"Expected FINISHED, got {res}")

        if not op.execute_called:
            self.fail("execute() was not called")

        if op.note != "":
            self.fail(f"Note should be cleared, got '{op.note}'")

        print("Test 2 Passed.")

        print("\n--- Test 3: Dialog Disabled Logic ---")
        op = MockOp()
        op.force_quick = False
        op.note = "Should Be Cleared"

        context = MockContext()
        context.scene.savepoints_settings.show_save_dialog = False

        res = invoke_func(op, context, None)
        print(f"Result: {res}")

        if res != {'FINISHED'}:
            self.fail(f"Expected FINISHED, got {res}")

        if op.note != "":
            self.fail(f"Note should be cleared (standard quick save), got '{op.note}'")

        print("Test 3 Passed.")
        print("\nALL TESTS PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
