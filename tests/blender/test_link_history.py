import json
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


class TestLinkHistory(SavePointsTestCase):

    def test_link_history_scenario(self):
        """
        Scenario:
        1. Create an "orphaned" history folder with a valid manifest outside the project structure.
        2. Ensure the current project has no history folder yet.
        3. Execute 'Link History' operator targeting the orphan folder.
        4. Verify the orphan folder is moved/renamed to match the current project's history folder.
        """
        print("Starting Link History Scenario...")

        # Setup paths
        # SavePointsTestCase creates 'test_project.blend', so the target history dir is '.test_project_history'
        orphan_dir = self.test_dir / "some_random_backup_folder"
        target_history_dir = self.test_dir / ".test_project_history"

        # --- Step 1: Prepare Orphan Data ---
        with self.subTest(step="1. Prepare Orphan History"):
            print("Creating orphan history data...")

            orphan_dir.mkdir()

            # Create a dummy manifest
            manifest_data = {
                "parent_file": "unknown_origin.blend",
                "versions": [
                    {"id": "v001", "note": "Old version to link"}
                ]
            }

            manifest_path = orphan_dir / "manifest.json"
            with open(manifest_path, "w") as f:
                json.dump(manifest_data, f)

            self.assertTrue(manifest_path.exists(), "Setup failed: Manifest not created")

        # --- Step 2: Verify Pre-conditions ---
        with self.subTest(step="2. Verify Pre-conditions"):
            # Ensure the target location is empty so we know the operator actually did the work
            self.assertFalse(target_history_dir.exists(), "History dir should not exist before linking")

        # --- Step 3: Execute Link History ---
        with self.subTest(step="3. Execute Link History"):
            print(f"Linking from: {orphan_dir}...")

            # We pass both 'filepath' and 'directory' because ImportHelper-based operators
            # often require specific context args in headless execution.
            res = bpy.ops.savepoints.link_history('EXEC_DEFAULT', filepath=str(orphan_dir), directory=str(orphan_dir))

            self.assertIn('FINISHED', res, "Link History operator failed")

        # --- Step 4: Verify Result (Move & Rename) ---
        with self.subTest(step="4. Verify Link Result"):
            print("Verifying filesystem changes...")

            # 1. Target directory must now exist
            self.assertTrue(target_history_dir.exists(), f"History dir was not created at {target_history_dir}")

            # 2. Source (Orphan) directory must be gone (moved)
            self.assertFalse(orphan_dir.exists(), "Orphan dir was not removed/moved (Original folder should be gone)")

            # 3. Content verification
            new_manifest_path = target_history_dir / "manifest.json"
            self.assertTrue(new_manifest_path.exists(), "Manifest file missing in the new history location")

        print("Link History Scenario: Completed")


if __name__ == "__main__":
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
