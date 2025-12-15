import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402


def setup_test_env():
    # Create a temporary directory for testing
    test_dir = ROOT / "test_no_auto_history"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting No Automatic History Creation Test...")
    test_dir = setup_test_env()

    # Paths
    project_path = test_dir / "project.blend"
    history_dir = test_dir / ".project_history"

    try:
        # 1. Save a new file
        print(f"Saving project to {project_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(project_path))

        print("Registering savepoints addon...")
        savepoints.register()

        # 2. Simulate loading the file (which triggers load_post handler)
        print("Simulating file load...")
        # Note: save_as_mainfile might not trigger load_post in background mode in the same way, 
        # but we can explicitly call the handler or reload the file.
        bpy.ops.wm.open_mainfile(filepath=str(project_path))

        # Verify history dir does NOT exist
        if history_dir.exists():
            raise RuntimeError(f"History directory created automatically! {history_dir}")

        print("History directory correctly missing.")

        # 3. Verify that calling sync_history_to_props manually also doesn't create it
        from savepoints import ui_utils
        ui_utils.sync_history_to_props(bpy.context)

        if history_dir.exists():
            raise RuntimeError(f"History directory created by sync_history_to_props! {history_dir}")

        print("History directory still missing after sync.")

        print("Test Passed!")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print("Cleaning up...")
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
