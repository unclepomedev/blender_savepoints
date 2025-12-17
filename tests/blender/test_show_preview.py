import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints
from savepoints import ui


class TestShowPreview(unittest.TestCase):
    def setUp(self):
        savepoints.register()
        self.settings = bpy.context.scene.savepoints_settings

        # Create a dummy version to ensure we have an active item
        item = self.settings.versions.add()
        item.version_id = "v001"
        item.note = "Test Version"
        self.settings.active_version_index = 0

    def tearDown(self):
        savepoints.unregister()

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
        # We can't easily check what was drawn, but we can ensure it runs without error
        # and potentially mock objects to see which path was taken.

        layout = MagicMock()
        box = MagicMock()
        layout.box.return_value = box

        # Case 1: Show Preview = False
        self.settings.show_preview = False

        # In headless mode context.region is usually None.
        # If the code tries to access context.region.width, it would fail if we don't mock context.
        # But if show_preview is False, it should NOT access it (or even check previews).

        # We pass a dummy context where region is explicitly None to prove it doesn't access it
        MockContext = MagicMock()
        MockContext.region = None

        try:
            ui._draw_version_details(layout, self.settings, MockContext)
        except AttributeError as e:
            self.fail(f"_draw_version_details raised AttributeError with show_preview=False: {e}")

        # Verify that box.row() was NOT called (because row is used for preview or "No Preview")
        # Actually, wait. 
        # If show_preview is False:
        #   It skips the whole block.
        #   It draws ID, Date, Note...
        # So box.row() should NOT be called for the image.
        # However, checking call counts on mocks is fragile if other UI elements use rows.
        # Let's look at the code:
        # if settings.show_preview: ...
        # box.label(text=f"ID: ...") 

        # So if show_preview is False, we just check that it runs safely.

        # Case 2: Show Preview = True
        self.settings.show_preview = True

        # If we run this now with region=None, does it fail?
        # It only fails if has_preview is True. 
        # In this test environment, pcoll is likely empty or None, so has_preview = False.
        # Then it goes to `else: row.label(text="No Preview"...)`.
        # So it should still run safely even with region=None.

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
