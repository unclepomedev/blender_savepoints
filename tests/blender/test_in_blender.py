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
    test_dir = ROOT / "test_e2e_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main() -> None:
    print("Starting E2E Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_project.blend"

    try:
        # 1. Save initial project file
        print(f"Saving initial project to {blend_file_path}")
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # 2. Register Addon
        print("Registering savepoints addon...")
        savepoints.register()

        # 3. Test Commit
        print("Testing Commit...")
        # Create some data to verify later
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "TestCube_v1"

        # EXEC_DEFAULT to bypass invoke_props_dialog
        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="First Version")
        if "FINISHED" not in res:
            raise RuntimeError(f"Commit failed with result: {res}")

        # Verify filesystem
        history_dir = test_dir / ".test_project_history"
        if not history_dir.exists():
            raise RuntimeError("History directory not created")

        manifest_path = history_dir / "manifest.json"
        if not manifest_path.exists():
            raise RuntimeError("Manifest not created")

        v001_dir = history_dir / "v001"
        if not v001_dir.exists():
            raise RuntimeError("Version v001 folder not created")

        snapshot_path = v001_dir / "snapshot.blend"
        if not snapshot_path.exists():
            raise RuntimeError("Snapshot file not created")

        print("Commit Verification: OK")

        # 4. Test Checkout
        print("Testing Checkout...")
        # Modify current scene so we know if we switched
        bpy.ops.mesh.primitive_uv_sphere_add()
        bpy.context.object.name = "TransientSphere"

        # Set active index to 0 (v001)
        bpy.context.scene.savepoints_settings.active_version_index = 0

        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            raise RuntimeError(f"Checkout failed with result: {res}")

        # Verify loaded file
        current_path = Path(bpy.data.filepath)
        if current_path.name != "snapshot.blend":
            raise RuntimeError(f"Checkout did not load snapshot.blend, current: {current_path}")

        # Verify content (should have TestCube_v1, but NOT TransientSphere)
        if "TestCube_v1" not in bpy.data.objects:
            raise RuntimeError("Snapshot does not contain TestCube_v1")
        if "TransientSphere" in bpy.data.objects:
            raise RuntimeError("Snapshot contains TransientSphere (should have been discarded)")

        # Verify Snapshot Mode
        from savepoints.utils import get_parent_path_from_snapshot
        parent_path_detected = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path_detected:
            raise RuntimeError("Snapshot Mode not detected (get_parent_path_from_snapshot returned None)")

        if Path(parent_path_detected) != blend_file_path:
            raise RuntimeError(f"Parent path mismatch: {parent_path_detected} vs {blend_file_path}")

        print("Checkout Verification: OK")

        # 5. Test Restore (Save as Parent)
        print("Testing Restore...")

        # Add something new in the snapshot to verify it gets saved to parent
        bpy.ops.mesh.primitive_cone_add()
        bpy.context.object.name = "RestoredCone"

        # EXEC_DEFAULT to bypass confirmation
        res = bpy.ops.savepoints.restore('EXEC_DEFAULT')
        if "FINISHED" not in res:
            raise RuntimeError(f"Restore failed with result: {res}")

        # Verify filepath is back to original
        current_path = Path(bpy.data.filepath)
        if current_path.name != "test_project.blend":
            raise RuntimeError(f"Restore did not switch back to original file, current: {current_path}")

        # Verify content
        if "RestoredCone" not in bpy.data.objects:
            raise RuntimeError("Restored file does not contain the new object added in snapshot")

        # Verify Backup
        backups = list(history_dir.glob("test_project.blend.*.bak"))
        if not backups:
            raise RuntimeError("Backup file was not created in history folder")

        print("Restore Verification: OK")

        print("ALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print("Cleaning up...")
        # Unregister might fail if register failed half-way, but try anyway
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
