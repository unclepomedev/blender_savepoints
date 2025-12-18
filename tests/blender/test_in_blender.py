import sys
import unittest
from pathlib import Path

import bpy

from savepoints.services.storage import get_parent_path_from_snapshot
# Add project root to sys.path
from savepoints_test_case import SavePointsTestCase


class TestInBlenderE2E(SavePointsTestCase):
    def test_e2e_flow(self):
        print("\n--- Starting E2E Test ---")

        # Base setup (setUp) already created test_project.blend and registered addon
        # history_dir will be based on test_project.blend
        history_dir = self.test_dir / ".test_project_history"

        # 3. Test Commit
        print("Testing Commit...")
        # Create some data to verify later
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "TestCube_v1"

        # EXEC_DEFAULT to bypass invoke_props_dialog
        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="First Version")
        if "FINISHED" not in res:
            self.fail(f"Commit failed with result: {res}")

        # Verify filesystem
        if not history_dir.exists():
            self.fail("History directory not created")

        manifest_path = history_dir / "manifest.json"
        if not manifest_path.exists():
            self.fail("Manifest not created")

        v001_dir = history_dir / "v001"
        if not v001_dir.exists():
            self.fail("Version v001 folder not created")

        snapshot_path = v001_dir / "snapshot.blend_snapshot"
        if not snapshot_path.exists():
            self.fail("Snapshot file not created")

        print("Commit Verification: OK")

        # 4. Test Checkout
        print("Testing Checkout...")
        # Modify current scene so we know if we switched
        bpy.ops.mesh.primitive_uv_sphere_add()
        bpy.context.object.name = "TransientSphere"

        # Set active index to 0 (v001)
        bpy.context.scene.savepoints_settings.active_version_index = 0

        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            self.fail(f"Checkout failed with result: {res}")

        # Verify loaded file
        current_path = Path(bpy.data.filepath)
        if current_path.name != "snapshot.blend_snapshot":
            self.fail(f"Checkout did not load snapshot.blend_snapshot, current: {current_path}")

        # Verify content (should have TestCube_v1, but NOT TransientSphere)
        if "TestCube_v1" not in bpy.data.objects:
            self.fail("Snapshot does not contain TestCube_v1")
        if "TransientSphere" in bpy.data.objects:
            self.fail("Snapshot contains TransientSphere (should have been discarded)")

        # Verify Snapshot Mode
        parent_path_detected = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path_detected:
            self.fail("Snapshot Mode not detected (get_parent_path_from_snapshot returned None)")

        if Path(parent_path_detected) != self.blend_path:
            self.fail(f"Parent path mismatch: {parent_path_detected} vs {self.blend_path}")

        # Verify Commit Guard (should fail in snapshot mode)
        print("Testing Commit Guard...")
        try:
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Illegal Commit")
            self.fail("Commit should have failed in snapshot mode but succeeded")
        except RuntimeError:
            # Expected failure: poll() failed
            print("Commit blocked as expected.")
        except Exception as e:
            self.fail(f"Unexpected error during commit guard test: {e}")

        print("Checkout Verification: OK")

        # 5. Test Restore (Save as Parent)
        print("Testing Restore...")

        # Add something new in the snapshot to verify it gets saved to parent
        bpy.ops.mesh.primitive_cone_add()
        bpy.context.object.name = "RestoredCone"

        # EXEC_DEFAULT to bypass confirmation
        res = bpy.ops.savepoints.restore('EXEC_DEFAULT')
        if "FINISHED" not in res:
            self.fail(f"Restore failed with result: {res}")

        # Verify filepath is back to original
        current_path = Path(bpy.data.filepath)
        if current_path.name != "test_project.blend":
            self.fail(f"Restore did not switch back to original file, current: {current_path}")

        # Verify content
        if "RestoredCone" not in bpy.data.objects:
            self.fail("Restored file does not contain the new object added in snapshot")

        # Verify Backup
        backups = list(history_dir.glob("test_project.blend.*.bak"))
        if not backups:
            self.fail("Backup file was not created in history folder")

        print("Restore Verification: OK")


if __name__ == '__main__':
    res = unittest.main(argv=[''], exit=False)
    if not res.result.wasSuccessful():
        sys.exit(1)
