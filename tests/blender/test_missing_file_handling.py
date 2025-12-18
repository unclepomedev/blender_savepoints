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

from savepoints_test_case import SavePointsTestCase


class TestMissingFileHandling(SavePointsTestCase):
    def test_missing_file_handling(self):
        print("Starting Missing File Handling Test...")
        # SavePointsTestCase setup provides self.test_dir and self.blend_path (test_project.blend)

        # 3. Create a version
        print("Creating version v001...")
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="To be broken")

        # 4. Verify creation
        history_dir = self.test_dir / ".test_project_history"
        snapshot_path = history_dir / "v001" / "snapshot.blend_snapshot"
        self.assertTrue(snapshot_path.exists(), "Setup failed: Snapshot file was not created.")

        # 5. Sabotage: Delete the snapshot file
        print("Sabotaging: Deleting snapshot file...")
        snapshot_path.unlink()

        # 6. Attempt Checkout
        print("Attempting Checkout on missing file...")
        bpy.context.scene.savepoints_settings.active_version_index = 0

        # We expect this operator to report an ERROR and return CANCELLED.
        # In scripting, this often raises a RuntimeError.
        try:
            res = bpy.ops.savepoints.checkout('EXEC_DEFAULT')
            # If it didn't raise, check if it returned CANCELLED (though usually it raises)
            if 'CANCELLED' in res:
                print("Checkout was correctly CANCELLED (via return value).")
            else:
                self.fail(f"Checkout should have been CANCELLED but returned: {res}")
        except RuntimeError as e:
            # Check if the error message is what we expect
            if "File not found" in str(e):
                print("Checkout was correctly CANCELLED (via RuntimeError).")
            else:
                raise e

        # 7. Verify we are NOT in snapshot mode (file path should still be original or safe)
        # Because the open_mainfile failed, we should still be at test_project.blend
        current_path = Path(bpy.data.filepath)
        print(f"Current filepath after failure: {current_path}")

        self.assertEqual(current_path, self.blend_path, f"Safety check failed: Filepath changed to {current_path}")

        print("Missing File Handling Test: PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
