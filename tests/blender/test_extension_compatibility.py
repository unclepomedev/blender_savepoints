import json
import shutil
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
from savepoints.services.storage import get_parent_path_from_snapshot
from savepoints_test_case import SavePointsTestCase


class TestExtensionCompatibility(SavePointsTestCase):
    def create_manual_history(self):
        """
        Manually create a history structure with mixed extensions.
        v001 -> snapshot.blend (Old format)
        v002 -> snapshot.blend_snapshot (New format)
        """
        # Using self.blend_path which is "test_project.blend"
        history_dir = self.test_dir / ".test_project_history"
        history_dir.mkdir()

        # Create v001 (Old format: .blend)
        v001_dir = history_dir / "v001"
        v001_dir.mkdir()
        shutil.copy2(self.blend_path, v001_dir / "snapshot.blend")

        # Create v002 (New format: .blend_snapshot)
        v002_dir = history_dir / "v002"
        v002_dir.mkdir()
        shutil.copy2(self.blend_path, v002_dir / "snapshot.blend_snapshot")

        # Create manifest.json
        manifest = {
            "parent_file": str(self.blend_path),
            "versions": [
                {
                    "id": "v001",
                    "note": "Old Format",
                    "timestamp": "1234567890",
                    "thumbnail": "v001/thumbnail.png",
                    "blend": "v001/snapshot.blend",
                    "object_count": 1,
                    "file_size": 1024
                },
                {
                    "id": "v002",
                    "note": "New Format",
                    "timestamp": "1234567891",
                    "thumbnail": "v002/thumbnail.png",
                    "blend": "v002/snapshot.blend_snapshot",
                    "object_count": 1,
                    "file_size": 1024
                }
            ]
        }

        with open(history_dir / "manifest.json", "w") as f:
            json.dump(manifest, f, indent=4)

    def test_extension_compatibility(self):
        print("Starting Extension Compatibility Test...")
        # SavePointsTestCase creates test_project.blend and registers addon

        # 3. Create Manual History (Mixed extensions)
        print("Creating manual history with mixed extensions...")
        self.create_manual_history()

        # Refresh to load manifest
        bpy.ops.savepoints.refresh()

        # Verify settings loaded
        settings = bpy.context.scene.savepoints_settings
        self.assertEqual(len(settings.versions), 2, f"Expected 2 versions, found {len(settings.versions)}")

        # 4. Test Checkout Old Format (.blend)
        print("Testing Checkout v001 (.blend)...")
        settings.active_version_index = 0  # v001

        bpy.ops.savepoints.checkout()

        current_path = Path(bpy.data.filepath)
        print(f"Current path after checkout: {current_path}")

        self.assertEqual(current_path.name, "snapshot.blend",
                         f"Failed to checkout old format. Expected snapshot.blend, got {current_path.name}")

        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        self.assertTrue(parent_path, "Snapshot mode not detected for .blend file")
        if Path(parent_path) != self.blend_path:
            self.fail(f"Incorrect parent path detected: {parent_path}")

        print("v001 (.blend) Verification: OK")

        # 5. Return to Parent (to be clean, though checkout handles switching)
        print("Returning to parent...")
        bpy.ops.savepoints.open_parent()
        if Path(bpy.data.filepath) != self.blend_path:
            self.fail("Failed to return to parent file")

        # 6. Test Checkout New Format (.blend_snapshot)
        print("Testing Checkout v002 (.blend_snapshot)...")

        bpy.ops.savepoints.refresh()
        settings = bpy.context.scene.savepoints_settings
        settings.active_version_index = 1  # v002

        bpy.ops.savepoints.checkout()

        current_path = Path(bpy.data.filepath)
        print(f"Current path after checkout: {current_path}")

        self.assertEqual(current_path.name, "snapshot.blend_snapshot",
                         f"Failed to checkout new format. Expected snapshot.blend_snapshot, got {current_path.name}")

        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
        self.assertTrue(parent_path, "Snapshot mode not detected for .blend_snapshot file")

        print("v002 (.blend_snapshot) Verification: OK")

        print("ALL COMPATIBILITY TESTS PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
