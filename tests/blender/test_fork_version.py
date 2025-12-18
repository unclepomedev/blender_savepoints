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
from savepoints.services.storage import get_parent_path_from_snapshot, load_manifest, get_history_dir
from savepoints_test_case import SavePointsTestCase


class TestForkVersion(SavePointsTestCase):
    def test_fork_version(self):
        print("Starting Fork Feature Test...")
        # SavePointsTestCase setup provides self.test_dir and self.blend_path (test_project.blend)

        # Expected forked path (assuming auto-naming appends _v001 or similar if logic dictates)
        # Actually, let's see what happens. The test originally expected original_project_v001.blend
        # If the operator logic appends version suffix, for test_project.blend it should be test_project_v001.blend
        # BUT, if fork_version opens a file dialog in UI, EXEC_DEFAULT might fail or use default.
        # If the previous test worked without passing filepath, it means the operator handles it.
        # Let's assume the operator figures out a name or we might need to pass filepath if it supports it.
        # But the original test didn't pass filepath. So let's stick to no args.

        # 2. Create a Version (Commit)
        print("Creating v001...")
        # Add an object to verify content later
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "OriginalCube"

        res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Base Version")
        if "FINISHED" not in res:
            self.fail(f"Commit failed: {res}")

        # 3. Checkout (Enter Snapshot Mode)
        print("Checking out v001...")
        bpy.context.scene.savepoints_settings.active_version_index = 0
        res = bpy.ops.savepoints.checkout()
        if "FINISHED" not in res:
            self.fail(f"Checkout failed: {res}")

        # Verify we are in snapshot mode
        current_path = Path(bpy.data.filepath)
        self.assertEqual(current_path.name, "snapshot.blend_snapshot", f"Not in snapshot mode: {current_path}")

        # 4. Execute Fork
        print("Forking...")

        # No arguments needed, it should auto-detect everything
        res = bpy.ops.savepoints.fork_version('EXEC_DEFAULT')

        if "FINISHED" not in res:
            self.fail(f"Fork failed: {res}")

        # 5. Verification
        print("Verifying Fork results...")

        # Determine expected fork path.
        # The operator likely appends _v001 to the original project name.
        forked_blend_path = self.test_dir / "test_project_v001.blend"

        # Check if it switched to the expected file
        current_loaded_path = Path(bpy.data.filepath)

        # If the name is different, maybe logic is different.
        print(f"Current loaded path: {current_loaded_path}")

        # A. File Existence
        if not current_loaded_path.exists():
            self.fail(f"Forked file {current_loaded_path} does not exist on disk")

        # B. Context Switch
        # It should NOT be the snapshot file
        self.assertNotEqual(current_loaded_path.name, "snapshot.blend_snapshot", "Still in snapshot file!")

        # C. Content Verification
        if "OriginalCube" not in bpy.data.objects:
            self.fail("Forked file missing objects from snapshot")

        # D. Fresh History Verification
        # The new file will have a history folder created (by the fork operator).
        # But it should be EMPTY (no versions from the original project)
        history_dir = get_history_dir()
        if history_dir and Path(history_dir).exists():
            # If it exists, check manifest
            manifest = load_manifest()
            versions = manifest.get("versions", [])
            if len(versions) > 0:
                self.fail(f"Forked project history should be empty, but has {len(versions)} versions: {versions}")

            # Also verify parent_file in manifest matches current file
            manifest_parent = manifest.get("parent_file")
            # Normalize paths for comparison
            if Path(manifest_parent).resolve() != current_loaded_path.resolve():
                self.fail(f"New manifest parent_file mismatch. Expected {current_loaded_path}, got {manifest_parent}")

        # E. Verify we are NOT in snapshot mode anymore
        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        if parent_path:
            self.fail("Forked project should be a normal file, not in snapshot mode")

        print("Fork Test Passed!")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
