# SPDX-License-Identifier: GPL-3.0-or-later

import time

import bpy
from .snapshot import create_snapshot
from .storage import get_parent_path_from_snapshot
from .versioning import delete_version_by_id

UNSAFE_MODES = {
    "SCULPT",
    "PAINT_VERTEX",
    "PAINT_WEIGHT",
    "PAINT_TEXTURE",
    "PAINT_GPENCIL",
    "SCULPT_GPENCIL",
    "SCULPT_CURVES",
    "EDIT_MESH",
}


def is_rendering():
    """Check if a render job is running."""
    return bpy.app.is_job_running("RENDER")


class AutoSaveManager:
    def __init__(self, context):
        self.context = context
        self.check_interval = 5.0
        self.scene = getattr(context, "scene", None)
        self.settings = (
            getattr(self.scene, "savepoints_settings", None) if self.scene else None
        )

    def should_run(self):
        if not self.scene or not self.settings:
            return False
        return self.settings.use_auto_save

    def get_last_save_time(self):
        if not self.settings:
            return 0.0
        try:
            return float(self.settings.last_autosave_timestamp)
        except ValueError:
            return 0.0

    def initialize_timestamp(self, now):
        if not self.settings:
            return False
        if self.get_last_save_time() == 0.0:
            self.settings.last_autosave_timestamp = str(now)
            return True
        return False

    @staticmethod
    def is_snapshot_mode():
        if not bpy.data.filepath:
            return False
        return bool(get_parent_path_from_snapshot(bpy.data.filepath))

    def _tag_redraw(self):
        for window in self.context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == "VIEW_3D":
                    area.tag_redraw()

    @property
    def is_dirty(self):
        return bpy.data.is_dirty

    def update_warning(self, now):
        if not self.settings:
            return

        last_save = self.get_last_save_time()
        interval_min = max(1, self.settings.auto_save_interval)

        minutes_since_save = (now - last_save) / 60.0
        threshold_minutes = max(15, interval_min + 5)

        should_warn = self.is_dirty and minutes_since_save > threshold_minutes

        if should_warn:
            self.settings.show_autosave_warning = True
            self.settings.autosave_warning_message = f"Not auto-saved for {int(minutes_since_save)} min. Switch to Object Mode."
            self._tag_redraw()
        else:
            if self.settings.show_autosave_warning:
                self.settings.show_autosave_warning = False
                self._tag_redraw()

    def can_save(self, now):
        if not self.settings:
            return False

        if self.context.mode in UNSAFE_MODES:
            return False

        if is_rendering():
            return False

        last_save = self.get_last_save_time()
        interval_min = max(1, self.settings.auto_save_interval)
        interval_sec = interval_min * 60.0

        if (now - last_save) < interval_sec:
            return False

        return True

    def execute_save(self):
        if not self.settings:
            return

        try:
            delete_version_by_id("autosave", use_trash=False)
            create_snapshot(self.context, "autosave", "Auto Save", skip_thumbnail=True)
            self.settings.last_autosave_timestamp = str(time.time())
            # Clear warning if save successful
            self.settings.show_autosave_warning = False
        except Exception as e:
            print(f"SavePoints: Auto Save execution failed: {e}")

    def process(self):
        try:
            if not self.should_run():
                return self.check_interval

            now = time.time()

            if self.initialize_timestamp(now):
                return self.check_interval

            if not bpy.data.filepath:
                return self.check_interval

            if self.is_snapshot_mode():
                return self.check_interval

            self.update_warning(now)

            if self.can_save(now):
                self.execute_save()

            return self.check_interval
        except Exception as e:
            print(f"SavePoints: Auto Save timer error: {e}")
            return self.check_interval


def autosave_timer():
    """Timer function for auto-save."""
    manager = AutoSaveManager(bpy.context)
    return manager.process()
