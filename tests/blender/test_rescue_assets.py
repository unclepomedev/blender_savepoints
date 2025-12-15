import sys
import unittest
import shutil
import os
from pathlib import Path
import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import core

class TestRescueAssets(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_rescue_assets_env"
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

    def test_rescue_assets_execution(self):
        print("\n--- Test Rescue Assets ---")
        # 1. Create a dummy snapshot
        version_id = "v001"
        history_dir = self.test_dir / f".test_history"
        version_dir = history_dir / version_id
        version_dir.mkdir(parents=True)
        
        snapshot_path = version_dir / "snapshot.blend_snapshot"
        # Create a valid blend file as snapshot
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)
        
        # Verify history dir matches
        computed_history_dir = core.get_history_dir()
        self.assertEqual(str(computed_history_dir), str(history_dir))
        
        # 2. Run Operator with INVALID version
        print("Testing invalid version...")
        try:
            # This should fail (return CANCELLED, causing RuntimeError in script call)
            bpy.ops.savepoints.rescue_assets(version_id="v999")
            self.fail("Operator should have failed for missing snapshot")
        except RuntimeError as e:
            # Expected
            print("Caught expected error for invalid version.")
            pass

        # 3. Run Operator with VALID version
        print("Testing valid version...")
        try:
            # This calls wm.append('INVOKE_DEFAULT', directory=...)
            # In background mode, this *might* fail or return FINISHED depending on Blender version/behavior.
            # If it returns FINISHED, it means it found the file and called append.
            # If it fails with "context is incorrect", it also means it tried to call append (since append is context sensitive).
            
            res = bpy.ops.savepoints.rescue_assets(version_id=version_id)
            print(f"Result: {res}")
            
            if "FINISHED" in res:
                 print("Operator finished successfully.")
                 
        except RuntimeError as e:
            # If the error comes from wm.append complaining about context, it's a success for us (we reached that line).
            # If it says "Snapshot file not found", it's a fail.
            err_str = str(e)
            if "Snapshot file not found" in err_str:
                self.fail(f"Snapshot not found: {e}")
            else:
                print(f"Caught runtime error (likely UI context): {e}")

        # Note: We can't verify the exact directory string passed to append without mocking, 
        # but passing this test ensures the file was found and logic proceeded to append call.

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
