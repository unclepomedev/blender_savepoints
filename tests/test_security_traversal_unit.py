import os
import sys
import types
import unittest
import unittest.mock as mock
import tempfile
import shutil
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

# --- ROBUST MOCKING START ---
bpy = types.ModuleType("bpy")
bpy.app = types.ModuleType("bpy.app")
bpy.app.handlers = types.ModuleType("bpy.app.handlers")
bpy.utils = types.ModuleType("bpy.utils")
bpy.utils.previews = types.ModuleType("bpy.utils.previews")
bpy.types = types.ModuleType("bpy.types")
bpy.props = types.ModuleType("bpy.props")
bpy.data = types.ModuleType("bpy.data")
sys.modules["bpy"] = bpy
sys.modules["bpy.app"] = bpy.app
sys.modules["bpy.app.handlers"] = bpy.app.handlers
sys.modules["bpy.utils"] = bpy.utils
sys.modules["bpy.utils.previews"] = bpy.utils.previews


class MockImagePreviewCollection: pass


bpy.utils.previews.ImagePreviewCollection = MockImagePreviewCollection

sys.modules["bpy.types"] = bpy.types
sys.modules["bpy.props"] = bpy.props
sys.modules["bpy.data"] = bpy.data


def persistent(func): return func


bpy.app.handlers.persistent = persistent


class MockContext: pass


bpy.types.Context = MockContext


class MockOperator: pass


bpy.types.Operator = MockOperator


class MockPanel: pass


bpy.types.Panel = MockPanel


class MockMenu: pass


bpy.types.Menu = MockMenu


class MockPropertyGroup: pass


bpy.types.PropertyGroup = MockPropertyGroup


class MockUIList: pass


bpy.types.UIList = MockUIList

bpy.props.StringProperty = mock.MagicMock()
bpy.props.IntProperty = mock.MagicMock()
bpy.props.BoolProperty = mock.MagicMock()
bpy.props.FloatProperty = mock.MagicMock()
bpy.props.EnumProperty = mock.MagicMock()
bpy.props.CollectionProperty = mock.MagicMock()
bpy.props.PointerProperty = mock.MagicMock()
blf = types.ModuleType("blf")
sys.modules["blf"] = blf
gpu = types.ModuleType("gpu")
sys.modules["gpu"] = gpu
gpu_extras = types.ModuleType("gpu_extras")
gpu_extras.batch = types.ModuleType("gpu_extras.batch")
sys.modules["gpu_extras"] = gpu_extras
sys.modules["gpu_extras.batch"] = gpu_extras.batch
gpu_extras.batch.batch_for_shader = mock.MagicMock()
bpy_extras = types.ModuleType("bpy_extras")
bpy_extras.io_utils = types.ModuleType("bpy_extras.io_utils")
sys.modules["bpy_extras"] = bpy_extras
sys.modules["bpy_extras.io_utils"] = bpy_extras.io_utils


class MockImportHelper: pass


bpy_extras.io_utils.ImportHelper = MockImportHelper


class MockExportHelper: pass


bpy_extras.io_utils.ExportHelper = MockExportHelper

# --- ROBUST MOCKING END ---

from savepoints.core import delete_version_by_id


class TestSecurityTraversal(unittest.TestCase):
    @mock.patch("savepoints.core.shutil.rmtree")
    @mock.patch("savepoints.core.get_history_dir")
    @mock.patch("savepoints.core.load_manifest")
    @mock.patch("savepoints.core.save_manifest")
    def test_delete_version_path_traversal_prevention(self, mock_save, mock_load, mock_get_history, mock_rmtree):
        # Setup temporary directories
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            history_dir = tmp_path / "project" / "history"
            history_dir.mkdir(parents=True)

            # The target outside history that attacker wants to delete
            target_dir = tmp_path / "system"
            target_dir.mkdir()

            mock_get_history.return_value = str(history_dir)

            # Malicious ID: ../../system
            # From history_dir: ../../system -> tmp_path/system
            malicious_id = "../../system"

            mock_load.return_value = {
                "versions": [{"id": malicious_id, "is_protected": False}]
            }

            # Action
            delete_version_by_id(malicious_id)

            # Verification: rmtree should NOT be called
            self.assertFalse(mock_rmtree.called, "shutil.rmtree should NOT be called for path traversal attempt")

    @mock.patch("savepoints.core.shutil.rmtree")
    @mock.patch("savepoints.core.get_history_dir")
    @mock.patch("savepoints.core.load_manifest")
    @mock.patch("savepoints.core.save_manifest")
    def test_delete_version_rejects_multiple_traversal_patterns(self, mock_save, mock_load, mock_get_history,
                                                                mock_rmtree):
        malicious_ids = [
            "../../system",
            "../../../etc",
            "version/../../../system",
            "/absolute/path",
            "..\\..\\system",  # Windows-style
            "path/with/slash",
            "",  # empty string
        ]

        mock_get_history.return_value = "/tmp/history"
        mock_load.return_value = {"versions": []}

        for malicious_id in malicious_ids:
            mock_rmtree.reset_mock()
            delete_version_by_id(malicious_id)
            self.assertFalse(mock_rmtree.called, f"rmtree should not be called for: {malicious_id}")


if __name__ == '__main__':
    unittest.main()
