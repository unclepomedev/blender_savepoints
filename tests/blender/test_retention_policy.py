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
    test_dir = ROOT / "test_retention_run"
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


def reset_history():
    history_dir = core.get_history_dir()
    if history_dir and Path(history_dir).exists():
        shutil.rmtree(history_dir)
    # Re-init manifest
    core.load_manifest()


def set_version_timestamp(version_id, days_ago, hour_offset=0):
    manifest = core.load_manifest()
    target_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    # Adjust hour to distinguish versions on the same day if needed
    # Fixed time 12:00:00 + offset
    target_date = target_date.replace(hour=12, minute=0, second=0) + datetime.timedelta(hours=hour_offset)

    ts_str = target_date.strftime("%Y-%m-%d %H:%M:%S")

    found = False
    for v in manifest["versions"]:
        if v["id"] == version_id:
            v["timestamp"] = ts_str
            found = True
            break

    if found:
        core.save_manifest(manifest)
    else:
        raise ValueError(f"Version {version_id} not found in manifest")


def main():
    print("Starting Retention Policy & Protection Tests...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_retention.blend"

    try:
        # 1. Setup
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))
        savepoints.register()

        scene = bpy.context.scene
        settings = scene.savepoints_settings

        # Enable Retention Policy
        settings.use_limit_versions = True
        settings.max_versions_to_keep = 3

        print("\n--- Test 1: Basic Pruning (Limit=3) ---")
        # Create 3 versions (v001, v002, v003)
        for i in range(3):
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"Ver {i + 1}")

        ids = get_version_ids()
        print(f"Current IDs: {ids}")
        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions, got {len(ids)}")

        # Create 4th version -> Should trigger pruning of v001
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Ver 4")

        ids = get_version_ids()
        print(f"IDs after pruning: {ids}")

        if "v001" in ids:
            raise RuntimeError("v001 should have been pruned")
        if len(ids) != 3:
            raise RuntimeError(f"Expected 3 versions after pruning, got {len(ids)}")
        if ids[0] != "v004":  # Newest first
            raise RuntimeError("Newest version should be v004")

        print("Test 1 Passed.")

        print("\n--- Test 2: Version Protection (Locking) ---")
        # Current: v004, v003, v002. Limit=3.
        # We want to protect v002 (the oldest).

        # Lock v002
        bpy.ops.savepoints.toggle_protection(version_id="v002")

        # Verify protection in manifest
        manifest = core.load_manifest()
        v002 = next(v for v in manifest["versions"] if v["id"] == "v002")
        if not v002.get("is_protected"):
            raise RuntimeError("v002 failed to lock")

        # Create v005. 
        # Logic: Excess=1. Candidates oldest->newest: v002, v003, v004.
        # v002 is protected. Next oldest is v003. v003 should be pruned.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Ver 5")

        ids = get_version_ids()
        print(f"IDs after protected prune: {ids}")

        if "v002" not in ids:
            raise RuntimeError("Protected version v002 was incorrectly pruned")
        if "v003" not in ids:
            raise RuntimeError("Recent version v003 should have been kept alongside Protected v002")

        # Remaining should be: v005, v004, v003, v002 (order in list: v005, v004, v003, v002)
        print("Test 2 Passed.")

        print("\n--- Test 3: Autosave Exclusion ---")
        # Current: v005, v004, v003, v002. Count=4. Limit=3.

        # Create Autosave manually (simulating the timer logic)
        from savepoints.operators import create_snapshot
        create_snapshot(bpy.context, "autosave", "Auto Save", skip_thumbnail=True)

        ids = get_version_ids()
        print(f"IDs with autosave: {ids}")
        # Should be v005, v004, v003, v002, autosave (or similar order)

        if "autosave" not in ids:
            raise RuntimeError("Autosave not created")

        # Create v006.
        # Manual versions count: 4 (v005, v004, v003, v002). Limit: 3.
        # Adding v006 makes manual count 5.
        # New Logic: Keep 3 recent (v006, v005, v004). Keep Protected (v002).
        # v003 should be pruned (it is 4th recent, not protected).
        # Autosave should persist.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Ver 6")

        ids = get_version_ids()
        print(f"IDs after v006: {ids}")

        if "autosave" not in ids:
            raise RuntimeError("Autosave was incorrectly pruned")
        if "v003" in ids:
            raise RuntimeError("v003 should have been pruned")
        if "v004" not in ids:
            raise RuntimeError("v004 should have been kept (Recent)")
        if "v002" not in ids:
            raise RuntimeError("Protected v002 should still remain")

        # Remaining manual: v006, v005, v004, v002. Total 4 manual.
        print("Test 3 Passed.")

        print("\n--- Test 4: Locked Limit Reached ---")
        # Current Manual: v006, v005, v004, v002.
        # Lock v005 and v006 as well.
        bpy.ops.savepoints.toggle_protection(version_id="v005")
        bpy.ops.savepoints.toggle_protection(version_id="v006")

        # Create v007.
        # Manual versions will be 4. Excess 1.
        # But all (v002, v005, v006) are protected.
        # Pruning should skip deletion.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Ver 7")

        ids = get_version_ids()
        print(f"IDs after saturated lock: {ids}")

        manual_ids = [i for i in ids if i != "autosave"]
        if len(manual_ids) != 4:
            raise RuntimeError(f"Expected 4 manual versions (pruning skipped), got {len(manual_ids)}")

        if not all(k in ids for k in ["v002", "v005", "v006", "v007"]):
            raise RuntimeError("Some versions missing unexpectedly")

        print("Test 4 Passed.")

        print("\n--- Test 5: Manual Delete Protection ---")
        # v006 is locked. Try to delete it via operator.

        # Select v006
        idx = -1
        for i, v in enumerate(settings.versions):
            if v.version_id == "v006":
                idx = i
                break

        if idx == -1:
            raise RuntimeError("v006 not found in UI list")

        settings.active_version_index = idx

        # Execute delete
        res = bpy.ops.savepoints.delete()

        if "CANCELLED" not in res:
            # It might return FINISHED if we didn't implement the check in execute,
            # or passed silently. The operator uses report({'WARNING'}) and returns {'CANCELLED'}
            # But running from script without invoke might behave differently?
            # Let's check if it still exists.
            pass

        ids = get_version_ids()
        if "v006" not in ids:
            raise RuntimeError("Locked version v006 was deleted!")
        else:
            print("Locked version v006 was NOT deleted (Good).")

        # Unlock and delete
        bpy.ops.savepoints.toggle_protection(version_id="v006")
        bpy.ops.savepoints.delete()

        ids = get_version_ids()
        if "v006" in ids:
            raise RuntimeError("Unlocked version v006 failed to delete")

        print("Test 5 Passed.")

        print("\n--- Test 6: Daily Backup Retention ---")
        # 1. Reset Environment
        # Clear history to start fresh with v001
        reset_history()
        # Force refresh settings
        from savepoints.ui_utils import sync_history_to_props
        sync_history_to_props(bpy.context)

        # 2. Configure Settings
        settings.use_limit_versions = True
        settings.max_versions_to_keep = 1
        settings.keep_daily_backups = True

        # 3. Create Versions & Fake Timestamps

        # v001: 20 days ago (Old -> Prune)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Old 20d")
        set_version_timestamp("v001", 20)

        # v002: 15 days ago (Old but Protected -> Keep)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Old 15d Protected")
        set_version_timestamp("v002", 15)
        bpy.ops.savepoints.toggle_protection(version_id="v002")

        # v003: 13 days ago (Shadowed -> Prune)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="13d Early")
        set_version_timestamp("v003", 13, hour_offset=-2)  # 10:00

        # v004: 13 days ago (Latest of day -> Keep)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="13d Late")
        set_version_timestamp("v004", 13, hour_offset=0)  # 12:00

        # v005: 1 day ago (Yesterday -> Keep)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Yesterday")
        set_version_timestamp("v005", 1)

        # 4. Create v006 (Today) -> Triggers Pruning
        # max_keep=1. v006 is Recent.
        # v005 is Daily. v004 is Daily. v002 is Protected.
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Today")

        # 5. Verify
        ids = get_version_ids()
        print(f"IDs after Daily Prune: {ids}")

        expected_kept = {"v006", "v005", "v004", "v002"}
        expected_pruned = {"v001", "v003"}

        current_ids = set(ids)

        # Note: Autosave might be present if triggered, but we reset history so maybe not?
        # Autosave timer runs in background. Ideally we ignore "autosave" ID if present.
        if "autosave" in current_ids:
            current_ids.remove("autosave")

        if not expected_kept.issubset(current_ids):
            missing = expected_kept - current_ids
            raise RuntimeError(f"Missing expected versions: {missing}")

        if not expected_pruned.isdisjoint(current_ids):
            leaked = expected_pruned.intersection(current_ids)
            raise RuntimeError(f"Versions should have been pruned: {leaked}")

        print("Test 6 Passed.")

        print("\n--- Test 7: Autosave Lock Guard ---")
        # Ensure autosave exists
        from savepoints.operators import create_snapshot
        create_snapshot(bpy.context, "autosave", "Auto Save", skip_thumbnail=True)

        # Attempt to lock autosave
        # Note: In background mode, operators return a set. EXEC_DEFAULT executes directly.
        res = bpy.ops.savepoints.toggle_protection('EXEC_DEFAULT', version_id="autosave")

        # Verify in manifest that it is NOT protected
        manifest = core.load_manifest()
        autosave_entry = next((v for v in manifest["versions"] if v["id"] == "autosave"), None)

        if not autosave_entry:
            raise RuntimeError("Autosave missing for Test 7")

        if autosave_entry.get("is_protected", False):
            raise RuntimeError("Autosave was successfully protected (should be forbidden)")

        print("Test 7 Passed.")

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
