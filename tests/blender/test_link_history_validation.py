import json
import sys
import unittest
from pathlib import Path

from savepoints.services.linking import link_history
# Add project root to sys.path
from savepoints_test_case import SavePointsTestCase


class TestLinkHistoryValidation(SavePointsTestCase):
    def test_link_history_validation(self):
        print("Starting Link History Validation Test...")

        # Setup Paths
        # Use self.blend_path from base class (test_project.blend)
        project_path = self.blend_path

        bad_json_dir = self.test_dir / "bad_json_history"
        missing_keys_dir = self.test_dir / "missing_keys_history"
        valid_dir = self.test_dir / "valid_history"

        # 1. Test Malformed JSON
        bad_json_dir.mkdir()
        (bad_json_dir / "manifest.json").write_text("{ this is not json }", encoding='utf-8')

        print("Testing Malformed JSON...")
        try:
            link_history(bad_json_dir, str(project_path))
            self.fail("Malformed JSON should have raised ValueError")
        except ValueError as e:
            print(f"Caught expected error: {e}")
            pass

        # 2. Test Missing Keys (Valid JSON but not a manifest)
        missing_keys_dir.mkdir()
        (missing_keys_dir / "manifest.json").write_text("{}", encoding='utf-8')

        print("Testing Missing Keys...")
        try:
            link_history(missing_keys_dir, str(project_path))
            self.fail("Empty JSON should have raised ValueError")
        except ValueError as e:
            print(f"Caught expected error: {e}")

        # 3. Test Valid Manifest
        valid_dir.mkdir()
        valid_manifest = {
            "versions": [],
            "parent_file": str(project_path)
        }
        with (valid_dir / "manifest.json").open('w', encoding='utf-8') as f:
            json.dump(valid_manifest, f)

        print("Testing Valid Manifest...")
        # This should succeed
        target_path_str = link_history(valid_dir, str(project_path))
        print("Valid manifest linked successfully.")

        # Verification
        target_path = Path(target_path_str)
        if not target_path.exists():
            self.fail(f"Target history directory not found at: {target_path}")

        if valid_dir.exists():
            self.fail(f"Source directory still exists at: {valid_dir}")

        if not (target_path / "manifest.json").exists():
            self.fail("manifest.json not found in target directory")

        # Expect .test_project_history because blend file is test_project.blend
        expected_name = ".test_project_history"
        if target_path.name != expected_name:
            self.fail(f"Unexpected target directory name. Expected {expected_name}, got {target_path.name}")

        print("ALL VALIDATION TESTS PASSED")


if __name__ == "__main__":
    res = unittest.main(argv=[''], exit=False)
    if not res.result.wasSuccessful():
        sys.exit(1)
