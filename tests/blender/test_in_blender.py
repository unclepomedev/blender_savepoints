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

from savepoints.services.storage import get_parent_path_from_snapshot
from savepoints_test_case import SavePointsTestCase


class TestInBlenderE2E(SavePointsTestCase):

    def test_e2e_flow_scenario(self):
        """
        Scenario:
        1. Commit a new version (creates v001).
        2. Checkout that version (enters Snapshot Mode).
        3. Verify safeguards (Commit should be blocked in Snapshot Mode).
        4. Restore (Merge changes back to Parent File).
        """
        print("Starting E2E Flow Scenario...")

        # Base setup (setUp) already created test_project.blend
        history_dir = self.test_dir / ".test_project_history"

        # --- Step 1: Commit ---
        with self.subTest(step="1. Commit Version"):
            print("Testing Commit...")

            # Create data to verify persistence later
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = "TestCube_v1"

            # Execute Commit (Bypass dialog)
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="First Version")
            self.assertIn('FINISHED', res, "Commit failed")

            # Verify Filesystem Structure
            self.assertTrue(history_dir.exists(), "History directory not created")
            self.assertTrue((history_dir / "manifest.json").exists(), "Manifest not created")

            v001_dir = history_dir / "v001"
            self.assertTrue(v001_dir.exists(), "Version v001 folder not created")
            self.assertTrue((v001_dir / "snapshot.blend_snapshot").exists(), "Snapshot file not created")

        # --- Step 2: Checkout ---
        with self.subTest(step="2. Checkout Snapshot"):
            print("Testing Checkout...")

            # Modify current scene BEFORE checkout (to ensure it gets discarded)
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.object.name = "TransientSphere"

            # Set active index to 0 (v001)
            if hasattr(bpy.context.scene, "savepoints_settings"):
                bpy.context.scene.savepoints_settings.active_version_index = 0

            # Execute Checkout
            res = bpy.ops.savepoints.checkout()
            self.assertIn('FINISHED', res, "Checkout failed")

            # Verify Loaded File
            current_path = Path(bpy.data.filepath)
            self.assertEqual(current_path.name, "snapshot.blend_snapshot",
                             f"Failed to load snapshot file. Current: {current_path}")

            # Verify Content
            self.assertIn("TestCube_v1", bpy.data.objects, "Snapshot missing original data")
            self.assertNotIn("TransientSphere", bpy.data.objects,
                             "Snapshot contains data that should have been discarded")

            # Verify Snapshot Mode Detection
            parent_path_detected = get_parent_path_from_snapshot(bpy.data.filepath)
            self.assertIsNotNone(parent_path_detected, "Snapshot Mode not detected internally")
            self.assertEqual(Path(parent_path_detected), self.blend_path, "Parent path mismatch")

        # --- Step 3: Commit Guard (Restriction Test) ---
        with self.subTest(step="3. Verify Commit Guard"):
            print("Testing Commit Guard (Should fail in Snapshot Mode)...")

            # Attempting to commit inside a snapshot should fail (Poll fails -> RuntimeError in headless)
            with self.assertRaises(RuntimeError):
                bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Illegal Commit")

        # --- Step 4: Restore ---
        with self.subTest(step="4. Restore to Parent"):
            print("Testing Restore...")

            # Add something new in the snapshot to verify it merges back to parent
            bpy.ops.mesh.primitive_cone_add()
            bpy.context.object.name = "RestoredCone"

            # Execute Restore
            res = bpy.ops.savepoints.restore('EXEC_DEFAULT')
            self.assertIn('FINISHED', res, "Restore failed")

            # Verify Filepath (Should be back to original)
            current_path = Path(bpy.data.filepath)
            self.assertEqual(current_path.name, "test_project.blend",
                             f"Failed to return to parent file. Current: {current_path}")

            # Verify Content
            self.assertIn("RestoredCone", bpy.data.objects, "Restored file missing object added during snapshot")
            self.assertIn("TestCube_v1", bpy.data.objects, "Restored file missing original data")

            # Verify Backup Creation (Safety feature)
            # Look for *.bak files in history dir
            backups = list(history_dir.glob("test_project.blend.*.bak"))
            self.assertTrue(len(backups) > 0, "Backup file was not created during restore")

        print("E2E Flow Scenario: Completed")


if __name__ == '__main__':
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
