import importlib
import sys
import unittest
from unittest.mock import MagicMock, patch


# Define mock classes at module level (safe as they don't modify global state)
class MockImportHelper: pass


class MockExportHelper: pass


class MockOperator: pass


class TestUiSorting(unittest.TestCase):
    def setUp(self):
        # --- 1. Mock Blender API ---
        self.mock_bpy = MagicMock()

        # Define mock modules
        modules = {
            "bpy": self.mock_bpy,
            "bpy.app": self.mock_bpy.app,
            "bpy.app.handlers": self.mock_bpy.app.handlers,
            "bpy.types": self.mock_bpy.types,
            "bpy.props": self.mock_bpy.props,
            "bpy.utils": self.mock_bpy.utils,
            "bpy.utils.previews": MagicMock(),
            "bpy_extras": MagicMock(),
            "bpy_extras.io_utils": MagicMock(),
            "blf": MagicMock(),
            "gpu": MagicMock(),
            "gpu_extras": MagicMock(),
            "gpu_extras.batch": MagicMock(),
        }

        # Configure Mocks for inheritance
        modules["bpy_extras.io_utils"].ImportHelper = MockImportHelper
        modules["bpy_extras.io_utils"].ExportHelper = MockExportHelper
        modules["bpy"].types.Operator = MockOperator

        # --- 2. Patch sys.modules ---
        # Use patch.dict to scope changes to sys.modules
        self.patcher = patch.dict(sys.modules, modules)
        self.patcher.start()

        # --- 3. Import/Reload Addon Modules ---
        # We must import (or reload) the module under test *after* patching sys.modules
        # so that it picks up the mock modules.
        # importlib.reload is safer if the module was already imported by another test.
        try:
            import savepoints.ui_utils
            importlib.reload(savepoints.ui_utils)
            self.ui_utils = savepoints.ui_utils
        except ImportError:
            # Fallback or handle cases where dependencies might be missing if mocks aren't perfect
            # But since we mocked everything savepoints.ui_utils needs (bpy, core), it should work.
            # Note: savepoints.ui_utils imports core. If core isn't in sys.modules, it will be imported.
            # core imports bpy (which is mocked).
            # If savepoints.__init__ is triggered, it imports operators, etc.
            # We need to ensure we mocked enough for the recursive imports.
            # The list above covers most things.
            raise

        # Mock core functions used in sync_history_to_props
        # We act on the imported module object
        self.mock_core = MagicMock()
        self.ui_utils.core = self.mock_core

        # Mock preview collection
        self.ui_utils.preview_collections = {"main": MagicMock()}

    def tearDown(self):
        self.patcher.stop()

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

        # Simulate len()
        mock_settings.versions.__len__.return_value = 4

        # Set active_version_index to a valid integer to avoid comparison error
        mock_settings.active_version_index = -1

        # Execute
        self.ui_utils.sync_history_to_props(mock_context)

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
