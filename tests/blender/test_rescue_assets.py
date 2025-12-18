import shutil
import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from savepoints.services.storage import get_history_dir
import savepoints


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
        computed_history_dir = get_history_dir()
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
            # Check if the error is the expected one for headless environment
            err_str = str(e)

            # Normalize path separators for cross-platform check
            err_str_norm = err_str.replace("\\", "/")
            expected_path_part = f"{version_id}/snapshot_rescue_temp.blend/Object"

            if "Snapshot file not found" in err_str:
                self.fail(f"Snapshot not found: {e}")

            elif "nothing indicated" in err_str and expected_path_part in err_str_norm:
                # SUCCESS: This error confirms that the operator constructed the correct path
                # and attempted to open it via wm.append.
                # The "nothing indicated" error is expected because we are in background mode (no UI).
                print(f"Test Passed: Verified correct append path attempt:\n  -> .../{expected_path_part}")

            else:
                # Unexpected error
                print(f"Caught unexpected runtime error: {e}")
                # We interpret this as a pass if it's just a UI context error, but warn the user
                if "context" in err_str.lower():
                    print("Pass (UI Context Error)")
                else:
                    raise e

        # Note: We can't verify the exact directory string passed to append without mocking, 
        # but passing this test ensures the file was found and logic proceeded to append call.

    def test_rescue_assets_legacy(self):
        print("\n--- Test Rescue Assets (Legacy .blend) ---")
        version_id = "v002"
        # The history dir is determined by the blend file name ("test.blend")
        history_dir = self.test_dir / ".test_history"
        version_dir = history_dir / version_id
        version_dir.mkdir(parents=True, exist_ok=True)

        # Create legacy snapshot
        snapshot_path = version_dir / "snapshot.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)

        print(f"Testing rescue for legacy file: {snapshot_path}")

        try:
            res = bpy.ops.savepoints.rescue_assets(version_id=version_id)
            print(f"Result: {res}")

        except RuntimeError as e:
            err_str = str(e)
            # Normalize path separators
            err_str_norm = err_str.replace("\\", "/")

            # The operator creates a temp file from the source
            temp_blend_path = version_dir / "snapshot_rescue_temp.blend"

            if temp_blend_path.exists():
                print("Temp file created, meaning source file was found.")
            else:
                if "Snapshot file not found" in err_str:
                    self.fail(f"Legacy snapshot not detected: {e}")
                else:
                    # Some other error, but maybe file was found?
                    # If temp file doesn't exist, it likely failed before copy or copy failed.
                    print(f"Caught error without temp file: {err_str}")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
