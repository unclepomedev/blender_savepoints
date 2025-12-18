import sys
import unittest
from pathlib import Path

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.asset_path import unmap_snapshot_paths
from savepoints_test_case import SavePointsTestCase


class TestUnmapSnapshotPaths(SavePointsTestCase):
    def test_unmap_returns_false_if_no_changes(self):
        # Ensure no existing weird paths
        changed = unmap_snapshot_paths()
        self.assertFalse(changed, "Should return False when no paths need fixing")

    def test_unmap_returns_true_if_changes_made(self):
        # Create a dummy image with snapshot path
        img = bpy.data.images.new("TestImage", width=10, height=10)
        original_path = "//../../textures/test.png"
        img.filepath = original_path

        # Verify setup
        self.assertEqual(img.filepath, original_path)

        # Run unmap
        changed = unmap_snapshot_paths()

        # Verify
        self.assertTrue(changed, "Should return True when path fixed")
        self.assertEqual(img.filepath, "//textures/test.png")

        # Cleanup (SavePointsTestCase cleans up session anyway, but explicit is fine)
        bpy.data.images.remove(img)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
