# SPDX-License-Identifier: GPL-3.0-or-later
import os
import shutil

import bpy

from .services.export import create_glb_export_executor, process_export_failure


class SAVEPOINTS_OT_export_glb(bpy.types.Operator):
    bl_idname = "savepoints.export_glb"
    bl_label = "Export GLB (Background)"
    bl_description = (
        "Export selected objects from the specified version to .glb in background"
    )

    _timer = None
    _executor = None

    def execute(self, context):
        return self.invoke(context, None)

    def invoke(self, context, event):
        settings = context.scene.savepoints_settings
        if settings.active_version_index < 0 or settings.active_version_index >= len(
            settings.versions
        ):
            self.report({"ERROR"}, "No version selected")
            return {"CANCELLED"}

        version = settings.versions[settings.active_version_index]

        # Get selected objects in the CURRENT scene
        selected_objects = [obj.name for obj in context.selected_objects]
        if not selected_objects:
            self.report({"ERROR"}, "No objects selected in current scene")
            return {"CANCELLED"}

        try:
            self._executor = create_glb_export_executor(
                version=version,
                object_names=selected_objects,
                output_dir_raw=settings.glb_export_path,
                filename_template=settings.glb_export_filename,
            )
        except ValueError as e:
            self.report({"ERROR"}, str(e))
            return {"CANCELLED"}
        except OSError as e:
            self.report({"ERROR"}, f"File System Error: {e}")
            return {"CANCELLED"}
        except Exception as e:
            self.report({"ERROR"}, f"Unexpected Error: {e}")
            return {"CANCELLED"}

        # Start modal
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.5, window=context.window)
        wm.modal_handler_add(self)

        self.report(
            {"INFO"}, f"Started background export for version {version.version_id}"
        )
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type == "TIMER":
            if self._executor:
                status = self._executor.update()

                if status["status"] == "FINISHED":
                    self.report({"INFO"}, "Export Process Finished")
                    return self.finish(context)
                elif status["status"] == "TASK_FINISHED":
                    if status.get("return_code") != 0:
                        self.report(
                            {"ERROR"}, f"Export failed for {status['version_id']}"
                        )
                        process_export_failure(status)
                    else:
                        self.report(
                            {"INFO"}, f"Exported {status['version_id']} successfully"
                        )
                elif status["status"] == "CANCELLED":
                    self.report({"WARNING"}, "Export Cancelled")
                    return self.finish(context)

        return {"PASS_THROUGH"}

    def finish(self, context):
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)
        if (
            self._executor
            and self._executor.temp_dir
            and os.path.exists(self._executor.temp_dir)
        ):
            try:
                shutil.rmtree(self._executor.temp_dir)
            except Exception as e:
                print(f"Failed to cleanup temp dir: {e}")
        self._executor = None
        return {"FINISHED"}
