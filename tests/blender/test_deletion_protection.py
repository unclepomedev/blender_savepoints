import shutil
import sys
import time
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints import core


def setup_test_env():
    test_dir = ROOT / "test_deletion_protection_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def create_dummy_version(settings, note="Dummy"):
    # Create a version via operator
    bpy.ops.savepoints.commit('EXEC_DEFAULT', note=note)
    manifest = core.load_manifest()
    return manifest["versions"][0]


def set_version_timestamp(version_id, timestamp_dt):
    """Directly modify manifest to set a specific timestamp for a version."""
    manifest = core.load_manifest()
    found = False
    for v in manifest["versions"]:
        if v["id"] == version_id:
            v["timestamp"] = timestamp_dt.strftime("%Y-%m-%d %H:%M:%S")
            found = True
            break
    if found:
        core.save_manifest(manifest)


def main():
    print("Starting Deletion Protection Test (Extended)...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_protection.blend"

    try:
        # 1. Setup
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))
        savepoints.register()
        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Manual Deletion Protection (Operator) ---")

        # Create a version
        v1 = create_dummy_version(settings, "Protected Version")
        v1_id = v1["id"]

        # Enable protection
        core.set_version_protection(v1_id, True)

        # Try to delete via operator
        settings.active_version_index = 0
        bpy.ops.savepoints.delete('EXEC_DEFAULT')

        # Check manifest
        manifest = core.load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])
        if not found:
            raise RuntimeError("Protected version was deleted by Operator!")
        print("Test 1 Passed.")

        print("\n--- Test 2: Internal API Protection ---")
        core.delete_version_by_id(v1_id)
        manifest = core.load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])
        if not found:
            raise RuntimeError("Protected version was deleted by internal API!")
        print("Test 2 Passed.")

        print("\n--- Test 3: Prune Protection (Basic) ---")
        # Create filler versions
        for i in range(3):
            create_dummy_version(settings, f"Filler {i}")
            time.sleep(0.1)

        # v1 (Protected) is now index 3 (Oldest)
        # Prune max_keep=1
        core.prune_versions(max_keep=1)

        manifest = core.load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]
        if v1_id not in remaining_ids:
            raise RuntimeError("Protected version was deleted by Prune!")
        print("Test 3 Passed.")

        print("\n--- Test 4: Unprotect and Delete ---")
        # Create a fresh version for this test since previous tests might have cleared the manifest
        v5 = create_dummy_version(settings, "Version to Unprotect")
        v5_id = v5["id"]

        # Ensure it starts protected
        core.set_version_protection(v5_id, True)

        # Unprotect
        core.set_version_protection(v5_id, False)

        # Delete
        core.delete_version_by_id(v5_id)

        # Verify deletion
        manifest = core.load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]
        if v5_id in remaining_ids:
            raise RuntimeError("Unprotected version was NOT deleted!")
        print("Test 4 Passed.")

        print("\nALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
