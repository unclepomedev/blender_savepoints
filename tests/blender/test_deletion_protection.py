import datetime
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

        print("\n--- Test 4: Keep Daily Backups Interaction ---")
        # Clear all existing versions to start clean for this complex test
        manifest = core.load_manifest()
        manifest["versions"] = []
        core.save_manifest(manifest)

        now = datetime.datetime.now()

        # Scenario A: Ancient History (Older than 14 days)
        # 20 days ago
        ancient_date = now - datetime.timedelta(days=20)

        # Create Ancient Protected
        v_ancient_prot = create_dummy_version(settings, "Ancient Protected")
        core.set_version_protection(v_ancient_prot["id"], True)
        set_version_timestamp(v_ancient_prot["id"], ancient_date)

        # Create Ancient Unprotected
        v_ancient_unprot = create_dummy_version(settings, "Ancient Unprotected")
        core.set_version_protection(v_ancient_unprot["id"], False)
        set_version_timestamp(v_ancient_unprot["id"], ancient_date)

        # Scenario B: Recent History (Yesterday) - Crowded Day
        # Use yesterday midnight to avoid rolling over to today when adding hours
        yesterday_date = now.date() - datetime.timedelta(days=1)
        yesterday = datetime.datetime.combine(yesterday_date, datetime.time(0, 0))

        # We need to add them so that they appear in correct order in manifest (Newest -> Oldest)
        # create_dummy_version appends to top (Newest).
        # So we should create them in reverse chronological order if we want to simulate reality easily,
        # OR we just create them and then fix timestamps. 
        # But verify logic: prune_versions iterates manifest list.
        # It expects Newest first.
        # So v_yest_4 (13:00) should be at index 0 (of yesterday group).

        # Let's create them:

        # v_yest_4 (Newest of day) - Should be KEPT as Daily Keeper
        v_yest_4 = create_dummy_version(settings, "Yesterday 13:00 (Keeper)")
        set_version_timestamp(v_yest_4["id"], yesterday + datetime.timedelta(hours=13))

        # v_yest_3 (Unprotected) - Should be DELETED
        v_yest_3 = create_dummy_version(settings, "Yesterday 12:00 (Delete)")
        set_version_timestamp(v_yest_3["id"], yesterday + datetime.timedelta(hours=12))

        # v_yest_2 (Protected) - Should be KEPT (Protected)
        v_yest_2 = create_dummy_version(settings, "Yesterday 11:00 (Protected)")
        core.set_version_protection(v_yest_2["id"], True)
        set_version_timestamp(v_yest_2["id"], yesterday + datetime.timedelta(hours=11))

        # v_yest_1 (Oldest of day) - Should be DELETED
        v_yest_1 = create_dummy_version(settings, "Yesterday 10:00 (Delete)")
        set_version_timestamp(v_yest_1["id"], yesterday + datetime.timedelta(hours=10))

        # v_today (Today) - Recent buffer
        v_today = create_dummy_version(settings, "Today (Recent)")
        # Timestamp is already roughly now, but set explicitly
        set_version_timestamp(v_today["id"], now)

        # Note: create_dummy_version inserts at 0.
        # So currently order in manifest is:
        # v_yest_1, v_yest_2, v_yest_3, v_yest_4, v_ancient_unprot, v_ancient_prot
        # But timestamps are:
        # v_yest_1 (10:00) < v_yest_2 (11:00) < ...
        # So manifest order is Oldest -> Newest (Reverse of typical usage if we just pushed them).
        # Wait, create_dummy_version:
        #   add_version_to_manifest -> manifest["versions"].insert(0, new_version)
        # So the LAST one created is at index 0.
        # We created v_ancient_prot first. It is at bottom.
        # We created v_yest_1 last. It is at top.

        # So manifest list: [v_yest_1, v_yest_2, v_yest_3, v_yest_4, v_ancient_unprot, v_ancient_prot]
        # Timestamps:
        # v_yest_1: Yest 10:00
        # v_yest_2: Yest 11:00
        # v_yest_3: Yest 12:00
        # v_yest_4: Yest 13:00
        # v_ancient_unprot: -20d
        # v_ancient_prot: -20d

        # This order is "Oldest First" for the Yesterday group.
        # But logic `prune_versions` says:
        # "Since list is Newest -> Oldest, the first version we encounter for a given date is the latest one."
        # If our list is NOT Newest -> Oldest, the logic might fail or pick the wrong one as "Latest".
        # If list is v_yest_1 (10:00) first... it will pick v_yest_1 as the "Daily Keeper" because it hits it first.
        # But strictly speaking, savepoints ensures Newest->Oldest order by inserting at 0.
        # So we should create them in Chronological order (Oldest creation first) to get Newest at top?
        # NO.
        # If I create V1, it is at 0.
        # If I create V2, it is at 0. V1 is at 1.
        # So V2 (Newer) is before V1 (Older). This is correct Newest->Oldest.

        # So I should create Oldest *First*.
        # My creation order above:
        # 1. Ancient Prot
        # 2. Ancient Unprot
        # ...
        # Last: v_yest_1

        # So v_yest_1 is at index 0. It is the NEWEST created.
        # BUT I assigned it timestamp 10:00.
        # And I assigned v_yest_4 timestamp 13:00.
        # So v_yest_4 (at index ~3) is OLDER creation-wise (so lower index? No, higher index), but I gave it a NEWER timestamp.
        # Let's trace:
        # Create V_A (Index 0). List: [V_A]
        # Create V_B (Index 0). List: [V_B, V_A]
        # Create V_C (Index 0). List: [V_C, V_B, V_A]

        # If I want [V_Newest, V_Older, V_Oldest]
        # I must create V_Oldest, then V_Older, then V_Newest.

        # My creation order for Yesterday group:
        # v_yest_4 (13:00) -> First created.
        # v_yest_3 (12:00)
        # v_yest_2 (11:00)
        # v_yest_1 (10:00) -> Last created.

        # Result list: [v_yest_1, v_yest_2, v_yest_3, v_yest_4 ...]
        # Timestamp order: 10:00, 11:00, 12:00, 13:00 ...
        # So index 0 is 10:00 (Oldest of day).
        # This breaks the "Newest -> Oldest" assumption of the list.
        # The list is sorted by "Creation Time" (implicitly), but I am overriding timestamps.

        # To fix this test, I must sort the manifest manually to ensure it respects Newest->Oldest timestamp order,
        # otherwise `prune_versions` logic (which relies on order) might behave unexpectedly (picking the first one it sees).

        # Let's re-sort the manifest by timestamp descending.
        manifest = core.load_manifest()
        manifest["versions"].sort(key=lambda x: x["timestamp"], reverse=True)
        core.save_manifest(manifest)

        # Now list should be:
        # v_yest_4 (13:00)
        # v_yest_3 (12:00)
        # v_yest_2 (11:00)
        # v_yest_1 (10:00)
        # v_ancient (Unprot or Prot depending on exact time, same date)

        # Execute Prune
        # max_keep=1 (Keep 1 recent version. The rest depends on daily logic)
        # keep_daily_backups=True

        deleted_count = core.prune_versions(max_keep=1, keep_daily_backups=True)

        manifest = core.load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]

        print(f"Remaining IDs: {remaining_ids}")

        # Assertions

        # Today (Recent)
        if v_today["id"] not in remaining_ids:
            raise RuntimeError("Recent version (v_today) was deleted!")

        # Ancient:
        if v_ancient_prot["id"] not in remaining_ids:
            raise RuntimeError("Ancient Protected version was deleted!")
        if v_ancient_unprot["id"] in remaining_ids:
            raise RuntimeError("Ancient Unprotected version was NOT deleted!")

        # Yesterday:
        # v_yest_4 (Newest/Daily Keeper) -> Keep
        if v_yest_4["id"] not in remaining_ids:
            raise RuntimeError("Daily Keeper (Newest) was deleted!")

        # v_yest_2 (Protected) -> Keep
        if v_yest_2["id"] not in remaining_ids:
            raise RuntimeError("Intermediate Protected version was deleted!")

        # v_yest_3 (Unprotected, Intermediate) -> Delete
        if v_yest_3["id"] in remaining_ids:
            raise RuntimeError("Intermediate Unprotected version (v_yest_3) was NOT deleted!")

        # v_yest_1 (Oldest, Intermediate) -> Delete
        if v_yest_1["id"] in remaining_ids:
            raise RuntimeError("Intermediate Unprotected version (v_yest_1) was NOT deleted!")

        print("Test 4 Passed: Daily Backup + Protection interaction verified.")

        print("\n--- Test 5: Unprotect and Delete ---")
        core.set_version_protection(v1_id, False)
        core.delete_version_by_id(v1_id)
        print("Test 5 Passed.")

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
