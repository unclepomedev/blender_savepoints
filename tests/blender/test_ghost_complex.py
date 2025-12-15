import os
import shutil
import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import core


class TestGhostComplex(unittest.TestCase):
    def setUp(self):
        self.test_dir = ROOT / "test_ghost_complex_env"
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

        # Save current blend file
        self.blend_path = self.test_dir / "test_complex.blend"
        # Reset Blender to clean state
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

        savepoints.register()

    def tearDown(self):
        try:
            savepoints.unregister()
        except Exception:
            pass
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_multiple_ghosts_and_missing_file(self):
        print("\n--- Test: Multiple Ghosts & Missing File ---")

        # --- PREPARATION ---
        # Create v001 with Cube at (0,0,0)
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
        cube = bpy.context.active_object
        cube.name = "Cube_V1"
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v1")
        v1_id = "v001"

        # Create v002 with Cube at (5,0,0)
        # Move cube
        cube.location.x = 5.0
        cube.name = "Cube_V2"  # Rename to distinguish easily
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v2")
        v2_id = "v002"

        # Create v003 then delete it for missing file test
        cube.location.x = 10.0
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="v3")
        v3_id = "v003"

        # --- SCENARIO 1: Multiple Ghosts ---
        print("1. Activating Ghost v1...")
        bpy.ops.savepoints.toggle_ghost(version_id=v1_id)

        print("2. Activating Ghost v2...")
        bpy.ops.savepoints.toggle_ghost(version_id=v2_id)

        # Verify both collections exist
        col_v1 = bpy.data.collections.get(f"Ghost_Reference_{v1_id}")
        col_v2 = bpy.data.collections.get(f"Ghost_Reference_{v2_id}")

        self.assertIsNotNone(col_v1, "Ghost v1 collection should exist")
        self.assertIsNotNone(col_v2, "Ghost v2 collection should exist")

        # Verify libraries loaded
        # We expect at least 2 libraries (one for each snapshot)
        # Filter libraries that point to our snapshots
        snapshot_libs = [
            lib for lib in bpy.data.libraries
            if "snapshot.blend_snapshot" in lib.filepath
        ]
        self.assertGreaterEqual(len(snapshot_libs), 2, "Should have at least 2 snapshot libraries loaded")

        print(f"Loaded snapshot libraries: {[l.filepath for l in snapshot_libs]}")

        # --- SCENARIO 2: Selective Removal ---
        print("3. Removing Ghost v1...")
        bpy.ops.savepoints.toggle_ghost(version_id=v1_id)

        # Verify v1 gone
        self.assertIsNone(bpy.data.collections.get(f"Ghost_Reference_{v1_id}"), "Ghost v1 should be gone")

        # Verify v2 STILL exists
        self.assertIsNotNone(bpy.data.collections.get(f"Ghost_Reference_{v2_id}"), "Ghost v2 should still exist")

        # Verify v1 library is cleaned up, v2 library remains
        libs_v1 = [l for l in bpy.data.libraries if f"/{v1_id}/" in l.filepath.replace("\\", "/")]
        libs_v2 = [l for l in bpy.data.libraries if f"/{v2_id}/" in l.filepath.replace("\\", "/")]

        self.assertEqual(len(libs_v1), 0, "Ghost v1 library should be cleaned up")
        self.assertGreater(len(libs_v2), 0, "Ghost v2 library should remain")

        print("Selective removal passed.")

        # Cleanup v2
        bpy.ops.savepoints.toggle_ghost(version_id=v2_id)
        self.assertIsNone(bpy.data.collections.get(f"Ghost_Reference_{v2_id}"))

        # --- SCENARIO 3: Missing Snapshot File ---
        print("4. Testing Missing Snapshot File...")

        # Manually delete the snapshot file for v3
        # Manually delete the snapshot file for v3
        history_dir = core.get_history_dir()
        self.assertIsNotNone(history_dir, "History directory should exist after commits")
        v3_path = Path(history_dir) / v3_id / "snapshot.blend_snapshot"
        if v3_path.exists():
            os.remove(v3_path)

        # Try to toggle ghost
        try:
            bpy.ops.savepoints.toggle_ghost(version_id=v3_id)
            self.fail("Operator should have failed (CANCELLED) due to missing file")
        except RuntimeError as e:
            print(f"Caught expected error: {e}")
            # In headless, CANCELLED raises RuntimeError.
            # Ideally we check the message if possible, but RuntimeError usually just says "Operator failed..."
            pass

        # Ensure no garbage collection created
        self.assertIsNone(bpy.data.collections.get(f"Ghost_Reference_{v3_id}"),
                          "No collection should be created for missing file")

        print("Complex Ghost Test Passed.")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
