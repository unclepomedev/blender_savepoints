import datetime
import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints import core


def setup_test_env():
    test_dir = ROOT / "test_retention_policy_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def get_version_ids():
    manifest = core.load_manifest()
    return [v["id"] for v in manifest.get("versions", [])]


def main():
    print("Starting Retention Policy Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_retention.blend"

    try:
        # 1. Setup
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))
        savepoints.register()
        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Basic Limit (Max 3) ---")
        settings.use_limit_versions = True
        settings.max_versions_to_keep = 3

        # Create 3 versions
        for i in range(3):
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"v{i + 1}")

        ids = get_version_ids()
        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions, got {len(ids)}")

        # Create 4th -> Should delete v001 (Oldest)
        # Note: In our list, v003 is Newest (index 0), v001 is Oldest (index 2)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v4")

        ids = get_version_ids()
        print(f"IDs: {ids}")
        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions after pruning, got {len(ids)}")

        if "v001" in ids:
            raise RuntimeError("v001 should have been pruned")
        if "v004" not in ids:
            raise RuntimeError("v004 should be present")

        print("Test 1 Passed.")

        print("\n--- Test 2: Disable Limit ---")
        settings.use_limit_versions = False

        # Create 5th -> Should keep all (3 + 1 = 4)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v5")

        ids = get_version_ids()
        if len(ids) != 4:
            raise RuntimeError(f"Expected 4 versions, got {len(ids)}")

        print("Test 2 Passed.")

        print("\n--- Test 3: Re-enable Limit (Immediate Prune?) ---")
        # Creating a new version triggers prune. Just enabling the property doesn't trigger it immediately 
        # unless we call an operator or save.

        settings.use_limit_versions = True
        settings.max_versions_to_keep = 2

        # Current: 4 versions [v5, v4, v3, v2]
        # Create v6 -> Total 5. Max 2. Should prune v2, v3, v4?
        # Expect remaining: v6, v5.

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v6")

        ids = get_version_ids()
        print(f"IDs: {ids}")
        if len(ids) != 2:
            raise RuntimeError(f"Expected 2 versions, got {len(ids)}")

        expected = ["v006", "v005"]
        if ids != expected:
            raise RuntimeError(f"Mismatch. Expected {expected}, got {ids}")

        print("Test 3 Passed.")

        print("\n--- Test 4: Protected Versions Ignored by Prune ---")
        # Current: v6, v5.
        # Protect v5
        bpy.ops.savepoints.toggle_protection(version_id="v005")

        # Set Max 1
        settings.max_versions_to_keep = 1

        # Create v7.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v7")

        ids = get_version_ids()
        print(f"IDs: {ids}")

        # Should have v7 (New), v5 (Protected)
        # v6 should be gone.

        if "v006" in ids:
            raise RuntimeError("v006 should have been pruned")
        if "v005" not in ids:
            raise RuntimeError("v005 (Protected) should be kept")
        if "v007" not in ids:
            raise RuntimeError("v007 (Newest) should be kept")

        print("Test 4 Passed.")

        print("\n--- Test 5: Unprotect to Prune ---")
        # Current: v7, v5
        # Set Max 1.
        # Create v8 -> [v8, v7, v5]
        # Keep 1 -> v8.
        # v7 (Unprotected) -> Delete.
        # v5 (Protected) -> Keep.

        # Let's create v8 first to clear v7.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v8")

        ids = get_version_ids()
        # Expect v8, v5
        if "v007" in ids:
            raise RuntimeError("v007 should be pruned")

        # Let's lock v8.
        bpy.ops.savepoints.toggle_protection(version_id="v008")

        # Current: v8(locked), v5(locked).
        # Max 1.
        # Create v9 -> [v9, v8, v5]
        # v9 (Recent) -> Keep.
        # v8 (Locked) -> Keep.
        # v5 (Locked) -> Keep.

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v9")
        ids = get_version_ids()
        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 locked/recent versions, got {len(ids)}")

        # Now unlock v5.
        bpy.ops.savepoints.toggle_protection(version_id="v005")

        # Create v10 -> [v10, v9, v8, v5]
        # Max 1.
        # v10 (Recent).
        # v9 (Unprotected? No we didn't lock v9). v9 is previous recent. Now it is old.
        # v8 (Locked).
        # v5 (Unprotected).

        # Result should be: v10, v8.
        # v9 deleted. v5 deleted.

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v10")

        ids = get_version_ids()
        print(f"IDs: {ids}")

        if "v005" in ids:
            raise RuntimeError("v005 (Unlocked) should be pruned")
        if "v009" in ids:
            raise RuntimeError("v009 (Old Unprotected) should be pruned")
        if "v008" not in ids:
            raise RuntimeError("v008 (Locked) should be kept")
        if "v010" not in ids:
            raise RuntimeError("v010 (Newest) should be kept")

        print("Test 5 Passed.")

        print("\n--- Test 6: Autosave Lock Guard ---")
        # Ensure autosave exists
        from savepoints.operators import create_snapshot
        create_snapshot(bpy.context, "autosave", "Auto Save", skip_thumbnail=True)

        # Attempt to lock autosave
        res = bpy.ops.savepoints.toggle_protection('EXEC_DEFAULT', version_id="autosave")

        # Verify in manifest that it is NOT protected
        manifest = core.load_manifest()
        autosave_entry = next((v for v in manifest["versions"] if v["id"] == "autosave"), None)

        if not autosave_entry:
            raise RuntimeError("Autosave missing for Test 6")

        if autosave_entry.get("is_protected", False):
            raise RuntimeError("Autosave was successfully protected (should be forbidden)")

        print("Test 6 Passed.")

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
