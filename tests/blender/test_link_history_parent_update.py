import json

import sys
import unittest
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.linking import link_history
from savepoints_test_case import SavePointsTestCase


class TestLinkHistoryParentUpdate(SavePointsTestCase):
    def test_link_history_parent_update(self):
        print("Starting Link History Parent Update Test...")

        # 1. Setup paths
        old_blend_path = self.test_dir / "old_project.blend"
        new_blend_path = self.test_dir / "new_project.blend"

        # Fake source history directory
        source_history_name = ".old_project_history"
        source_history_dir = self.test_dir / source_history_name
        source_history_dir.mkdir()

        # Create manifest with old parent reference
        manifest_path = source_history_dir / "manifest.json"
        manifest_data = {
            "parent_file": str(old_blend_path),
            "versions": []
        }
        with manifest_path.open('w', encoding='utf-8') as f:
            json.dump(manifest_data, f)

        print(f"Created source history at {source_history_dir} with parent_file: {old_blend_path}")

        # 2. Execute Link History
        print("Executing link_history...")
        try:
            new_history_path_str = link_history(source_history_dir, str(new_blend_path))
        except Exception as e:
            self.fail(f"link_history failed: {e}")

        new_history_path = Path(new_history_path_str)

        self.assertTrue(new_history_path.exists(), "New history directory does not exist")

        # 3. Verify manifest update
        new_manifest_path = new_history_path / "manifest.json"
        with new_manifest_path.open('r', encoding='utf-8') as f:
            new_data = json.load(f)

        actual_parent = new_data.get("parent_file")

        if actual_parent != str(new_blend_path):
            # Try posix version if simple string fails (in case fix uses posix conversion)
            if actual_parent != Path(new_blend_path).as_posix():
                self.fail(f"FAILURE: parent_file was not updated. Expected {new_blend_path}, got {actual_parent}")

        print("SUCCESS: parent_file updated correctly.")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
