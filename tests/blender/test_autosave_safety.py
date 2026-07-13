import sys
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.autosave import (
    autosave_timer,
    has_blocking_modal_operator,
)
from savepoints_test_case import SavePointsTestCase


class TestAutosaveSafety(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        # Enable autosave in settings
        self.settings = bpy.context.scene.savepoints_settings
        self.settings.use_auto_save = True
        self.settings.auto_save_interval = 1
        # Set last_autosave_timestamp to something old to trigger autosave
        self.settings.last_autosave_timestamp = str(time.time() - 100)

    def test_autosave_in_object_mode(self):
        """Test that autosave runs in OBJECT mode (Safe mode)"""
        # Ensure we have an active object to change modes safely
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="OBJECT")

        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"

        self.assertFalse(autosave_dir.exists())

        # Run timer
        autosave_timer()

        # It should have created a snapshot
        self.assertTrue(
            autosave_dir.exists(), "Autosave should have run in OBJECT mode"
        )
        self.assertTrue((autosave_dir / "snapshot.blend_snapshot").exists())

    def test_autosave_runs_in_edit_mesh_mode(self):
        """Test that an idle edit-mode session can be auto-saved."""
        # Ensure we have a mesh object to enter edit mode
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="EDIT")
        self.assertEqual(bpy.context.mode, "EDIT_MESH")

        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"

        # Run timer
        autosave_timer()

        self.assertTrue(autosave_dir.exists(), "Autosave should run in EDIT_MESH mode")

    def test_autosave_runs_in_sculpt_mode(self):
        """Test that an idle sculpt-mode session can be auto-saved."""
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="SCULPT")
        self.assertEqual(bpy.context.mode, "SCULPT")

        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"

        # Run timer
        autosave_timer()

        self.assertTrue(autosave_dir.exists(), "Autosave should run in SCULPT mode")

    def test_autosave_runs_in_weight_paint_mode(self):
        """Test that an idle weight-paint session can be auto-saved."""
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
        self.assertEqual(bpy.context.mode, "PAINT_WEIGHT")

        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"
        autosave_timer()
        self.assertTrue(
            autosave_dir.exists(), "Autosave should run in PAINT_WEIGHT mode"
        )

    def test_blocking_modal_operator_is_detected(self):
        """A running brush/transform must defer autosave until it finishes."""

        class BlockingOperator:
            bl_options = {"BLOCKING"}

        class Window:
            modal_operators = [BlockingOperator()]

        class WindowManager:
            windows = [Window()]

        self.assertTrue(has_blocking_modal_operator(WindowManager()))

    def test_non_blocking_modal_operator_does_not_defer_autosave(self):
        """Persistent non-blocking add-on modals must not disable autosave."""

        class NonBlockingOperator:
            bl_options = {"REGISTER"}

        class Window:
            modal_operators = [NonBlockingOperator()]

        class WindowManager:
            windows = [Window()]

        self.assertFalse(has_blocking_modal_operator(WindowManager()))

    def test_autosave_inhibited_during_render(self):
        """Test that autosave is inhibited when a render job is running"""
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="OBJECT")

        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"

        # Mock the helper function
        with patch(
            "savepoints.services.autosave.is_rendering", return_value=True
        ) as mock_render:
            autosave_timer()
            mock_render.assert_called_once()

        # It should NOT have created a snapshot
        self.assertFalse(
            autosave_dir.exists(), "Autosave should be inhibited during RENDER"
        )


if __name__ == "__main__":
    result = unittest.main(argv=["first-arg-is-ignored"], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
