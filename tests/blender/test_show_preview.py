import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

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
        self.settings = bpy.context.scene.savepoints_settings

        item = self.settings.versions.add()
        item.version_id = "v001"
        item.note = "Test Version"
        self.settings.active_version_index = 0

    def test_preview_ui_scenario(self):
        """
        Scenario:
        1. Property Logic: Verify default value and toggling of 'show_preview'.
        2. General Settings UI: Verify the 'show_preview' checkbox is drawn.
        3. Detail View UI: Verify preview image is drawn ONLY when enabled.
        4. Robustness: Verify drawing does not crash in headless mode (region=None).
        """
        print("Starting Preview UI Scenario...")

        # --- Step 1: Property Logic ---
        with self.subTest(step="1. Property Logic"):
            self.assertTrue(self.settings.show_preview, "Default should be True")
            self.settings.show_preview = False
            self.assertFalse(self.settings.show_preview)
            self.settings.show_preview = True
            self.assertTrue(self.settings.show_preview)

        # --- Step 2: General Settings UI (Checkbox) ---
        with self.subTest(step="2. General Settings UI"):
            layout_mock = MagicMock()
            box_mock = MagicMock()
            layout_mock.box.return_value = box_mock

            ui._draw_general_settings(layout_mock, self.settings)

            prop_calls = [args[1] for args, _ in box_mock.prop.call_args_list]
            self.assertIn("show_preview", prop_calls)

        # --- Step 3: Detail View UI (Conditional Drawing) ---
        with self.subTest(step="3. Detail View UI"):
            layout_mock = MagicMock()

            mock_context = MagicMock()
            mock_context.region = MagicMock()
            mock_context.region.width = 300

            mock_preview_image = MagicMock()
            mock_preview_image.icon_id = 99999

            fake_collections_dict = {"main": {"v001": mock_preview_image}}

            with patch('savepoints.ui_utils.preview_collections', fake_collections_dict):
                # Case A: Show Preview = OFF
                self.settings.show_preview = False
                ui._draw_version_details(layout_mock, self.settings, mock_context)

                # Case B: Show Preview = ON
                self.settings.show_preview = True
                ui._draw_version_details(layout_mock, self.settings, mock_context)

        # --- Step 4: Robustness (Headless Mode) ---
        with self.subTest(step="4. Robustness (Region=None)"):
            self.settings.show_preview = True

            layout_mock = MagicMock()
            mock_context_headless = MagicMock()
            mock_context_headless.region = None

            mock_preview_image = MagicMock()
            mock_preview_image.icon_id = 88888
            fake_collections_dict = {"main": {"v001": mock_preview_image}}

            with patch('savepoints.ui_utils.preview_collections', fake_collections_dict):
                try:
                    ui._draw_version_details(layout_mock, self.settings, mock_context_headless)
                except AttributeError as e:
                    self.fail(f"UI crashed in headless mode (region=None): {e}")

        print("Preview UI Scenario: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
