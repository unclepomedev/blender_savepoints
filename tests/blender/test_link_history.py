import json
import sys
import unittest

import bpy

# Add project root to sys.path
from savepoints_test_case import SavePointsTestCase


class TestLinkHistory(SavePointsTestCase):
    def test_link_history(self):
        print("\n--- Starting Link History Test ---")

        # 3. Create an orphaned history folder
        orphan_dir = self.test_dir / "some_random_backup_folder"
        orphan_dir.mkdir()

        # Add manifest
        manifest_data = {
            "parent_file": "unknown",
            "versions": [
                {"id": "v001", "note": "Old version"}
            ]
        }
        with open(orphan_dir / "manifest.json", "w") as f:
            json.dump(manifest_data, f)

        # Verify pre-conditions
        # History dir should be .test_project_history (derived from test_project.blend)
        history_dir = self.test_dir / ".test_project_history"

        if history_dir.exists():
            self.fail("History dir should not exist yet")

        # 4. Run Link History Operator
        print(f"Linking from: {orphan_dir}")

        # We pass both filepath and directory to be safe, as ImportHelper logic relies on them.
        res = bpy.ops.savepoints.link_history('EXEC_DEFAULT', filepath=str(orphan_dir), directory=str(orphan_dir))

        if "FINISHED" not in res:
            self.fail(f"Operator failed: {res}")

        # 5. Verify
        if not history_dir.exists():
            self.fail(f"History dir was not created at {history_dir}")

        if orphan_dir.exists():
            self.fail("Orphan dir was not removed/moved")

        if not (history_dir / "manifest.json").exists():
            self.fail("Manifest not found in new history dir")

        print("Link History Verification: OK")


if __name__ == "__main__":
    res = unittest.main(argv=[''], exit=False)
    if not res.result.wasSuccessful():
        sys.exit(1)
