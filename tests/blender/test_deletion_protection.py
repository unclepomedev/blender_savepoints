import sys
import time
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

from savepoints.services.storage import load_manifest
from savepoints.services.versioning import set_version_protection, delete_version_by_id, prune_versions
from savepoints_test_case import SavePointsTestCase


class TestDeletionProtection(SavePointsTestCase):

    def _create_dummy_version(self, note="Dummy"):
        """Helper to create a version and return its data."""
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note=note)
        manifest = load_manifest()
        # Assuming the new version is always at index 0 (newest)
        return manifest["versions"][0]

    def _get_all_version_ids(self):
        """Helper to get a list of all current version IDs."""
        manifest = load_manifest()
        return [v["id"] for v in manifest["versions"]]

    def test_deletion_protection_scenario(self):
        """
        Scenario:
        Validates the lifecycle of a protected version:
        1. Cannot be deleted by Operator (UI).
        2. Cannot be deleted by Internal API.
        3. Persists through Pruning (cleanup).
        4. Can be deleted after unprotecting.
        """
        print("Starting Deletion Protection Scenario...")

        settings = bpy.context.scene.savepoints_settings

        # Prepare the target version
        target_version = self._create_dummy_version(note="Protected Target")
        target_id = target_version["id"]

        # Enable protection
        set_version_protection(target_id, True)

        # --- Step 1: Manual Deletion Protection (Operator) ---
        with self.subTest(step="1. Protection against Operator"):
            print("Step 1: Attempting deletion via Operator...")

            # Target the specific version in UI list (index 0 currently)
            settings.active_version_index = 0

            # Attempt delete
            bpy.ops.savepoints.delete('EXEC_DEFAULT')

            # Verify: Should still exist
            current_ids = self._get_all_version_ids()
            self.assertIn(target_id, current_ids, "Protected version was deleted by Operator!")

        # --- Step 2: Internal API Protection ---
        with self.subTest(step="2. Protection against Internal API"):
            print("Step 2: Attempting deletion via Internal API...")

            # Attempt delete directly by ID
            delete_version_by_id(target_id)

            # Verify: Should still exist
            current_ids = self._get_all_version_ids()
            self.assertIn(target_id, current_ids, "Protected version was deleted by internal API!")

        # --- Step 3: Prune Protection ---
        with self.subTest(step="3. Protection against Pruning"):
            print("Step 3: Attempting deletion via Pruning...")

            # Create filler versions to push the protected version down the list
            # We add wait times to ensure timestamps are distinct
            for i in range(3):
                time.sleep(0.1)
                self._create_dummy_version(note=f"Filler {i}")

            # Now we have [Filler2, Filler1, Filler0, ProtectedTarget]
            # Prune with max_keep=1.
            # Normal behavior: Keep Filler2, delete everything else.
            # Protected behavior: Keep Filler2 AND ProtectedTarget.
            prune_versions(max_keep=1)

            current_ids = self._get_all_version_ids()

            # Verify: Protected version must persist
            self.assertIn(target_id, current_ids, "Protected version was deleted by Prune!")

            # Optional Verify: Pruning actually worked (some fillers should be gone)
            # Depending on implementation, Filler 0 or 1 should be gone.
            self.assertLess(len(current_ids), 4, "Pruning didn't delete any versions at all")

        # --- Step 4: Unprotect and Delete ---
        with self.subTest(step="4. Unprotect and Delete"):
            print("Step 4: Unprotecting and Deleting...")

            # Unprotect
            set_version_protection(target_id, False)

            # Delete
            delete_version_by_id(target_id)

            # Verify: Should be gone now
            current_ids = self._get_all_version_ids()
            self.assertNotIn(target_id, current_ids, "Unprotected version was NOT deleted!")

        print("Deletion Protection Scenario: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
