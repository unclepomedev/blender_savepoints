import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services import storage
from savepoints_test_case import SavePointsTestCase


class TestDiskUsageAlert(SavePointsTestCase):
    """
    Verify disk usage checking logic.
    """

    def test_get_free_disk_space(self):
        """
        Verify get_free_disk_space returns correct bytes from shutil.disk_usage.
        """
        print("Starting test_get_free_disk_space...")

        # 10 GB in bytes
        ten_gb = 10 * 1024 * 1024 * 1024

        # Mock usage return
        mock_usage = MagicMock()
        mock_usage.free = ten_gb

        # Patch shutil in storage module (we will add the import there)
        with patch("savepoints.services.storage.shutil.disk_usage", return_value=mock_usage) as mock_disk_usage:
            # Call the function (to be implemented)
            # We pass a dummy path
            free_space = storage.get_free_disk_space("/dummy/path")

            self.assertEqual(free_space, ten_gb)
            mock_disk_usage.assert_called_with("/dummy/path")
            print("Verified get_free_disk_space returns correct value.")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
