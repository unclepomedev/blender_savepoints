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

from savepoints.services.storage import ensure_directory
from savepoints_test_case import SavePointsTestCase


class TestWindowsHiddenFolder(SavePointsTestCase):

    def test_ensure_directory_scenario(self):
        """
        Scenario:
        1. Windows + Dot Folder: Verify folders starting with '.' get the Hidden attribute (0x02).
        2. Windows + Normal Folder: Verify normal folders do NOT get the Hidden attribute.
        3. Non-Windows + Dot Folder: Verify no attributes are set on Linux/Mac even for dot folders.
        """
        print("Starting Windows Hidden Folder Scenario...")

        # Constants
        FILE_ATTRIBUTE_HIDDEN = 0x02

        # --- Step 1: Windows + Dot Folder ---
        with self.subTest(step="1. Windows + Dot Folder"):
            dot_folder = self.test_dir / ".hidden_history_win"

            # Mock Windows environment
            with patch('sys.platform', 'win32'):
                with patch('savepoints.services.storage.ctypes') as mock_ctypes:
                    # Setup Mock
                    mock_set_attr = MagicMock()
                    mock_ctypes.windll.kernel32.SetFileAttributesW = mock_set_attr

                    # Execute
                    ensure_directory(dot_folder)

                    # Assert: Directory exists
                    self.assertTrue(dot_folder.exists())
                    self.assertTrue(dot_folder.is_dir())

                    # Assert: Hidden attribute set
                    mock_set_attr.assert_called_once_with(str(dot_folder), FILE_ATTRIBUTE_HIDDEN)

        # --- Step 2: Windows + Normal Folder ---
        with self.subTest(step="2. Windows + Normal Folder"):
            normal_folder = self.test_dir / "visible_folder"

            # Mock Windows environment
            with patch('sys.platform', 'win32'):
                with patch('savepoints.services.storage.ctypes') as mock_ctypes:
                    mock_set_attr = MagicMock()
                    mock_ctypes.windll.kernel32.SetFileAttributesW = mock_set_attr

                    # Execute
                    ensure_directory(normal_folder)

                    # Assert: Directory exists
                    self.assertTrue(normal_folder.exists())

                    # Assert: Attribute NOT set
                    mock_set_attr.assert_not_called()

        # --- Step 3: Non-Windows + Dot Folder ---
        with self.subTest(step="3. Non-Windows + Dot Folder"):
            dot_folder_linux = self.test_dir / ".hidden_linux"

            # Mock Linux environment
            with patch('sys.platform', 'linux'):
                with patch('savepoints.services.storage.ctypes') as mock_ctypes:
                    mock_set_attr = MagicMock()
                    mock_ctypes.windll.kernel32.SetFileAttributesW = mock_set_attr

                    # Execute
                    ensure_directory(dot_folder_linux)

                    # Assert: Directory exists
                    self.assertTrue(dot_folder_linux.exists())

                    # Assert: Attribute NOT set (Linux handles dot files natively)
                    mock_set_attr.assert_not_called()

        print("Windows Hidden Folder Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
