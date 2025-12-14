import os
import sys
import types
import unittest
import unittest.mock as mock
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

# --- ROBUST MOCKING START ---
# Create module objects
bpy = types.ModuleType("bpy")
bpy.app = types.ModuleType("bpy.app")
bpy.app.handlers = types.ModuleType("bpy.app.handlers")
bpy.utils = types.ModuleType("bpy.utils")
bpy.utils.previews = types.ModuleType("bpy.utils.previews")
bpy.types = types.ModuleType("bpy.types")
bpy.props = types.ModuleType("bpy.props")
bpy.data = types.ModuleType("bpy.data")

# Populate modules
sys.modules["bpy"] = bpy
sys.modules["bpy.app"] = bpy.app
sys.modules["bpy.app.handlers"] = bpy.app.handlers
sys.modules["bpy.utils"] = bpy.utils
sys.modules["bpy.utils.previews"] = bpy.utils.previews
sys.modules["bpy.types"] = bpy.types
sys.modules["bpy.props"] = bpy.props
sys.modules["bpy.data"] = bpy.data


class MockImagePreviewCollection: pass


bpy.utils.previews.ImagePreviewCollection = MockImagePreviewCollection


# Mock specific attributes used by import time code
def persistent(func): return func


bpy.app.handlers.persistent = persistent


# Mock basic classes needed for inheritance if any
class MockPropertyGroup: pass


bpy.types.PropertyGroup = MockPropertyGroup


class MockOperator: pass


bpy.types.Operator = MockOperator


class MockUIList: pass


bpy.types.UIList = MockUIList


class MockPanel: pass


bpy.types.Panel = MockPanel


class MockContext: pass


bpy.types.Context = MockContext

# Mock props
bpy.props.StringProperty = mock.MagicMock()
bpy.props.IntProperty = mock.MagicMock()
bpy.props.BoolProperty = mock.MagicMock()
bpy.props.FloatProperty = mock.MagicMock()
bpy.props.EnumProperty = mock.MagicMock()
bpy.props.CollectionProperty = mock.MagicMock()
bpy.props.PointerProperty = mock.MagicMock()

# Mock graphics modules (needed because __init__ imports hud which imports these)
blf = types.ModuleType("blf")
sys.modules["blf"] = blf

gpu = types.ModuleType("gpu")
sys.modules["gpu"] = gpu

gpu_extras = types.ModuleType("gpu_extras")
gpu_extras.batch = types.ModuleType("gpu_extras.batch")
sys.modules["gpu_extras"] = gpu_extras
sys.modules["gpu_extras.batch"] = gpu_extras.batch
gpu_extras.batch.batch_for_shader = mock.MagicMock()

# Mock bpy_extras
bpy_extras = types.ModuleType("bpy_extras")
bpy_extras.io_utils = types.ModuleType("bpy_extras.io_utils")
sys.modules["bpy_extras"] = bpy_extras
sys.modules["bpy_extras.io_utils"] = bpy_extras.io_utils

class MockImportHelper: pass
bpy_extras.io_utils.ImportHelper = MockImportHelper

class MockExportHelper: pass
bpy_extras.io_utils.ExportHelper = MockExportHelper

# --- ROBUST MOCKING END ---

from savepoints.core import get_parent_path_from_snapshot


