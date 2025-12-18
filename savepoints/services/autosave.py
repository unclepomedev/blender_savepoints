import time

import bpy

from .snapshot import create_snapshot
from .storage import get_parent_path_from_snapshot
from .versioning import delete_version_by_id


def autosave_timer():
    """Timer function for auto-save."""
    # Check every 5 seconds for responsiveness
    check_interval = 5.0

    try:
        context = bpy.context
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

        # Check if we can save
        if not bpy.data.filepath:
            return check_interval

        if get_parent_path_from_snapshot(bpy.data.filepath):
            return check_interval

        # Execute save
        delete_version_by_id("autosave")
        create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)
        settings.last_autosave_timestamp = str(time.time())

        return check_interval

    except Exception as e:
        print(f"Auto Save failed: {e}")
        return check_interval
