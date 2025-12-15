import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints.operators


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


def main():
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
        raise RuntimeError(f"Expected RUNNING_MODAL, got {res}")

    if op.execute_called:
        raise RuntimeError("execute() called unexpectedly")

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
        raise RuntimeError(f"Expected FINISHED, got {res}")

    if not op.execute_called:
        raise RuntimeError("execute() was not called")

    if op.note != "":
        raise RuntimeError(f"Note should be cleared, got '{op.note}'")

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
        raise RuntimeError(f"Expected FINISHED, got {res}")

    if op.note != "":
        raise RuntimeError(f"Note should be cleared (standard quick save), got '{op.note}'")

    print("Test 3 Passed.")
    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()
