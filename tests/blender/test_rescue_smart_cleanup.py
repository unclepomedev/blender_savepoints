import unittest
import bpy
import os
import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from savepoints import core

class TestUnmapSnapshotPaths(unittest.TestCase):
    def test_unmap_returns_false_if_no_changes(self):
        # Ensure no existing weird paths
        changed = core.unmap_snapshot_paths()
        self.assertFalse(changed, "Should return False when no paths need fixing")

    def test_unmap_returns_true_if_changes_made(self):
        # Create a dummy image with snapshot path
        img = bpy.data.images.new("TestImage", width=10, height=10)
        original_path = "//../../textures/test.png"
        img.filepath = original_path
        
        # Verify setup
        self.assertEqual(img.filepath, original_path)
        
        # Run unmap
        changed = core.unmap_snapshot_paths()
        
        # Verify
        self.assertTrue(changed, "Should return True when path fixed")
        self.assertEqual(img.filepath, "//textures/test.png")
        
        # Cleanup
        bpy.data.images.remove(img)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
