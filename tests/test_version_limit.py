import sys
import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# MOCK BPY
mock_bpy = MagicMock()


def persistent(func):
    return func


mock_bpy.app.handlers.persistent = persistent
mock_bpy.app = mock_bpy.app
mock_bpy.utils = MagicMock()
mock_bpy.props = MagicMock()
mock_bpy.types = MagicMock()
mock_bpy.ops = MagicMock()
mock_bpy.context = MagicMock()
mock_bpy.utils.previews = MagicMock()
mock_bpy.app.timers = MagicMock()


# Define dummy base classes
class MockOperator: pass


class MockPanel: pass


class MockMenu: pass


class MockUIList: pass


mock_bpy.types.Operator = MockOperator
mock_bpy.types.Panel = MockPanel
mock_bpy.types.Menu = MockMenu
mock_bpy.types.UIList = MockUIList

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


class MockImportHelper: pass


sys.modules['bpy_extras.io_utils'].ImportHelper = MockImportHelper
sys.modules['bpy_extras.io_utils'].ExportHelper = MockImportHelper  # Added this

from savepoints.services.versioning import get_next_version_id, VersionLimitReachedError


class TestVersionLimit(unittest.TestCase):
    def test_version_limit_v999(self):
        # Scenario: Last version is v999. Next should be v1000 (currently).
        versions = [{"id": "v999"}]

        with self.assertRaises(VersionLimitReachedError):
            get_next_version_id(versions)


if __name__ == '__main__':
    unittest.main()
