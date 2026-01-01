import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services import versioning
from savepoints_test_case import SavePointsTestCase


class TestTrashDeletion(SavePointsTestCase):
    """
    E2E/Integration tests to verify that file deletion operations
    use send2trash (Recycle Bin) instead of permanent deletion.
    """

    def test_delete_version_uses_send2trash(self):
        """
        Verify that deleting a version calls send2trash on the version directory.
        """
        print("Starting Delete Version Trash Test...")

        # 1. Setup Environment
        history_dir = self.test_dir / ".test_project_history"
        history_dir.mkdir(parents=True, exist_ok=True)

        version_id = "v_trash_test"
        version_dir = history_dir / version_id
        version_dir.mkdir()

        # Mock manifest
        fake_manifest = {
            "versions": [
                {"id": version_id, "is_protected": False}
            ]
        }

        # 2. Patch & Verify
        with patch("savepoints.services.versioning.load_manifest", return_value=fake_manifest), \
                patch("savepoints.services.versioning.save_manifest") as mock_save, \
                patch("savepoints.services.versioning.send2trash") as mock_send2trash:
            # Execute
            versioning.delete_version_by_id(version_id)

            # Verify call
            mock_send2trash.assert_called_once()
            called_path_arg = mock_send2trash.call_args[0][0]
            self.assertEqual(Path(called_path_arg).resolve(), version_dir.resolve())

            print(f"Verified send2trash called for version: {called_path_arg}")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
