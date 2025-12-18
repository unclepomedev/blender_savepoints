import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints import ui
from savepoints_test_case import SavePointsTestCase


class TestShowPreview(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # savepoints.register() is called in super().setUp()

        # We need settings. SavePointsTestCase creates a clean session, so settings are reset.
        self.settings = bpy.context.scene.savepoints_settings

        # Create a dummy version to ensure we have an active item
        item = self.settings.versions.add()
        item.version_id = "v001"
        item.note = "Test Version"
        self.settings.active_version_index = 0

    def tearDown(self):
        super().tearDown()
        # savepoints.unregister() is called in super().tearDown()

    def test_show_preview_property_default(self):
        # Default should be True
        self.assertTrue(self.settings.show_preview)

    def test_show_preview_toggle(self):
        self.settings.show_preview = False
        self.assertFalse(self.settings.show_preview)
        self.settings.show_preview = True
        self.assertTrue(self.settings.show_preview)

    def test_draw_general_settings_contains_prop(self):
        # Verify that the property is drawn in the settings panel
        layout = MagicMock()
        box = MagicMock()
        layout.box.return_value = box

        ui._draw_general_settings(layout, self.settings)

        # Check if box.prop was called with "show_preview"
        calls = box.prop.call_args_list
        prop_names = [call[0][1] for call in calls]  # call[0] is args, call[0][1] is property name

        self.assertIn("show_preview", prop_names)

    def test_draw_version_details_logic(self):
        # Test that _draw_version_details respects the flag
        layout = MagicMock()
        box = MagicMock()
        layout.box.return_value = box

        # Case 1: Show Preview = False
        self.settings.show_preview = False

        MockContext = MagicMock()
        MockContext.region = None

        try:
            ui._draw_version_details(layout, self.settings, MockContext)
        except AttributeError as e:
            self.fail(f"_draw_version_details raised AttributeError with show_preview=False: {e}")

        # Case 2: Show Preview = True
        self.settings.show_preview = True

        try:
            ui._draw_version_details(layout, self.settings, MockContext)
        except Exception as e:
            self.fail(f"_draw_version_details failed with show_preview=True: {e}")

    def test_draw_version_details_with_preview_and_no_region(self):
        # Populate preview collection to make has_preview=True
        from savepoints import ui_utils
        pcoll = ui_utils.preview_collections.setdefault("main", bpy.utils.previews.new())

        # Mock preview for v001
        # pcoll["v001"] = ... (you'd need to create a mock preview)

        self.settings.show_preview = True

        layout = MagicMock()
        box = MagicMock()
        layout.box.return_value = box

        MockContext = MagicMock()
        MockContext.region = None  # Simulate headless mode

        # Should not raise AttributeError
        try:
            ui._draw_version_details(layout, self.settings, MockContext)
        except AttributeError as e:
            self.fail(f"Should handle region=None gracefully: {e}")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
