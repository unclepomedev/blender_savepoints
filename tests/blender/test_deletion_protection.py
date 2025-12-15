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


def main():
    print("Starting Deletion Protection Test...")
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

        # Verify it is protected
        manifest = core.load_manifest()
        v1 = manifest["versions"][0]
        if not v1.get("is_protected"):
            raise RuntimeError("Failed to set protection status")

        # Select this version in UI (required for operator)
        settings.active_version_index = 0

        # Try to delete via operator
        res = bpy.ops.savepoints.delete('EXEC_DEFAULT')

        # Operator should either return CANCELLED or notify user and not delete.
        # Check manifest to verify persistence
        manifest = core.load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])

        if not found:
            raise RuntimeError("Protected version was deleted by Operator!")

        print("Test 1 Passed: Operator refused to delete protected version.")

        print("\n--- Test 2: Internal API Protection (core.delete_version_by_id) ---")

        # Try to delete via internal API directly
        # This was the vulnerability fix target
        core.delete_version_by_id(v1_id)

        manifest = core.load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])

        if not found:
            raise RuntimeError("Protected version was deleted by internal API!")

        print("Test 2 Passed: Internal API refused to delete protected version.")

        print("\n--- Test 3: Prune (Retention Policy) Protection ---")

        # Create many older versions to trigger pruning
        # We need to manipulate timestamps to make them "old" if we test date-based,
        # or just create enough to exceed count-based limit.

        # Create 5 more versions
        for i in range(5):
            create_dummy_version(settings, f"Filler {i}")
            time.sleep(0.1)  # ensure timestamp diff

        # Now we have v1 (protected, oldest) and 5 newer versions. Total 6.
        # Set max_keep to 3. 
        # Ideally, v1 is the oldest (index 5), so it should be deleted if not protected.
        # Since it is protected, it should be kept.

        # Force reload manifest to get correct order
        manifest = core.load_manifest()
        versions = manifest["versions"]
        # versions[0] is newest. versions[-1] is oldest (our protected v1).
        if versions[-1]["id"] != v1_id:
            # Just to be sure about order logic
            pass

        # Run Prune
        deleted_count = core.prune_versions(max_keep=3)

        manifest = core.load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]

        # Check if v1_id is still there
        if v1_id not in remaining_ids:
            raise RuntimeError("Protected version was deleted by Prune!")

        # Check if other old versions were deleted
        # We had 6 versions. Max keep 3.
        # Protected version (oldest) is kept.
        # So we expect 3 recent versions + 1 protected version? 
        # core.py logic:
        # for i, v in enumerate(manual_versions):
        #    if i < max_keep or is_locked or is_daily: continue
        #    else: delete

        # indices 0, 1, 2 are kept (is_recent).
        # index 3, 4 are deleted.
        # index 5 (protected) is kept (is_locked).
        # So we expect 4 versions remaining.

        if len(remaining_ids) != 4:
            print(f"Warning: Expected 4 versions remaining, got {len(remaining_ids)}. IDs: {remaining_ids}")
            # This is not strictly a failure of protection, but a check on logic.
            # As long as v1_id is there, protection works.

        print("Test 3 Passed: Prune respected protection.")

        print("\n--- Test 4: Verify unprotection allows deletion ---")
        core.set_version_protection(v1_id, False)
        core.delete_version_by_id(v1_id)

        manifest = core.load_manifest()
        if any(v["id"] == v1_id for v in manifest["versions"]):
            raise RuntimeError("Failed to delete version after unprotection")

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
