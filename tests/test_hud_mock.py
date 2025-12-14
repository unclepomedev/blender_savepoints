import unittest
import sys
from unittest.mock import MagicMock, PropertyMock

# --- 1. Mock Blender API (Must be done before import) ---
mock_bpy = MagicMock()
mock_bpy.app.handlers.persistent = lambda func: func  # Pass-through decorator

# Define mock modules
modules = {
    "bpy": mock_bpy,
    "bpy.app": mock_bpy.app,
    "bpy.app.handlers": mock_bpy.app.handlers,
    "bpy.types": mock_bpy.types,
    "bpy.props": mock_bpy.props,
    "bpy.utils": mock_bpy.utils,
    "bpy.utils.previews": MagicMock(),
    "blf": MagicMock(),
    "gpu": MagicMock(),
    "gpu_extras": MagicMock(),
    "gpu_extras.batch": MagicMock(),
    "bpy_extras": MagicMock(),
    "bpy_extras.io_utils": MagicMock(),
}
sys.modules.update(modules)

# Assign ImportHelper for inheritance
class MockImportHelper: pass
modules["bpy_extras.io_utils"].ImportHelper = MockImportHelper

# Fix for multiple inheritance (metaclass conflict)
class MockOperator: pass
modules["bpy"].types.Operator = MockOperator

# Alias for convenience in tests
mock_blf = modules["blf"]
mock_gpu = modules["gpu"]
mock_gpu_batch = modules["gpu_extras.batch"]

# --- 2. Import Addon Modules ---
import savepoints.hud
# core is imported to leverage real path parsing logic (unless mocked later)
import savepoints.core


class TestHud(unittest.TestCase):
    def setUp(self):
        mock_bpy.reset_mock()
        mock_blf.reset_mock()
        mock_gpu.reset_mock()
        mock_gpu_batch.reset_mock()

    def test_draw_hud_abort_on_invalid_context(self):
        """Should abort drawing if context is missing or invalid."""
        # Simulate context access error
        type(mock_bpy).context = PropertyMock(side_effect=AttributeError)

        savepoints.hud.draw_hud()

        mock_blf.draw.assert_not_called()

    def test_draw_hud_abort_on_wrong_area(self):
        """Should abort if not in 3D View."""
        mock_context = MagicMock()
        mock_context.area.type = "PROPERTIES"
        type(mock_bpy).context = PropertyMock(return_value=mock_context)

        savepoints.hud.draw_hud()

        mock_blf.draw.assert_not_called()

    def test_draw_hud_abort_on_normal_file(self):
        """Should abort if the file is a standard .blend project (not a snapshot)."""
        mock_context = MagicMock()
        mock_context.area.type = "VIEW_3D"
        mock_context.blend_data.filepath = "/path/to/my_project.blend"
        type(mock_bpy).context = PropertyMock(return_value=mock_context)

        savepoints.hud.draw_hud()

        mock_blf.draw.assert_not_called()

    def test_draw_hud_render_in_snapshot_mode(self):
        """Should execute drawing commands when in Snapshot Mode."""
        # Setup Snapshot Context
        mock_context = MagicMock()
        mock_context.area.type = "VIEW_3D"

        # 修正1: core.py のロジックを通過するように正しい命名規則にする (.history -> .my_project_history)
        mock_context.blend_data.filepath = "/path/to/.my_project_history/v001/snapshot.blend_snapshot"

        mock_context.region.width = 800
        mock_context.region.height = 600

        # 修正2: HUDコード内で使用している ui_scale の値を設定する (これがないと計算でエラーになる)
        mock_context.preferences.system.ui_scale = 1.0

        type(mock_bpy).context = PropertyMock(return_value=mock_context)

        # Setup Drawing Mocks
        mock_blf.dimensions.return_value = (100, 20)
        mock_gpu.shader.from_builtin.return_value = MagicMock()
        mock_gpu_batch.batch_for_shader.return_value = MagicMock()

        savepoints.hud.draw_hud()

        # Verify: 4 corners of text + 1 border batch
        self.assertEqual(mock_blf.draw.call_count, 4)
        mock_gpu.shader.from_builtin.assert_called()
        mock_gpu_batch.batch_for_shader.assert_called()

    def test_register_unregister(self):
        """Should correctly add and remove the draw handler."""
        savepoints.hud._draw_handler = None
        mock_bpy.types.SpaceView3D.draw_handler_add.return_value = "HANDLER_REF"

        # Test Register
        savepoints.hud.register()
        mock_bpy.types.SpaceView3D.draw_handler_add.assert_called_once()
        self.assertIsNotNone(savepoints.hud._draw_handler)

        # Test Unregister
        savepoints.hud.unregister()
        mock_bpy.types.SpaceView3D.draw_handler_remove.assert_called_once_with("HANDLER_REF", 'WINDOW')
        self.assertIsNone(savepoints.hud._draw_handler)


if __name__ == '__main__':
    unittest.main()
