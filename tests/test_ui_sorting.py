import sys
import unittest
from unittest.mock import MagicMock

# --- 1. Mock Blender API (Must be done before import) ---
mock_bpy = MagicMock()

# Define mock modules
modules = {
    "bpy": mock_bpy,
    "bpy.app": mock_bpy.app,
    "bpy.app.handlers": mock_bpy.app.handlers,
    "bpy.types": mock_bpy.types,
    "bpy.props": mock_bpy.props,
    "bpy.utils": mock_bpy.utils,
    "bpy.utils.previews": MagicMock(),
    "bpy_extras": MagicMock(),
    "bpy_extras.io_utils": MagicMock(),
    "blf": MagicMock(),
    "gpu": MagicMock(),
    "gpu_extras": MagicMock(),
    "gpu_extras.batch": MagicMock(),
}
sys.modules.update(modules)


# Assign ImportHelper for inheritance
class MockImportHelper: pass


modules["bpy_extras.io_utils"].ImportHelper = MockImportHelper


class MockExportHelper: pass


modules["bpy_extras.io_utils"].ExportHelper = MockExportHelper


# Fix for multiple inheritance (metaclass conflict) if operators are imported
class MockOperator: pass


modules["bpy"].types.Operator = MockOperator

# --- 2. Import Addon Modules ---
# Note: ui_utils imports core, so we need to handle that.
# We will mock core AFTER import, or mock the function within ui_utils.
import savepoints.ui_utils


class TestUiSorting(unittest.TestCase):
    def setUp(self):
        mock_bpy.reset_mock()

        # Mock core functions used in sync_history_to_props
        self.mock_core = MagicMock()
        savepoints.ui_utils.core = self.mock_core

        # Mock preview collection
        savepoints.ui_utils.preview_collections = {"main": MagicMock()}

    def test_sync_history_sorting(self):
        """Verify that versions are sorted by ID, with autosave last."""

        # Setup Mock Data
        manifest_data = {
            "versions": [
                {"id": "v003"},
                {"id": "autosave"},
                {"id": "v001"},
                {"id": "v002"},
            ]
        }
        self.mock_core.load_manifest.return_value = manifest_data
        self.mock_core.get_history_dir.return_value = "/tmp/history"
        self.mock_core.from_posix_path = lambda x: x  # Pass through
        self.mock_core.format_file_size.return_value = "10 MB"

        # Setup Mock Context
        mock_context = MagicMock()
        mock_settings = MagicMock()
        mock_context.scene.savepoints_settings = mock_settings

        # Simulate 'versions' collection
        created_items = []

        def add_version():
            item = MagicMock()
            created_items.append(item)
            return item

        mock_settings.versions.add.side_effect = add_version

        # Need to simulate len() for 'if len(settings.versions) > 0' check at the end
        # We can't easily mock len() on a PropertyMock return value if it's not a real list.
        # But we can mock the list access or just ignore the index reset part if it doesn't crash.
        # Let's make settings.versions a real list-like mock? No, PropertyGroup is complex.
        # Just mocking __len__ on the versions object might work.
        mock_settings.versions.__len__.return_value = 4

        # Set active_version_index to a valid integer to avoid comparison error
        mock_settings.active_version_index = -1

        # Execute
        savepoints.ui_utils.sync_history_to_props(mock_context)

        # Verify Calls
        self.mock_core.load_manifest.assert_called_once()
        self.assertEqual(mock_settings.versions.clear.call_count, 1)
        self.assertEqual(mock_settings.versions.add.call_count, 4)

        # Verify Order of added items
        # The items should have been populated in the sorted order: v001, v002, v003, autosave

        self.assertEqual(created_items[0].version_id, "v001")
        self.assertEqual(created_items[1].version_id, "v002")
        self.assertEqual(created_items[2].version_id, "v003")
        self.assertEqual(created_items[3].version_id, "autosave")


if __name__ == '__main__':
    unittest.main()
