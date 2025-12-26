import os
import re
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

from savepoints.services.batch_render import get_batch_render_output_dir
from savepoints_test_case import SavePointsTestCase


class TestBatchRenderUtils(SavePointsTestCase):
    def test_get_batch_render_output_dir(self):
        """
        Verify that the output directory follows the format:
        renders_batch/{blend_name}_{timestamp}
        """
        # Ensure we have a filepath set (SavePointsTestCase usually saves as test_project.blend)
        # But let's verify explicitly
        self.assertTrue(bpy.data.filepath, "Test setup should have saved a blend file")

        blend_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]

        output_dir = get_batch_render_output_dir()

        # Structure check
        # Expected: .../renders_batch/test_project_YYYYMMDD_HHMMSS

        parent_dir = os.path.dirname(output_dir)
        folder_name = os.path.basename(output_dir)

        self.assertEqual(os.path.basename(parent_dir), "renders_batch")

        # Regex check for folder name
        # pattern: blend_name + "_" + 8 digits + "_" + 6 digits
        pattern = r"^" + re.escape(blend_name) + r"_\d{8}_\d{6}$"
        self.assertRegex(folder_name, pattern)


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
