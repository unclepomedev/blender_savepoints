import os
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

from savepoints.services.storage import get_history_dir
from savepoints_test_case import SavePointsTestCase


class TestGhostComplex(SavePointsTestCase):

    def test_ghost_complex_scenario(self):
        """
        Scenario:
        1. Prepare history with 3 versions (v1, v2, v3).
        2. Activate Multiple Ghosts (v1 and v2) simultaneously and verify independence.
        3. Selectively remove one Ghost (v1) while keeping the other (v2).
        4. Test error handling when attempting to load a Ghost for a deleted snapshot (v3).
        """
        print("Starting Complex Ghost Scenario...")

        # Variables to store IDs across sub-tests
        v1_id = "v001"
        v2_id = "v002"
        v3_id = "v003"

        col_name_v1 = f"Ghost_Reference_{v1_id}"
        col_name_v2 = f"Ghost_Reference_{v2_id}"
        col_name_v3 = f"Ghost_Reference_{v3_id}"

        # --- Step 1: Preparation ---
        with self.subTest(step="1. Preparation"):
            print("Creating versions...")

            # Create v1 (Cube at 0,0,0)
            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            cube = bpy.context.active_object
            cube.name = "Cube_V1"
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v1")

            # Create v2 (Cube moved to 5,0,0)
            cube.location.x = 5.0
            cube.name = "Cube_V2"
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v2")

            # Create v3 (Cube moved to 10,0,0)
            cube.location.x = 10.0
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v3")

            # Verify history created
            history_dir = get_history_dir()
            self.assertIsNotNone(history_dir, "History directory missing")

        # --- Step 2: Multiple Ghosts Activation ---
        with self.subTest(step="2. Multiple Ghosts"):
            print("Activating Ghosts v1 and v2...")

            bpy.ops.savepoints.toggle_ghost(version_id=v1_id)
            bpy.ops.savepoints.toggle_ghost(version_id=v2_id)

            # Verify Collections
            self.assertIn(col_name_v1, bpy.data.collections, "Ghost v1 collection missing")
            self.assertIn(col_name_v2, bpy.data.collections, "Ghost v2 collection missing")

            # Verify Libraries
            # We filter libraries to find those pointing to our snapshots
            snapshot_libs = [
                lib for lib in bpy.data.libraries
                if "snapshot.blend_snapshot" in lib.filepath
            ]
            self.assertGreaterEqual(len(snapshot_libs), 2, "Should have at least 2 snapshot libraries loaded")

        # --- Step 3: Selective Removal ---
        with self.subTest(step="3. Selective Removal"):
            print("Removing Ghost v1...")

            # Toggle off v1
            bpy.ops.savepoints.toggle_ghost(version_id=v1_id)

            # Verify v1 is gone
            self.assertNotIn(col_name_v1, bpy.data.collections, "Ghost v1 collection should be gone")

            # Verify v2 is STILL there
            self.assertIn(col_name_v2, bpy.data.collections, "Ghost v2 collection should still exist")

            # Verify Library Cleanup
            libs_v1 = [l for l in bpy.data.libraries if f"/{v1_id}/" in l.filepath.replace("\\", "/")]
            libs_v2 = [l for l in bpy.data.libraries if f"/{v2_id}/" in l.filepath.replace("\\", "/")]

            self.assertEqual(len(libs_v1), 0, "Ghost v1 library should be cleaned up")
            self.assertGreater(len(libs_v2), 0, "Ghost v2 library should remain")

            # Cleanup v2 for next step
            bpy.ops.savepoints.toggle_ghost(version_id=v2_id)
            self.assertNotIn(col_name_v2, bpy.data.collections)

        # --- Step 4: Missing File Handling ---
        with self.subTest(step="4. Missing Snapshot File"):
            print("Testing Missing Snapshot File...")

            # Manually delete v3 file
            history_dir = get_history_dir()
            v3_path = Path(history_dir) / v3_id / "snapshot.blend_snapshot"

            if v3_path.exists():
                os.remove(v3_path)
            else:
                self.fail("Test setup failed: v3 snapshot file missing before deletion")

            # Attempt to toggle ghost for missing file
            # In headless mode, operator failure raises RuntimeError
            with self.assertRaises(RuntimeError):
                bpy.ops.savepoints.toggle_ghost(version_id=v3_id)

            # Ensure no garbage collection was created
            self.assertNotIn(col_name_v3, bpy.data.collections, "No collection should be created for missing file")

        print("Complex Ghost Scenario: Completed")


if __name__ == '__main__':
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