class TestPathUtils(unittest.TestCase):
    def test_snapshot_path_detection(self):
        # Case 1a: New snapshot extension (.blend_snapshot)
        base = "/projects"
        filename = "MyScene"
        history_dir = f".{filename}_history"
        version = "v005"
        snapshot = "snapshot.blend_snapshot"

        full_path = os.path.join(base, history_dir, version, snapshot)
        expected_parent = os.path.join(base, f"{filename}.blend")

        result = get_parent_path_from_snapshot(full_path)
        self.assertEqual(result, expected_parent)

        # Case 1b: Old snapshot extension (.blend)
        snapshot_old = "snapshot.blend"
        full_path_old = os.path.join(base, history_dir, version, snapshot_old)
        
        result_old = get_parent_path_from_snapshot(full_path_old)
        self.assertEqual(result_old, expected_parent)

    def test_not_snapshot_path(self):
        # Case 2: Normal file
        full_path = "/projects/MyScene.blend"
        result = get_parent_path_from_snapshot(full_path)
        self.assertIsNone(result)

    def test_nested_history_not_matched(self):
        # Case 3: Just inside a folder called history but not following convention
        full_path = "/projects/history/v001/snapshot.blend_snapshot"
        result = get_parent_path_from_snapshot(full_path)
        self.assertIsNone(result)

    def test_wrong_history_naming(self):
        # Case 4: History folder doesn't start with dot
        full_path = "/projects/MyScene_history/v001/snapshot.blend_snapshot"
        result = get_parent_path_from_snapshot(full_path)
        self.assertIsNone(result)

    def test_windows_path_on_posix_danger(self):
        # Simulate a manifest entry created on Windows: "v001\snapshot.blend_snapshot"
        # On POSIX (Mac/Linux), backslash is NOT a separator.
        # os.path.join joining a dir and this string results in: dir/v001\snapshot.blend_snapshot
        # os.path.dirname of this is 'dir' (the history folder), NOT 'dir/v001'.

        # Only run this test on POSIX
        if os.name == 'nt':
            return

        history_dir = "/project/.history"
        windows_blend_path = "v001\\snapshot.blend_snapshot"

        full_path = os.path.join(history_dir, windows_blend_path)

        # On POSIX, the filename is "v001\snapshot.blend_snapshot", so dirname is history_dir
        detected_folder = os.path.dirname(full_path)

        # This confirms the bug: we would inadvertently target the history root for deletion
        self.assertEqual(detected_folder, history_dir)

    def test_safe_path_resolution_with_fix(self):
        # Test the fix using from_posix_path
        from savepoints.core import from_posix_path

        if os.name == 'nt':
            # On Windows, both are separators or handled, but let's test logic explicitly
            pass

        history_dir = "/project/.history"
        windows_blend_path = "v001\\snapshot.blend_snapshot"

        # 1. Normalize the path from manifest
        normalized_path = from_posix_path(windows_blend_path)

        if os.name != 'nt':
            # On POSIX, it should replace backslash with slash
            self.assertEqual(normalized_path, "v001/snapshot.blend_snapshot")

            full_path = os.path.join(history_dir, normalized_path)
            detected_folder = os.path.dirname(full_path)

            # Should be .../v001
            self.assertEqual(detected_folder, "/project/.history/v001")
            self.assertNotEqual(detected_folder, history_dir)

    def test_commit_poll_guard(self):
        # Test that SAVEPOINTS_OT_commit.poll returns False when in snapshot mode
        # We need to import operators here so it uses the mocked bpy
        from savepoints.operators import SAVEPOINTS_OT_commit

        mock_context = mock.MagicMock()

        # Case 1: Normal file -> poll should be True
        # We use platform specific separator construction to be safe, 
        # though the mocked bpy is just a value holder.
        # get_parent_path_from_snapshot uses os.path, so we must match os.sep

        base = os.path.abspath("/project")
        filename = "MyScene.blend"
        normal_path = os.path.join(base, filename)

        bpy.data.filepath = normal_path
        self.assertTrue(SAVEPOINTS_OT_commit.poll(mock_context), f"Poll should be True for normal file: {normal_path}")

        # Case 2: Snapshot file -> poll should be False
        history_dir = ".MyScene_history"
        snapshot_path = os.path.join(base, history_dir, "v001", "snapshot.blend_snapshot")

        bpy.data.filepath = snapshot_path
        self.assertFalse(SAVEPOINTS_OT_commit.poll(mock_context),
                         f"Poll should be False for snapshot file: {snapshot_path}")


if __name__ == '__main__':
    unittest.main()
