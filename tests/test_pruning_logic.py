import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# MOCK BPY BEFORE IMPORTING PACKAGE
from unittest.mock import MagicMock

mock_bpy = MagicMock()


# Mock bpy.app.handlers.persistent
def persistent(func):
    return func


mock_bpy.app.handlers.persistent = persistent

# Assign submodules to mock_bpy for attribute access
mock_bpy.app = mock_bpy.app
mock_bpy.utils = MagicMock()
mock_bpy.props = MagicMock()
mock_bpy.types = MagicMock()
mock_bpy.ops = MagicMock()
mock_bpy.context = MagicMock()


# Define dummy base classes to avoid metaclass conflicts
class MockOperator:
    pass


class MockPanel:
    pass


class MockMenu:
    pass


class MockUIList:
    pass


mock_bpy.types.Operator = MockOperator
mock_bpy.types.Panel = MockPanel
mock_bpy.types.Menu = MockMenu
mock_bpy.types.UIList = MockUIList

# Inject into sys.modules
sys.modules['bpy'] = mock_bpy
sys.modules['bpy.app'] = mock_bpy.app
sys.modules['bpy.app.handlers'] = mock_bpy.app.handlers
sys.modules['bpy.utils'] = mock_bpy.utils
sys.modules['bpy.utils.previews'] = mock_bpy.utils.previews
sys.modules['bpy.props'] = mock_bpy.props
sys.modules['bpy.types'] = mock_bpy.types
sys.modules['bpy.ops'] = mock_bpy.ops
sys.modules['bpy.context'] = mock_bpy.context

# Mock other blender modules
sys.modules['gpu'] = MagicMock()
sys.modules['gpu_extras'] = MagicMock()
sys.modules['gpu_extras.batch'] = MagicMock()
sys.modules['bl_ui'] = MagicMock()
sys.modules['bpy_extras'] = MagicMock()
sys.modules['bpy_extras.io_utils'] = MagicMock()


# Assign ImportHelper as a class
class MockImportHelper:
    pass


sys.modules['bpy_extras.io_utils'].ImportHelper = MockImportHelper
sys.modules['bpy_extras.io_utils'].ExportHelper = MockImportHelper

from savepoints.services.versioning import prune_versions


class TestPruningLogic(unittest.TestCase):

    @patch('savepoints.services.versioning.load_manifest')
    @patch('savepoints.services.versioning.delete_version_by_id')
    def test_prune_versions_sorting(self, mock_delete, mock_load_manifest):
        """
        Verify that versions are sorted by ID (descending) before pruning.
        This ensures we keep the newest versions and delete the oldest.
        """
        # Setup mock manifest with unordered versions
        # IDs: v001, v003, v002
        # Chronological: v001 < v002 < v003
        mock_versions = [
            {"id": "v001", "is_protected": False},
            {"id": "v003", "is_protected": False},
            {"id": "v002", "is_protected": False},
            {"id": "autosave", "is_protected": False},  # autosave should be ignored
        ]

        mock_load_manifest.return_value = {"versions": mock_versions}

        # Execute prune with limit 2
        # Should keep v003 (newest), v002 (2nd newest).
        # Should delete v001.
        deleted_count = prune_versions(max_keep=2)

        # Verify
        self.assertEqual(deleted_count, 1, "Should have deleted exactly 1 version")

        # Check what was deleted
        mock_delete.assert_called_once_with("v001")

    @patch('savepoints.services.versioning.load_manifest')
    @patch('savepoints.services.versioning.delete_version_by_id')
    def test_prune_versions_with_protected(self, mock_delete, mock_load_manifest):
        """
        Verify that protected versions are ignored from quota and not deleted.
        """
        # Setup: v004(Locked), v003, v002, v001
        # Limit 2.
        # v004 is locked -> kept, doesn't count towards limit 2.
        # Remaining Unlocked: v003, v002, v001.
        # Should keep top 2 unlocked: v003, v002.
        # Should delete v001.

        mock_versions = [
            {"id": "v001", "is_protected": False},
            {"id": "v002", "is_protected": False},
            {"id": "v003", "is_protected": False},
            {"id": "v004", "is_protected": True},
        ]
        mock_load_manifest.return_value = {"versions": mock_versions}

        deleted_count = prune_versions(max_keep=2)

        self.assertEqual(deleted_count, 1, "Should have deleted exactly 1 version")
        mock_delete.assert_called_once_with("v001")


if __name__ == '__main__':
    unittest.main()
