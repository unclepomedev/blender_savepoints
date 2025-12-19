import json
import shutil
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


class TestExtensionCompatibility(SavePointsTestCase):

    def _create_manual_history(self):
        """
        Helper: Manually create a history structure with mixed extensions.
        v001 -> snapshot.blend (Legacy format)
        v002 -> snapshot.blend_snapshot (New format)
        """
        history_dir = self.test_dir / ".test_project_history"
        history_dir.mkdir(exist_ok=True)

        # Copy current blend file to use as snapshots
        src_blend = self.blend_path

        # Create v001 (Legacy format: .blend)
        v001_dir = history_dir / "v001"
        v001_dir.mkdir(exist_ok=True)
        shutil.copy2(src_blend, v001_dir / "snapshot.blend")

        # Create v002 (New format: .blend_snapshot)
        v002_dir = history_dir / "v002"
        v002_dir.mkdir(exist_ok=True)
        shutil.copy2(src_blend, v002_dir / "snapshot.blend_snapshot")

        # Create manifest.json
        manifest = {
            "parent_file": str(src_blend),
            "versions": [
                {
                    "id": "v001",
                    "note": "Legacy Format",
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

    def _set_active_version_by_id(self, target_id):
        """Helper to find the index of a version ID and set it active."""
        settings = bpy.context.scene.savepoints_settings
        for i, v in enumerate(settings.versions):
            # [FIXED] Use 'version_id' instead of 'id' to match PropertyGroup definition
            if v.version_id == target_id:
                settings.active_version_index = i
                return
        self.fail(f"Version ID {target_id} not found in UI list")

    def test_extension_compatibility_scenario(self):
        """
        Scenario:
        1. Setup a history folder containing both legacy (.blend) and new (.blend_snapshot) extensions.
        2. Verify that the addon can list both versions.
        3. Verify checkout works for the legacy .blend extension.
        4. Verify checkout works for the new .blend_snapshot extension.
        """
        print("Starting Extension Compatibility Scenario...")

        # --- Step 1: Setup Mixed History ---
        with self.subTest(step="1. Setup Mixed History"):
            print("Generating manual history...")
            self._create_manual_history()

            # Refresh to load the manually created manifest into Blender
            bpy.ops.savepoints.refresh()

            # Verify settings loaded correctly
            settings = bpy.context.scene.savepoints_settings
            self.assertEqual(len(settings.versions), 2, "Failed to load all versions from manifest")

        # --- Step 2: Checkout Legacy Format (.blend) ---
        with self.subTest(step="2. Checkout Legacy (.blend)"):
            print("Testing Checkout v001 (Legacy)...")

            self._set_active_version_by_id("v001")
            bpy.ops.savepoints.checkout()

            current_path = Path(bpy.data.filepath)

            # Verify filename matches legacy extension
            self.assertEqual(current_path.name, "snapshot.blend", "Failed to checkout legacy format")

            # Verify parent path detection
            parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
            self.assertTrue(parent_path, "Snapshot mode not detected for .blend file")
            self.assertEqual(Path(parent_path), self.blend_path, "Incorrect parent path detected for legacy file")

        # --- Step 3: Return to Parent ---
        with self.subTest(step="3. Return to Parent"):
            print("Returning to parent file...")

            bpy.ops.savepoints.open_parent()

            self.assertEqual(Path(bpy.data.filepath), self.blend_path, "Failed to return to parent file")

        # --- Step 4: Checkout New Format (.blend_snapshot) ---
        with self.subTest(step="4. Checkout New Format (.blend_snapshot)"):
            print("Testing Checkout v002 (New Format)...")

            # Need to refresh or ensure settings are valid after returning
            bpy.ops.savepoints.refresh()

            self._set_active_version_by_id("v002")
            bpy.ops.savepoints.checkout()

            current_path = Path(bpy.data.filepath)

            # Verify filename matches new extension
            self.assertEqual(current_path.name, "snapshot.blend_snapshot", "Failed to checkout new format")

            # Verify parent path detection
            parent_path = get_parent_path_from_snapshot(bpy.data.filepath)
            self.assertTrue(parent_path, "Snapshot mode not detected for .blend_snapshot file")

        print("Extension Compatibility Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
