import sys
import time
import unittest
from pathlib import Path
from unittest.mock import patch, PropertyMock

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.autosave import autosave_timer
from savepoints_test_case import SavePointsTestCase


class TestAutosaveWarning(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        self.settings = bpy.context.scene.savepoints_settings
        self.settings.use_auto_save = True
        self.settings.auto_save_interval = 1  # 1 minute

    def test_autosave_warning_triggered(self):
        """Test that autosave warning is triggered after threshold"""
        from savepoints.services.autosave import AutoSaveManager

        # Set last save to 20 minutes ago (threshold is max(15, 1+5) = 15 mins)
        # So 20 mins > 15 mins, should warn.
        self.settings.last_autosave_timestamp = str(time.time() - (20 * 60))

        bpy.ops.mesh.primitive_cube_add()

        # Keep the warning visible by simulating an active blocking operation,
        # which defers the save without relying on a blanket mode blacklist.
        with (
            patch.object(
                AutoSaveManager, "is_dirty", new_callable=PropertyMock
            ) as mock_dirty,
            patch(
                "savepoints.services.autosave.has_blocking_modal_operator",
                return_value=True,
            ),
        ):
            mock_dirty.return_value = True
            autosave_timer()

        self.assertTrue(self.settings.show_autosave_warning, "Warning should be shown")
        self.assertIn(
            "Not auto-saved for 20 min", self.settings.autosave_warning_message
        )

    def test_autosave_warning_cleared_on_save(self):
        """Test that warning is cleared after successful autosave"""
        # Trigger warning first
        self.settings.last_autosave_timestamp = str(time.time() - (20 * 60))
        self.settings.show_autosave_warning = True  # Force it just in case

        # Switch to SAFE mode
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.mode_set(mode="OBJECT")

        # Timer should run, save, and clear warning
        autosave_timer()

        # Autosave should have happened
        history_dir = self.test_dir / ".test_project_history"
        autosave_dir = history_dir / "autosave"
        self.assertTrue(autosave_dir.exists())

        # Warning should be cleared
        self.assertFalse(
            self.settings.show_autosave_warning, "Warning should be cleared after save"
        )

    def test_autosave_warning_not_shown_if_recent(self):
        """Test that warning is not shown if save was recent"""
        self.settings.last_autosave_timestamp = str(
            time.time() - (10 * 60)
        )  # 10 mins ago
        # Threshold is 15 mins.

        bpy.ops.mesh.primitive_cube_add()

        with patch(
            "savepoints.services.autosave.has_blocking_modal_operator",
            return_value=True,
        ):
            autosave_timer()

        self.assertFalse(self.settings.show_autosave_warning)


if __name__ == "__main__":
    result = unittest.main(argv=["first-arg-is-ignored"], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
