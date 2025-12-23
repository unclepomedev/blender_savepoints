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

from savepoints.services import versioning, rescue
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

    def test_delete_rescue_temp_file_uses_send2trash(self):
        """
        Verify that deleting a rescue temp file calls send2trash.
        """
        print("Starting Rescue Temp File Trash Test...")

        # 1. Setup
        temp_file = self.test_dir / "rescue_temp.blend"
        temp_file.touch()

        # 2. Patch & Verify
        with patch("savepoints.services.rescue.send2trash") as mock_send2trash:
            # Execute
            rescue.delete_rescue_temp_file(temp_file)

            # Verify
            mock_send2trash.assert_called_once_with(str(temp_file))
            print(f"Verified send2trash called for rescue temp file: {temp_file}")

    def test_cleanup_rescue_temp_files_uses_send2trash(self):
        """
        Verify that the cleanup function iterates versions and trashes temp files.
        """
        print("Starting Cleanup Rescue Files Trash Test...")

        # 1. Setup history structure
        custom_history_dir = self.test_dir / "custom_history"
        custom_history_dir.mkdir()

        # Create versions
        v1 = custom_history_dir / "v1"
        v1.mkdir()
        v2 = custom_history_dir / "v2"
        v2.mkdir()

        # Create temp files
        t1 = v1 / rescue.RESCUE_TEMP_FILENAME
        t1.touch()
        t2 = v2 / rescue.RESCUE_TEMP_FILENAME
        t2.touch()

        # Create safe file
        safe_file = v1 / "keep_me.txt"
        safe_file.touch()

        # 2. Patch & Verify
        with patch("savepoints.services.rescue.get_history_dir", return_value=str(custom_history_dir)), \
                patch("savepoints.services.rescue.send2trash") as mock_send2trash:
            # Execute
            count = rescue.cleanup_rescue_temp_files()

            # Verify counts
            self.assertEqual(count, 2, "Should have cleaned up 2 files")
            self.assertEqual(mock_send2trash.call_count, 2, "Should have called send2trash 2 times")

            # Verify arguments
            called_args = [str(Path(args[0]).resolve()) for args, _ in mock_send2trash.call_args_list]
            self.assertIn(str(t1.resolve()), called_args)
            self.assertIn(str(t2.resolve()), called_args)
            self.assertNotIn(str(safe_file.resolve()), called_args)

            print("Verified cleanup_rescue_temp_files trashed expected files.")

    def test_create_rescue_temp_file_cleanup_on_failure(self):
        """
        Verify that if rescue temp file creation times out (invalid file),
        it is cleaned up using send2trash.
        """
        print("Starting Create Rescue Temp Failure Trash Test...")

        # 1. Setup
        snapshot_path = self.test_dir / "snapshot.blend"
        snapshot_path.touch()  # Create empty file (size 0)

        # 2. Patch & Verify
        with patch("savepoints.services.rescue.send2trash") as mock_send2trash, \
                patch("savepoints.services.rescue.time") as mock_time:
            # Simulate timeout
            mock_time.time.side_effect = [1000.0, 1002.0, 1003.0]
            mock_time.sleep.return_value = None

            # Execute & Expect Error
            with self.assertRaises(TimeoutError):
                rescue.create_rescue_temp_file(snapshot_path)

            # Verify Cleanup
            expected_temp_path = snapshot_path.parent / rescue.RESCUE_TEMP_FILENAME
            mock_send2trash.assert_called_once_with(str(expected_temp_path))

            print(f"Verified create_rescue_temp_file cleanup called send2trash on {expected_temp_path}")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
