import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.handler_manager import RescuePostLoadHandler
from savepoints_test_case import SavePointsTestCase


class TestRescueSmartCleanup(SavePointsTestCase):
    def test_monitor_browser_cancel(self):
        """
        Verify that the timer detects browser opening and closing,
        and triggers cleanup if no changes occur (Cancel scenario).
        """
        print("Starting Rescue Smart Cleanup Test (Cancel)...")

        temp_file = self.test_dir / "temp_rescue.blend"
        temp_file.touch()

        # Setup Handler
        initial_count = len(bpy.data.objects)
        handler = RescuePostLoadHandler(temp_file, initial_count)

        # Register (just to put it in the list)
        handler.register()
        self.assertTrue(handler in bpy.app.handlers.depsgraph_update_post)

        # --- Simulation using _monitor_browser_step ---

        # 1. Step 1: Browser NOT YET open
        mock_ctx = MagicMock()
        mock_ctx.window_manager.windows = []

        res = handler._monitor_browser_step(mock_ctx)
        self.assertEqual(res, 0.5, "Should continue monitoring")
        self.assertFalse(handler.browser_seen)

        # 2. Step 2: Browser OPENS
        mock_area = MagicMock()
        mock_area.type = 'FILE_BROWSER'
        mock_window = MagicMock()
        mock_window.screen.areas = [mock_area]
        mock_ctx.window_manager.windows = [mock_window]

        res = handler._monitor_browser_step(mock_ctx)
        self.assertEqual(res, 0.5, "Should continue monitoring")
        self.assertTrue(handler.browser_seen, "Browser should be detected")

        # 3. Step 3: Browser CLOSES (Cancel)
        mock_area_3d = MagicMock()
        mock_area_3d.type = 'VIEW_3D'
        mock_window_3d = MagicMock()
        mock_window_3d.screen.areas = [mock_area_3d]
        mock_ctx.window_manager.windows = [mock_window_3d]

        with patch("savepoints.handler_manager.delete_rescue_temp_file") as mock_delete:
            res = handler._monitor_browser_step(mock_ctx)

            # Should detect close, check changes (None), and Cleanup
            self.assertIsNone(res, "Timer should stop")
            mock_delete.assert_called_with(temp_file)
            self.assertFalse(handler in bpy.app.handlers.depsgraph_update_post, "Handler should be unregistered")

    def test_monitor_browser_success(self):
        """
        Verify that if changes happen (Success), the normal flow handles it,
        and timer stops gracefully.
        """
        print("Starting Rescue Smart Cleanup Test (Success)...")

        temp_file = self.test_dir / "temp_rescue_success.blend"
        temp_file.touch()

        handler = RescuePostLoadHandler(temp_file, len(bpy.data.objects))
        handler.register()

        # 1. Browser Open
        mock_ctx = MagicMock()
        mock_area = MagicMock()
        mock_area.type = 'FILE_BROWSER'
        mock_window = MagicMock()
        mock_window.screen.areas = [mock_area]
        mock_ctx.window_manager.windows = [mock_window]

        handler._monitor_browser_step(mock_ctx)
        self.assertTrue(handler.browser_seen)

        # 2. Success happens (Depsgraph handler triggers)
        bpy.ops.mesh.primitive_cube_add()

        with patch("savepoints.handler_manager.delete_rescue_temp_file") as mock_delete:
            handler(bpy.context.scene, bpy.context.view_layer.depsgraph)

            self.assertFalse(handler in bpy.app.handlers.depsgraph_update_post)
            mock_delete.assert_called()

        # 3. Step 3 (Browser Closed)
        # Calling monitor_file_browser (wrapper) which checks handler list first
        # We can't call _monitor_browser_step directly because it doesn't check the list
        # But monitor_file_browser does.

        res = handler.monitor_file_browser()
        self.assertIsNone(res)


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
