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
    test_dir = ROOT / "test_missing_file"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting Missing File Handling Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "project.blend"

    try:
        # 1. Save initial project file
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        savepoints.register()

        # 3. Create a version
        print("Creating version v001...")
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="To be broken")

        # 4. Verify creation
        history_dir = test_dir / ".project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"
        if not snapshot_path.exists():
            raise RuntimeError("Setup failed: Snapshot file was not created.")

        # 5. Sabotage: Delete the snapshot file
        print("Sabotaging: Deleting snapshot file...")
        snapshot_path.unlink()

        # 6. Attempt Checkout
        print("Attempting Checkout on missing file...")
        bpy.context.scene.savepoints_settings.active_version_index = 0

        # We expect this operator to report an ERROR and return CANCELLED.
        # In scripting, this often raises a RuntimeError.
        try:
            res = bpy.ops.savepoints.checkout('EXEC_DEFAULT')
            # If it didn't raise, check if it returned CANCELLED (though usually it raises)
            if 'CANCELLED' in res:
                print("Checkout was correctly CANCELLED (via return value).")
            else:
                raise RuntimeError(f"Checkout should have been CANCELLED but returned: {res}")
        except RuntimeError as e:
            # Check if the error message is what we expect
            if "File not found" in str(e):
                print("Checkout was correctly CANCELLED (via RuntimeError).")
            else:
                raise e

        # 7. Verify we are NOT in snapshot mode (file path should still be original or safe)
        # Because the open_mainfile failed, we should still be at project.blend (or whatever state we were before)
        current_path = Path(bpy.data.filepath)
        print(f"Current filepath after failure: {current_path}")

        if current_path != blend_file_path:
            raise RuntimeError(f"Safety check failed: Filepath changed to {current_path}")

        print("Missing File Handling Test: PASSED")

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
