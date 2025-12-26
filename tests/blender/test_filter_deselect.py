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


class TestFilterDeselect(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # Create versions
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.savepoints.commit(note="V1")
        bpy.ops.savepoints.commit(note="V2")

        self.settings = bpy.context.scene.savepoints_settings
        versions = self.settings.versions

        self.v1 = next(v for v in versions if v.note == "V1")
        self.v2 = next(v for v in versions if v.note == "V2")

        # Setup tags
        # V1 -> STABLE
        # V2 -> BUG
        self.v1.tag = 'STABLE'
        self.v2.tag = 'BUG'

    def test_deselect_hidden_items_on_filter_change(self):
        """
        Verify that when the filter changes, items that are hidden (don't match filter)
        are automatically deselected.
        """
        v1 = self.v1  # STABLE
        v2 = self.v2  # BUG

        # 1. Select both
        v1.selected = True
        v2.selected = True

        # 2. Change filter to 'STABLE'
        # This should hide V2 (BUG). The requirement is that hidden items get deselected.
        self.settings.filter_tag = 'STABLE'

        # 3. Verify
        self.assertTrue(v1.selected, "V1 (Matching filter) should remain selected")
        self.assertFalse(v2.selected, "V2 (Hidden by filter) should be deselected")

    def test_deselect_on_switching_filters(self):
        """
        Verify switching between restrictive filters.
        """
        v1 = self.v1  # STABLE
        v2 = self.v2  # BUG

        # Select V1
        v1.selected = True
        v2.selected = False

        # Filter is currently ALL (default)

        # Switch to BUG
        self.settings.filter_tag = 'BUG'

        # V1 (STABLE) should now be deselected because it's hidden
        self.assertFalse(v1.selected, "V1 should be deselected when switching to BUG filter")

        # V2 (BUG) is visible, but was not selected. It should remain not selected (unless we wanted auto-select, but requirement says 'deselect hidden')
        self.assertFalse(v2.selected, "V2 should remain unselected")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
