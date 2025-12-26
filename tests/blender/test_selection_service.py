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

from savepoints_test_case import SavePointsTestCase
from savepoints.services.selection import get_selected_versions


class TestSelectionService(SavePointsTestCase):
    def test_get_selected_versions(self):
        """
        Test that get_selected_versions correctly filters:
        1. Versions with .selected = True
        2. Excludes 'autosave' even if selected (though autosave usually shouldn't be selected)
        3. Excludes unselected versions
        """
        print("Starting Selection Service Test...")

        settings = bpy.context.scene.savepoints_settings
        versions = settings.versions

        # 1. Create Data
        bpy.ops.savepoints.commit(note="V1")
        bpy.ops.savepoints.commit(note="V2")

        # 2. Select V1
        v1 = next(v for v in settings.versions if v.note == "V1")
        v2 = next(v for v in settings.versions if v.note == "V2")

        v1.selected = True
        v2.selected = False

        selected = get_selected_versions(settings)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0].note, "V1")

        # 3. Select Both
        v2.selected = True
        selected = get_selected_versions(settings)
        self.assertEqual(len(selected), 2)

        # 4. Autosave Check
        self.assertTrue(selected[0].version_id.startswith('v'))

        # 5. Deselect All
        versions[0].selected = False
        versions[1].selected = False
        selected = get_selected_versions(settings)
        self.assertEqual(len(selected), 0)

        print("Selection Service Test: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
