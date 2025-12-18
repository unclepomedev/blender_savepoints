import sys
import unittest
from pathlib import Path

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.storage import load_manifest
from savepoints.services.versioning import set_version_protection
from savepoints_test_case import SavePointsTestCase


class TestRetentionPolicy(SavePointsTestCase):
    def get_version_ids(self):
        manifest = load_manifest()
        return [v["id"] for v in manifest.get("versions", [])]

    def test_retention_policy_flow(self):
        print("Starting Retention Policy Test...")
        # SavePointsTestCase creates test_dir and setups blend_path

        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Basic Limit (Max 3) ---")
        settings.use_limit_versions = True
        settings.max_versions_to_keep = 3

        # Create 3 versions
        for i in range(3):
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"v{i + 1}")

        ids = self.get_version_ids()
        self.assertEqual(len(ids), 3, f"Expected 3 versions, got {len(ids)}")

        # Create 4th -> Should delete v001 (Oldest)
        # Note: In our list, v003 is Newest (index 0), v001 is Oldest (index 2)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v4")

        ids = self.get_version_ids()
        print(f"IDs: {ids}")
        self.assertEqual(len(ids), 3, f"Expected 3 versions after pruning, got {len(ids)}")

        self.assertNotIn("v001", ids, "v001 should have been pruned")
        self.assertIn("v004", ids, "v004 should be present")

        print("Test 1 Passed.")

        print("\n--- Test 2: Disable Limit ---")
        settings.use_limit_versions = False

        # Create 5th -> Should keep all (3 + 1 = 4)
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v5")

        ids = self.get_version_ids()
        self.assertEqual(len(ids), 4, f"Expected 4 versions, got {len(ids)}")

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

        ids = self.get_version_ids()
        print(f"IDs: {ids}")
        self.assertEqual(len(ids), 2, f"Expected 2 versions, got {len(ids)}")

        expected = ["v006", "v005"]
        self.assertEqual(ids, expected, f"Mismatch. Expected {expected}, got {ids}")

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

        ids = self.get_version_ids()
        print(f"IDs after v9: {ids}")

        self.assertIn("v007", ids, "v007 should be kept because v008(Locked) does not count towards quota.")
        self.assertEqual(len(ids), 3, f"Expected 3 versions (v9, v8L, v7), got {len(ids)}")

        # Create v10.
        # List: v10, v9, v8(L), v7.
        # Unlocked: v10, v9, v7. (Count = 3).
        # Max = 2.
        # Oldest unlocked is v7. Should be pruned.
        # Result: v10, v9, v8(L).

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v10")

        ids = self.get_version_ids()
        print(f"IDs after v10: {ids}")

        self.assertNotIn("v007", ids, "v007 should be pruned now.")
        self.assertEqual(len(ids), 3, f"Expected 3 versions (v10, v9, v8L), got {len(ids)}")

        print("Test 4 Passed.")

        print("\n--- Test 5: Unprotect to Prune ---")
        # Current State from Test 4: v10, v9, v8(L). Max=2.
        # Unlocked: v10, v9 (Count=2). Locked: v8.
        # All kept.

        ids = self.get_version_ids()
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

        ids = self.get_version_ids()
        print(f"IDs after v11: {ids}")

        # Expected: v11, v10.
        self.assertNotIn("v008", ids, "v008 (Unlocked) should be pruned")
        self.assertNotIn("v009", ids, "v009 (Old Unlocked) should be pruned")
        self.assertIn("v011", ids, "v011 (Newest) should be kept")
        self.assertIn("v010", ids, "v010 (2nd Newest) should be kept")

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

        self.assertIsNotNone(autosave_entry, "Autosave entry missing")
        self.assertFalse(autosave_entry.get("is_protected", False), "Autosave should NOT be protectable")

        print("Test 6 Passed.")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
