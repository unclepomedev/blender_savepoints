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

from savepoints.services.asset_path import unmap_snapshot_paths
from savepoints_test_case import SavePointsTestCase


class TestUnmapSnapshotPaths(SavePointsTestCase):

    def test_unmap_paths_scenario(self):
        """
        Scenario:
        1. Clean State: Verify function returns False when no paths need fixing.
        2. Apply Fix: Create an image with a snapshot-style relative path (//../../)
           and verify the function fixes it and returns True.
        3. Idempotency: Verify that running the function again on the fixed path
           returns False and does not alter the path further.
        """
        print("Starting Unmap Snapshot Paths Scenario...")

        # --- Step 1: Clean State ---
        with self.subTest(step="1. Clean State"):
            changed = unmap_snapshot_paths()
            self.assertFalse(changed, "Should return False when no paths need fixing")

        # --- Step 2: Apply Fix ---
        with self.subTest(step="2. Apply Fix"):
            # Setup: Create a dummy image with a broken/deep relative path
            # Simulating a file that was saved in a subdir and then opened in root
            img = bpy.data.images.new("TestImage", width=10, height=10)
            original_path = "//../../textures/test.png"
            img.filepath = original_path

            # Verify setup assumption
            self.assertEqual(img.filepath, original_path)

            # Execute
            changed = unmap_snapshot_paths()

            # Verify
            self.assertTrue(changed, "Should return True when modifications are made")

            # Expected: The deep relative part is removed/flattened
            expected_path = "//textures/test.png"
            self.assertEqual(img.filepath, expected_path,
                             f"Path mismatch. Expected '{expected_path}', got '{img.filepath}'")

        # --- Step 3: Idempotency (Stability Check) ---
        with self.subTest(step="3. Idempotency"):
            print("Verifying idempotency...")
            # Run it again immediately
            changed = unmap_snapshot_paths()

            self.assertFalse(changed, "Running on already fixed paths should return False")

            # Ensure path wasn't mangled by double execution
            img = bpy.data.images.get("TestImage")
            self.assertEqual(img.filepath, "//textures/test.png", "Path should remain stable after re-run")

        print("Unmap Snapshot Paths Scenario: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
