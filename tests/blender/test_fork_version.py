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

from savepoints.services.storage import get_parent_path_from_snapshot, load_manifest, get_history_dir
from savepoints_test_case import SavePointsTestCase


class TestForkVersion(SavePointsTestCase):

    def test_fork_version_scenario(self):
        """
        Scenario:
        1. Create a version with specific content (Cube).
        2. Checkout that version (enter Snapshot Mode).
        3. Execute 'Fork Version' to branch off into a new separate project file.
        4. Verify the new file exists, contains the content, and has a fresh (empty) history.
        """
        print("Starting Fork Version Scenario...")

        # --- Step 1: Create Base Version ---
        with self.subTest(step="1. Create Base Version"):
            print("Creating v001 with content...")

            # Add content to verify persistence later
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = "OriginalCube"

            # Commit
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Base Version")
            self.assertIn('FINISHED', res, "Commit failed")

        # --- Step 2: Checkout (Enter Snapshot Mode) ---
        with self.subTest(step="2. Checkout Snapshot"):
            print("Checking out v001...")

            # Set active index to 0 (v001)
            bpy.context.scene.savepoints_settings.active_version_index = 0

            res = bpy.ops.savepoints.checkout()
            self.assertIn('FINISHED', res, "Checkout failed")

            # Verify we are physically in the snapshot file
            current_path = Path(bpy.data.filepath)
            self.assertEqual(current_path.name, "snapshot.blend_snapshot", f"Not in snapshot mode: {current_path}")

        # --- Step 3: Execute Fork ---
        with self.subTest(step="3. Execute Fork"):
            print("Executing Fork...")

            # Fork operator should handle file naming automatically (e.g., test_project_v001.blend)
            res = bpy.ops.savepoints.fork_version('EXEC_DEFAULT')
            self.assertIn('FINISHED', res, "Fork operator failed")

        # --- Step 4: Verification (File & Content) ---
        with self.subTest(step="4. Verify Forked File"):
            print("Verifying Fork results...")

            current_loaded_path = Path(bpy.data.filepath)
            print(f"Current loaded path: {current_loaded_path}")

            # A. File Existence & Context Switch
            self.assertTrue(current_loaded_path.exists(), "Forked file does not exist on disk")
            self.assertNotEqual(current_loaded_path.name, "snapshot.blend_snapshot",
                                "Blender is still opening the snapshot file!")

            # The operator typically appends suffix like '_v001' to the original name
            self.assertIn("test_project", current_loaded_path.name, "Filename seems unrelated to original project")

            # B. Content Verification (Did the Cube survive?)
            self.assertIn("OriginalCube", bpy.data.objects, "Forked file missing objects from snapshot")

            # C. Snapshot Mode Check (Should be FALSE)
            parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
            self.assertIsNone(parent_path, "Forked project should be a normal file, but is detected as Snapshot Mode")

        # --- Step 5: Verification (History Reset) ---
        with self.subTest(step="5. Verify Fresh History"):
            print("Verifying History is Clean...")

            history_dir = get_history_dir()

            # If history dir exists, verify it's valid and clean for the new file
            if history_dir and Path(history_dir).exists():
                manifest = load_manifest()

                # A. History should be empty (New project starts fresh)
                versions = manifest.get("versions", [])
                self.assertEqual(len(versions), 0,
                                 f"Forked project history should be empty, but has {len(versions)} versions")

                # B. Parent pointer should point to ITSELF (Current file)
                manifest_parent = manifest.get("parent_file")
                self.assertEqual(
                    Path(manifest_parent).resolve(),
                    current_loaded_path.resolve(),
                    "New manifest 'parent_file' mismatch"
                )

        print("Fork Version Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
