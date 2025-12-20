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

from savepoints_test_case import SavePointsTestCase
from savepoints.services.versioning import set_version_protection


class TestPruningOnRefresh(SavePointsTestCase):

    def test_pruning_on_refresh(self):
        """
        Scenario:
        1. Disable limit versions.
        2. Create versions more than the limit.
        3. Enable limit versions.
        4. Call Refresh.
        5. Verify that excess versions are pruned.
        """
        print("Starting Pruning On Refresh Scenario...")

        settings = bpy.context.scene.savepoints_settings

        # --- Step 1: Create versions without limit ---
        with self.subTest(step="1. Create Versions"):
            settings.use_limit_versions = False

            # Create 3 versions
            for i in range(3):
                bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"Version {i + 1}")

            # Verify 3 versions exist
            self.assertEqual(len(settings.versions), 3, "Should have 3 versions")

        # --- Step 2: Enable Limit and Refresh ---
        with self.subTest(step="2. Enable Limit and Refresh"):
            settings.use_limit_versions = True
            settings.max_versions_to_keep = 2

            print("Executing Refresh...")
            bpy.ops.savepoints.refresh('EXEC_DEFAULT')

            # Verify versions count
            self.assertEqual(len(settings.versions), 2, "Should be pruned to 2 versions")

            # Verify the correct versions remain (latest ones)
            remaining_notes = [v.note for v in settings.versions]
            self.assertNotIn("Version 1", remaining_notes, "Oldest version should be pruned")
            self.assertIn("Version 2", remaining_notes)
            self.assertIn("Version 3", remaining_notes)

        print("Pruning On Refresh Scenario: Completed")

    def test_no_pruning_when_disabled(self):
        """
        Scenario:
        1. Disable limit versions.
        2. Create versions (e.g. 3).
        3. Set max_versions_to_keep to 2 (but limit is disabled).
        4. Call Refresh.
        5. Verify that NO pruning happens.
        """
        print("Starting No Pruning When Disabled Scenario...")
        settings = bpy.context.scene.savepoints_settings

        # --- Step 1: Create Versions ---
        settings.use_limit_versions = False
        settings.max_versions_to_keep = 2

        for i in range(3):
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note=f"Version {i + 1}")

        self.assertEqual(len(settings.versions), 3, "Should have 3 versions")

        # --- Step 2: Refresh with limit disabled ---
        print("Executing Refresh (Limit Disabled)...")
        bpy.ops.savepoints.refresh('EXEC_DEFAULT')

        # --- Step 3: Verify ---
        self.assertEqual(len(settings.versions), 3, "Should still have 3 versions because limit is disabled")

        print("No Pruning When Disabled Scenario: Completed")

    def test_pruning_respects_protection(self):
        """
        Scenario:
        1. Enable limit (Max=1).
        2. Create Version 1 and LOCK it.
        3. Create Version 2 (Latest).
        4. Call Refresh.
        5. Verify that Version 1 is KEPT (because it's locked) even though it's old.
           Verify that Version 2 is KEPT (because it fits the quota of 1).
           Total should be 2.
        """
        print("Starting Pruning With Protection Scenario...")
        settings = bpy.context.scene.savepoints_settings

        # --- Setup ---
        settings.use_limit_versions = True
        settings.max_versions_to_keep = 1

        # Create Version 1
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Version 1")

        # Lock Version 1
        # Use service function because property setter doesn't sync to disk (manifest)
        # settings.versions[0].is_protected = True
        v1_id = settings.versions[0].version_id
        set_version_protection(v1_id, True)

        # Create Version 2
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Version 2")

        # --- Execute Refresh ---
        print("Executing Refresh with Locked Item...")
        bpy.ops.savepoints.refresh('EXEC_DEFAULT')

        # --- Verify ---
        # Logic:
        # Locked(v1) -> Kept unconditionally (does not consume quota)
        # Unlocked(v2) -> Fits within quota (1), so it remains.

        self.assertEqual(len(settings.versions), 2, "Locked version should be ignored from quota")
        notes = [v.note for v in settings.versions]
        self.assertIn("Version 1", notes, "Locked version 1 should be protected")
        self.assertIn("Version 2", notes, "Newest version 2 should be kept")

        print("Pruning With Protection Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
