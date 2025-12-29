# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

from .services.asset_path import unmap_snapshot_paths
from .services.rescue import delete_rescue_temp_file


class RescuePostLoadHandler:
    """
    Handler to fix asset paths and cleanup temporary files after rescue operation.
    Also monitors the File Browser to detect cancellation.
    """

    def __init__(self, temp_blend_path, initial_obj_count):
        self.temp_blend_path = temp_blend_path
        self.initial_obj_count = initial_obj_count
        self.browser_seen = False

    def __call__(self, scene, _):
        if self._check_and_cleanup():
            pass

    def register(self):
        bpy.app.handlers.depsgraph_update_post.append(self)
        # Start monitoring the file browser to detect cancellation
        bpy.app.timers.register(self.monitor_file_browser, first_interval=0.2)

    def unregister(self):
        if self in bpy.app.handlers.depsgraph_update_post:
            bpy.app.handlers.depsgraph_update_post.remove(self)

    def monitor_file_browser(self):
        # Stop if we are already unregistered (e.g. by success in __call__)
        if self not in bpy.app.handlers.depsgraph_update_post:
            return None

        return self._monitor_browser_step(bpy.context)

    def _monitor_browser_step(self, context):
        # Check for File Browser
        is_browser_open = False
        if hasattr(context, "window_manager"):
            for window in context.window_manager.windows:
                for area in window.screen.areas:
                    if area.type == 'FILE_BROWSER':
                        is_browser_open = True
                        break
                if is_browser_open:
                    break

        # State transition logic
        if is_browser_open:
            self.browser_seen = True

        if self.browser_seen and not is_browser_open:
            # Browser was open, now closed.
            # Check for changes one last time (in case depsgraph didn't fire or we missed it)
            if self._check_and_cleanup():
                return None  # Cleanup done, stop timer
            else:
                # No changes detected -> Cancelled
                print("[SavePoints] Rescue cancelled or empty. Cleaning up temp file.")
                self.cleanup_temp_file()
                self.unregister()
                return None  # Stop timer

        return 0.5  # Continue monitoring

    def _check_and_cleanup(self) -> bool:
        """
        Check if changes occurred (objects added or paths fixed).
        If yes, unregister and cleanup.
        Returns True if cleanup was performed.
        """
        # Check if append actually happened (objects added or paths fixed)
        current_obj_count = len(bpy.data.objects)
        paths_fixed = False
        try:
            paths_fixed = unmap_snapshot_paths()
        except Exception as e:
            print(f"[SavePoints] Error fixing paths after rescue: {e}")

        # If objects were added OR paths were modified, we assume the user is done with the file
        has_changes = (current_obj_count != self.initial_obj_count) or paths_fixed

        if has_changes:
            self.unregister()
            self.cleanup_temp_file()
            return True

        return False

    def cleanup_temp_file(self):
        delete_rescue_temp_file(self.temp_blend_path)
