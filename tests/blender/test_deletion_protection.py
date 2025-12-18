import sys
import time
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
from savepoints.services.versioning import set_version_protection, delete_version_by_id, prune_versions
from savepoints_test_case import SavePointsTestCase


class TestDeletionProtection(SavePointsTestCase):
    def create_dummy_version(self, settings, note="Dummy"):
        # Create a version via operator
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note=note)
        manifest = load_manifest()
        return manifest["versions"][0]

    def test_deletion_protection(self):
        print("Starting Deletion Protection Test (Extended)...")

        # 1. Setup
        # SavePointsTestCase creates test_project.blend and registers addon
        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Manual Deletion Protection (Operator) ---")

        # Create a version
        v1 = self.create_dummy_version(settings, "Protected Version")
        v1_id = v1["id"]

        # Enable protection
        set_version_protection(v1_id, True)

        # Try to delete via operator
        settings.active_version_index = 0
        bpy.ops.savepoints.delete('EXEC_DEFAULT')

        # Check manifest
        manifest = load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])
        if not found:
            self.fail("Protected version was deleted by Operator!")
        print("Test 1 Passed.")

        print("\n--- Test 2: Internal API Protection ---")
        delete_version_by_id(v1_id)
        manifest = load_manifest()
        found = any(v["id"] == v1_id for v in manifest["versions"])
        if not found:
            self.fail("Protected version was deleted by internal API!")
        print("Test 2 Passed.")

        print("\n--- Test 3: Prune Protection (Basic) ---")
        # Create filler versions
        for i in range(3):
            self.create_dummy_version(settings, f"Filler {i}")
            time.sleep(0.1)

        # v1 (Protected) is now index 3 (Oldest)
        # Prune max_keep=1
        prune_versions(max_keep=1)

        manifest = load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]
        if v1_id not in remaining_ids:
            self.fail("Protected version was deleted by Prune!")
        print("Test 3 Passed.")

        print("\n--- Test 4: Unprotect and Delete ---")
        # Create a fresh version for this test since previous tests might have cleared the manifest
        v5 = self.create_dummy_version(settings, "Version to Unprotect")
        v5_id = v5["id"]

        # Ensure it starts protected
        set_version_protection(v5_id, True)

        # Unprotect
        set_version_protection(v5_id, False)

        # Delete
        delete_version_by_id(v5_id)

        # Verify deletion
        manifest = load_manifest()
        remaining_ids = [v["id"] for v in manifest["versions"]]
        if v5_id in remaining_ids:
            self.fail("Unprotected version was NOT deleted!")
        print("Test 4 Passed.")

        print("\nALL TESTS PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
