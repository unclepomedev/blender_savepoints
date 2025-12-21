import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

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

from savepoints.services.versioning import get_next_version_id, get_sorted_versions


class TestVersionLimit(unittest.TestCase):
    def test_version_over_999(self):
        # Scenario: Last version is v999. Should NOT raise error, but return v1000.
        versions = [{"id": "v999"}]

        next_id = get_next_version_id(versions)
        self.assertEqual(next_id, "v1000")

    def test_version_sorting(self):
        # Scenario: Verify sorting works for mixed digits (v2, v10, v999, v1000)
        # Note: manifest["versions"] is usually a list of dicts.
        manifest = {
            "versions": [
                {"id": "v2"},
                {"id": "v10"},
                {"id": "v999"},
                {"id": "v1000"},
                {"id": "v1"}
            ]
        }

        # newest_first=True -> v1000 should be first, v1 last
        sorted_versions = get_sorted_versions(manifest, newest_first=True)
        self.assertEqual(sorted_versions[0]["id"], "v1000")
        self.assertEqual(sorted_versions[1]["id"], "v999")
        self.assertEqual(sorted_versions[2]["id"], "v10")
        self.assertEqual(sorted_versions[3]["id"], "v2")
        self.assertEqual(sorted_versions[4]["id"], "v1")

        # newest_first=False -> v1 first, v1000 last
        sorted_versions_asc = get_sorted_versions(manifest, newest_first=False)
        self.assertEqual(sorted_versions_asc[0]["id"], "v1")
        self.assertEqual(sorted_versions_asc[-1]["id"], "v1000")


if __name__ == '__main__':
    unittest.main()
