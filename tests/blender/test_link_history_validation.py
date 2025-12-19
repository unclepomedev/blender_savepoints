import json
import sys
import unittest
from pathlib import Path

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.linking import link_history
from savepoints_test_case import SavePointsTestCase


class TestLinkHistoryValidation(SavePointsTestCase):

    def test_link_history_validation_scenario(self):
        """
        Scenario:
        1. Attempt to link a history folder with a malformed (non-JSON) manifest -> Expect ValueError.
        2. Attempt to link a history folder with valid JSON but missing required keys -> Expect ValueError.
        3. Link a valid history folder -> Expect Success, directory move, and correct naming.
        """
        print("Starting Link History Validation Scenario...")

        # Setup Paths
        project_path = str(self.blend_path)  # test_project.blend

        bad_json_dir = self.test_dir / "bad_json_history"
        missing_keys_dir = self.test_dir / "missing_keys_history"
        valid_dir = self.test_dir / "valid_history"

        # --- Step 1: Test Malformed JSON ---
        with self.subTest(step="1. Malformed JSON"):
            print("Testing Malformed JSON input...")

            bad_json_dir.mkdir()
            (bad_json_dir / "manifest.json").write_text("{ this is not json }", encoding='utf-8')

            # Verify that link_history raises ValueError for invalid JSON syntax
            with self.assertRaises(ValueError, msg="Malformed JSON should raise ValueError"):
                link_history(bad_json_dir, project_path)

        # --- Step 2: Test Missing Keys ---
        with self.subTest(step="2. Missing Keys"):
            print("Testing Missing Keys input...")

            missing_keys_dir.mkdir()
            (missing_keys_dir / "manifest.json").write_text("{}", encoding='utf-8')

            # Verify that link_history raises ValueError for missing schema keys (e.g., 'parent_file')
            with self.assertRaises(ValueError, msg="Empty JSON should raise ValueError"):
                link_history(missing_keys_dir, project_path)

        # --- Step 3: Test Valid Manifest (Happy Path) ---
        with self.subTest(step="3. Valid Manifest"):
            print("Testing Valid Manifest input...")

            valid_dir.mkdir()
            valid_manifest = {
                "versions": [],
                "parent_file": project_path
            }

            with (valid_dir / "manifest.json").open('w', encoding='utf-8') as f:
                json.dump(valid_manifest, f)

            # Execution
            target_path_str = link_history(valid_dir, project_path)
            target_path = Path(target_path_str)

            # Verification
            # 1. Target directory should exist
            self.assertTrue(target_path.exists(), f"Target history directory not found at: {target_path}")

            # 2. Source directory should be moved (not exist)
            self.assertFalse(valid_dir.exists(), f"Source directory still exists at: {valid_dir}")

            # 3. Manifest should be preserved
            self.assertTrue((target_path / "manifest.json").exists(), "manifest.json not found in target directory")

            # 4. Directory name check (Should be .test_project_history)
            expected_name = ".test_project_history"
            self.assertEqual(target_path.name, expected_name,
                             f"Unexpected target directory name. Expected '{expected_name}', got '{target_path.name}'")

        print("Link History Validation Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
