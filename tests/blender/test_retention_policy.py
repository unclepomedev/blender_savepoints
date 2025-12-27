import sys
import unittest
from pathlib import Path

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.manifest import load_manifest
from savepoints.services.versioning import set_version_protection
from savepoints.operators import create_snapshot
from savepoints_test_case import SavePointsTestCase


class TestRetentionPolicy(SavePointsTestCase):

    def _get_version_ids(self):
        """Helper to get list of version IDs from disk manifest."""
        manifest = load_manifest()
        return [v["id"] for v in manifest.get("versions", [])]

    def _get_version_entry(self, version_id):
        """Helper to get a specific version entry from manifest."""
        manifest = load_manifest()
        return next((v for v in manifest.get("versions", []) if v["id"] == version_id), None)

    def test_retention_scenario(self):
        """
        Scenario:
        1. Basic Limit: Verify pruning when limit is reached (Max 3).
        2. Disable Limit: Verify no pruning when limit is disabled.
        3. Re-enable Limit: Verify immediate pruning of excess versions upon next commit.
        4. Locked Versions: Verify locked versions are excluded from the quota count.
        5. Unlock & Prune: Verify unlocked versions become candidates for pruning.
        6. Autosave Guard: Verify autosave cannot be locked.
        """
        print("Starting Retention Policy Scenario...")

        settings = bpy.context.scene.savepoints_settings

        # --- Step 1: Basic Limit (Max 3) ---
        with self.subTest(step="1. Basic Limit (Max 3)"):
            settings.use_limit_versions = True
            settings.max_versions_to_keep = 3

            # Create 3 versions (v1, v2, v3)
            for i in range(3):
                bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"v{i + 1}")

            ids = self._get_version_ids()
            self.assertEqual(len(ids), 3, "Expected 3 versions")

            # Create 4th -> Should prune oldest (v001)
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v4")

            ids = self._get_version_ids()
            self.assertEqual(len(ids), 3, "Count should remain 3 after pruning")
            self.assertNotIn("v001", ids, "Oldest version (v001) should be pruned")
            self.assertIn("v004", ids, "Newest version (v004) should be present")

        # --- Step 2: Disable Limit ---
        with self.subTest(step="2. Disable Limit"):
            settings.use_limit_versions = False

            # Create 5th -> Should keep all (3 existing + 1 new = 4)
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v5")

            ids = self._get_version_ids()
            self.assertEqual(len(ids), 4, "Limit disabled: Should hold 4 versions")

        # --- Step 3: Re-enable Limit (Immediate Prune on Commit) ---
        with self.subTest(step="3. Re-enable Limit"):
            # Set tighter limit (Max 2)
            settings.use_limit_versions = True
            settings.max_versions_to_keep = 2

            # Current: [v5, v4, v3, v2] (4 versions)
            # Create v6 -> Total would be 5. Max 2.
            # Should prune oldest 3 versions (v2, v3, v4).
            # Expected remaining: v6, v5.
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v6")

            ids = self._get_version_ids()
            expected = ["v006", "v005"]
            self.assertEqual(ids, expected, f"Failed to prune multiple versions. Got: {ids}")

        # --- Step 4: Protected Versions (Quota Exclusion) ---
        with self.subTest(step="4. Protected Versions"):
            settings.use_limit_versions = False
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v7")
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v8")

            # Lock v8
            set_version_protection("v008", True)

            # Re-enable Limit (Max 2)
            # Current Unlocked: v7, v6, v5 (Oldest). Locked: v8.
            # If we commit v9, logic runs.
            settings.use_limit_versions = True
            settings.max_versions_to_keep = 2

            # Create v9
            # Unlocked candidates: v9, v7, v6, v5.
            # Locked: v8.
            # Quota 2. Should keep v9 and v7 (newest unlocked).
            # Should prune v6, v5.
            # Total kept: v9, v8(L), v7.
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v9")

            ids = self._get_version_ids()
            self.assertIn("v008", ids, "Locked version must be kept")
            self.assertIn("v007", ids, "v007 should be kept as part of quota (2)")
            self.assertIn("v009", ids, "v009 should be kept as part of quota (1)")
            self.assertNotIn("v006", ids, "v006 should be pruned")

            # Check total count: 2 (Quota) + 1 (Locked) = 3
            self.assertEqual(len(ids), 3)

            # Create v10 -> Pushes v7 out
            # Unlocked: v10, v9. (Count 2). v7 becomes 3rd -> Pruned.
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v10")

            ids = self._get_version_ids()
            self.assertNotIn("v007", ids, "v007 should be pruned now")
            self.assertIn("v008", ids, "Locked version still there")
            self.assertEqual(len(ids), 3, "Expected v10, v9, v8(L)")

        # --- Step 5: Unlock & Prune ---
        with self.subTest(step="5. Unlock & Prune"):
            # Current: v10, v9, v8(L).
            # Max=2.

            # Unlock v8
            set_version_protection("v008", False)

            # Now v8 is a candidate for pruning.
            # Current unlocked: v10, v9, v8. (Count 3). Max 2.
            # Next commit (v11) should force re-eval.

            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v11")

            ids = self._get_version_ids()
            # Expected: v11, v10. (v9 and v8 are pruned)
            # Logic: v11, v10, v9, v8 -> Keep top 2 -> v11, v10.

            self.assertNotIn("v008", ids, "Former locked version v008 should be pruned")
            self.assertNotIn("v009", ids, "v009 should be pruned")
            self.assertIn("v011", ids)
            self.assertIn("v010", ids)
            self.assertEqual(len(ids), 2)

        # --- Step 6: Autosave Guard ---
        with self.subTest(step="6. Autosave Guard"):
            # Manually create autosave
            create_snapshot(bpy.context, "autosave", "Auto Save", skip_thumbnail=True)

            # Attempt to lock autosave using operator
            # The operator poll or execute should prevent this, or it just ignores it.
            # If implementation raises error, we catch it. If it fails silently, we check flag.
            try:
                bpy.ops.savepoints.toggle_protection('EXEC_DEFAULT', version_id="autosave")
            except RuntimeError:
                # Operator might be disabled in poll, causing RuntimeError in headless exec
                pass

            # Verify it is NOT protected
            autosave_entry = self._get_version_entry("autosave")
            self.assertIsNotNone(autosave_entry, "Autosave should exist")
            self.assertFalse(autosave_entry.get("is_protected", False), "Autosave should not be protectable")

        print("Retention Policy Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
