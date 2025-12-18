import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402

from savepoints.services.storage import load_manifest
from savepoints.services.versioning import set_version_protection


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
    manifest = load_manifest()
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

        print("\n--- Test 4: Protected Versions Ignored by Prune (Quota Exclusion) ---")
        # Reset
        settings.use_limit_versions = False
        settings.max_versions_to_keep = 2

        # Create v7, v8.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v7")
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v8")

        # Lock v8 (the most recent one)
        set_version_protection("v008", True)

        # We have: v8(L), v7.
        # Max Keep = 2.
        settings.use_limit_versions = True

        # Create v9.
        # List: v9, v8(L), v7.
        # Unlocked: v9, v7. (Count = 2).
        # Locked: v8.
        # Result should be: v9, v8(L), v7. (All kept).
        # Note: If v8 counted towards limit, then v7 would be the 3rd item and pruned.

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v9")

        ids = get_version_ids()
        print(f"IDs after v9: {ids}")

        if "v007" not in ids:
            raise RuntimeError("v007 should be kept because v008(Locked) does not count towards quota.")

        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions (v9, v8L, v7), got {len(ids)}")

        # Create v10.
        # List: v10, v9, v8(L), v7.
        # Unlocked: v10, v9, v7. (Count = 3).
        # Max = 2.
        # Oldest unlocked is v7. Should be pruned.
        # Result: v10, v9, v8(L).

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v10")

        ids = get_version_ids()
        print(f"IDs after v10: {ids}")

        if "v007" in ids:
            raise RuntimeError("v007 should be pruned now.")

        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions (v10, v9, v8L), got {len(ids)}")

        print("Test 4 Passed.")

        print("\n--- Test 5: Unprotect to Prune ---")
        # Current State from Test 4: v10, v9, v8(L). Max=2.
        # Unlocked: v10, v9 (Count=2). Locked: v8.
        # All kept.

        ids = get_version_ids()
        expected_ids = ["v010", "v009", "v008"]
        if ids != expected_ids:
            # Just in case ordering is different or something failed before
            print(f"Warning: Starting state for Test 5 unexpected: {ids}")

        # Now unlock v8.
        # List: v10, v9, v8(Unlocked).
        # Unlocked Count = 3. Max = 2.
        # Should prune oldest unlocked -> v8.
        # Note: Simply toggling protection does not trigger prune. We must trigger it via commit or something?
        # Actually, prune_versions is called after commit.
        # If we just change metadata, prune isn't called automatically unless we do it manually or commit again.

        set_version_protection("v008", False)

        # Manually trigger prune for test purpose, or commit new version.
        # Let's commit v11 to trigger prune.
        # If we didn't prune v8 yet, list is: v11, v10, v9, v8.
        # Unlocked count = 4. Max = 2.
        # Should keep v11, v10. Prune v9, v8.

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v11")

        ids = get_version_ids()
        print(f"IDs after v11: {ids}")

        # Expected: v11, v10.
        if "v008" in ids:
            raise RuntimeError("v008 (Unlocked) should be pruned")
        if "v009" in ids:
            raise RuntimeError("v009 (Old Unlocked) should be pruned")
        if "v011" not in ids:
            raise RuntimeError("v011 (Newest) should be kept")
        if "v010" not in ids:
            raise RuntimeError("v010 (2nd Newest) should be kept")

        print("Test 5 Passed.")

        print("\n--- Test 6: Autosave Lock Guard ---")
        # Ensure autosave exists
        from savepoints.operators import create_snapshot
        create_snapshot(bpy.context, "autosave", "Auto Save", skip_thumbnail=True)

        # Attempt to lock autosave
        res = bpy.ops.savepoints.toggle_protection('EXEC_DEFAULT', version_id="autosave")

        # Verify in manifest that it is NOT protected
        manifest = load_manifest()
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
