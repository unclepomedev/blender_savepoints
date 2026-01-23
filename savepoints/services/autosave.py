# SPDX-License-Identifier: GPL-3.0-or-later

import time

import bpy
from .snapshot import create_snapshot
from .storage import get_parent_path_from_snapshot
from .versioning import delete_version_by_id

UNSAFE_MODES = {
    'SCULPT',
    'PAINT_VERTEX',
    'PAINT_WEIGHT',
    'PAINT_TEXTURE',
    'PAINT_GPENCIL',
    'SCULPT_GPENCIL',
    'SCULPT_CURVES',
    'EDIT_MESH',
}


def is_rendering():
    """Check if a render job is running."""
    return bpy.app.is_job_running("RENDER")


def autosave_timer():
    """Timer function for auto-save."""
    check_interval = 5.0

    try:
        context = bpy.context
        if context.mode in UNSAFE_MODES:
            return check_interval

        if is_rendering():
            return check_interval

        scene = getattr(context, "scene", None)
        if not scene:
            return check_interval

        settings = getattr(scene, "savepoints_settings", None)
        if not settings:
            return check_interval

        if not settings.use_auto_save:
            return check_interval

        interval_min = settings.auto_save_interval
        if interval_min < 1:
            interval_min = 1

        interval_sec = interval_min * 60.0

        now = time.time()
        try:
            last_save = float(settings.last_autosave_timestamp)
        except ValueError:
            last_save = 0.0

        # If last_save is 0 (initial), set it to now so we don't save immediately
        if last_save == 0.0:
            settings.last_autosave_timestamp = str(now)
            return check_interval

        if (now - last_save) < interval_sec:
            return check_interval

        if not bpy.data.filepath:
            return check_interval

        if get_parent_path_from_snapshot(bpy.data.filepath):
            return check_interval

        try:
            delete_version_by_id("autosave", use_trash=False)
            create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)
            settings.last_autosave_timestamp = str(time.time())
        except Exception as e:
            print(f"SavePoints: Auto Save execution failed: {e}")

        return check_interval

    except Exception as e:
        print(f"SavePoints: Auto Save timer error: {e}")
        return check_interval
