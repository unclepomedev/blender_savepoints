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

from savepoints.services.manifest import load_manifest
from savepoints_test_case import SavePointsTestCase


class TestTagging(SavePointsTestCase):

    def _get_version_from_settings(self, target_id):
        """Helper to retrieve version item from UI list by ID."""
        settings = bpy.context.scene.savepoints_settings
        for v in settings.versions:
            if v.version_id == target_id:
                return v
        return None

    def _get_version_from_manifest(self, target_id):
        """Helper to retrieve version dict from disk manifest by ID."""
        manifest = load_manifest()
        for v in manifest.get("versions", []):
            if v["id"] == target_id:
                return v
        return None

    def test_tagging_scenario(self):
        """
        Scenario:
        1. Create a version and confirm the default tag is 'NONE'.
        2. Update the tag to 'STABLE' and verify it reflects in both UI properties and disk manifest.
        3. Update the tag again to 'BUG' and verify the change is persisted.
        """
        print("Starting Tagging Scenario...")

        version_id = None

        # --- Step 1: Create Version & Check Default ---
        with self.subTest(step="1. Create Version"):
            print("Creating version...")

            # Setup context (ensure active object exists)
            bpy.ops.mesh.primitive_cube_add()

            # Commit
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Initial")
            self.assertIn('FINISHED', res, "Commit failed")

            # Get Version ID
            settings = bpy.context.scene.savepoints_settings
            self.assertGreater(len(settings.versions), 0, "No versions created")

            # Assuming the new one is at index 0
            version_id = settings.versions[0].version_id
            print(f"Target Version ID: {version_id}")

            # Verify Default Tag (Should be NONE)
            v_prop = self._get_version_from_settings(version_id)
            self.assertIsNotNone(v_prop, "Version not found in settings")
            self.assertEqual(v_prop.tag, 'NONE', "Default tag should be NONE")

        # --- Step 2: Set Tag to STABLE ---
        with self.subTest(step="2. Set Tag STABLE"):
            print(f"Setting tag for {version_id} to STABLE...")

            res = bpy.ops.savepoints.set_tag('EXEC_DEFAULT', version_id=version_id, tag='STABLE')
            self.assertIn('FINISHED', res, "Set Tag operator failed")

            # Verify in UI Props (Immediate update)
            v_prop = self._get_version_from_settings(version_id)
            self.assertEqual(v_prop.tag, 'STABLE', "UI Property tag not updated to STABLE")

            # Verify in Disk Manifest (Persistence)
            v_disk = self._get_version_from_manifest(version_id)
            self.assertIsNotNone(v_disk, "Version missing in manifest")
            self.assertEqual(v_disk["tag"], 'STABLE', "Manifest tag not persisted as STABLE")

        # --- Step 3: Set Tag to BUG ---
        with self.subTest(step="3. Set Tag BUG"):
            print(f"Setting tag for {version_id} to BUG...")

            # Update tag again to verify overwriting works
            res = bpy.ops.savepoints.set_tag('EXEC_DEFAULT', version_id=version_id, tag='BUG')
            self.assertIn('FINISHED', res, "Set Tag operator failed")

            # Verify in UI Props
            v_prop = self._get_version_from_settings(version_id)
            self.assertEqual(v_prop.tag, 'BUG', "UI Property tag not updated to BUG")

            # Verify in Disk Manifest
            v_disk = self._get_version_from_manifest(version_id)
            self.assertEqual(v_disk["tag"], 'BUG', "Manifest tag not persisted as BUG")

        print("Tagging Scenario: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
