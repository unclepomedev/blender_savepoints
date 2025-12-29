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

from savepoints.services import thumbnail
from savepoints_test_case import SavePointsTestCase


class TestThumbnailLogic(SavePointsTestCase):
    """
    Test logic in thumbnail.py, mocking the actual render operator.
    """

    def test_resize_renames_double_extension(self):
        """Verify that _resize_image_file handles double extension (file.png.png)"""
        print("Starting Rename Logic Test...")

        target_path = self.test_dir / "my_thumb.png"
        double_ext_path = self.test_dir / "my_thumb.png.png"

        # Create the double extension file (Valid PNG)
        TINY_PNG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'

        with open(double_ext_path, 'wb') as f:
            f.write(TINY_PNG)

        thumbnail._resize_image_file(str(target_path))

        # Verify renaming happened
        self.assertTrue(target_path.exists(), "Target file should exist after rename")
        self.assertFalse(double_ext_path.exists(), "Double extension file should be gone")

        print("Rename logic verified.")

    def test_resize_recovers_wrong_extension(self):
        """Verify that _resize_image_file recovers file with wrong extension (e.g. .exr)"""
        print("Starting Wrong Extension Recovery Test...")

        target_path = self.test_dir / "recover_test.png"
        wrong_ext_path = self.test_dir / "recover_test.exr"

        # Create a file with .exr extension (content is PNG for simplicity, Blender should handle it after rename)
        TINY_PNG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'

        with open(wrong_ext_path, 'wb') as f:
            f.write(TINY_PNG)

        # Ensure target doesn't exist
        if target_path.exists():
            target_path.unlink()

        # Run logic
        thumbnail._resize_image_file(str(target_path))

        # Verify:
        self.assertFalse(wrong_ext_path.exists(), "Wrong extension file should be moved")
        self.assertTrue(target_path.exists(), "Target .png file should exist after recovery")

        print("Recovery logic verified.")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
