import shutil
import sys
import unittest
import os
from pathlib import Path
import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import core

class TestRescueCleanup(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_rescue_cleanup_env"
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

        # Save current blend file there
        self.blend_path = self.test_dir / "test.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

        savepoints.register()

    def tearDown(self):
        savepoints.unregister()
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_cleanup_on_append_error(self):
        """
        Verify that snapshot_rescue_temp.blend is removed if wm.append fails (or any error occurs after creation).
        """
        print("\n--- Test Rescue Cleanup on Error ---")
        version_id = "v001"
        history_dir = self.test_dir / ".test_history"
        version_dir = history_dir / version_id
        version_dir.mkdir(parents=True)

        snapshot_path = version_dir / "snapshot.blend_snapshot"
        # Create a valid blend file as snapshot
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)
        
        temp_blend_path = version_dir / "snapshot_rescue_temp.blend"
        
        # Ensure temp file doesn't exist initially
        self.assertFalse(temp_blend_path.exists(), "Temp file should not exist before op")

        print("Running rescue_assets (expecting failure in headless mode)...")
        try:
            # This is expected to fail in headless mode either at context finding or wm.append
            # Because we are running in background, wm.append likely raises RuntimeError or Operator fails finding context
            bpy.ops.savepoints.rescue_assets(version_id=version_id)
        except RuntimeError as e:
            print(f"Caught expected error: {e}")
            pass
        
        # KEY ASSERTION: Temp file must NOT exist
        # Because we implemented cleanup_on_error
        if temp_blend_path.exists():
            self.fail(f"Cleanup failed! Temp file still exists at: {temp_blend_path}")
        else:
            print("SUCCESS: Temp file was cleaned up.")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
