# SPDX-License-Identifier: GPL-3.0-or-later
import json
import os
import shutil
import subprocess
import tempfile

import bpy

from .services.batch_render import extract_render_settings, get_worker_script_content
from .services.snapshot import find_snapshot_path


class SAVEPOINTS_OT_batch_render(bpy.types.Operator):
    """Batch Render selected versions without freezing UI"""
    bl_idname = "savepoints.batch_render"
    bl_label = "Batch Render Snapshots"
    bl_options = {'REGISTER'}

    _timer = None
    _process = None

    def invoke(self, context, event):
        self.settings = context.scene.savepoints_settings

        self.target_versions = [
            v for v in self.settings.versions
            if v.version_id.startswith('v') and v.selected
        ]

        if not self.target_versions:
            self.report({'WARNING'}, "No versions found to render.")
            return {'CANCELLED'}

        self.temp_dir = tempfile.mkdtemp(prefix="sp_batch_")
        self.settings_path = os.path.join(self.temp_dir, "render_config.json")
        self.worker_script_path = os.path.join(self.temp_dir, "worker_render.py")

        try:
            render_settings = extract_render_settings(context)
            with open(self.settings_path, 'w') as f:
                json.dump(render_settings, f, indent=4)

            with open(self.worker_script_path, 'w') as f:
                f.write(get_worker_script_content())
        except Exception as e:
            self.report({'ERROR'}, f"Initialization failed: {e}")
            return {'CANCELLED'}

        self.output_dir = os.path.join(bpy.path.abspath("//"), "renders_batch")
        os.makedirs(self.output_dir, exist_ok=True)

        self.task_queue = list(self.target_versions)
        self.total_tasks = len(self.task_queue)
        self.current_task_idx = 0
        self.current_version_id = ""

        self.report({'INFO'}, f"Batch Render Started: {self.total_tasks} versions.")
        context.window_manager.progress_begin(0, self.total_tasks)

        self._timer = context.window_manager.event_timer_add(0.5, window=context.window)
        context.window_manager.modal_handler_add(self)

        self.start_next_render()

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'TIMER':
            if self._process:
                ret_code = self._process.poll()

                if ret_code is None:
                    return {'PASS_THROUGH'}
                else:
                    if ret_code == 0:
                        self.report({'INFO'}, f"Finished: {self.current_version_id}")
                    else:
                        self.report({'ERROR'}, f"Failed: {self.current_version_id} (Code {ret_code})")

                    self._process = None
                    self.current_task_idx += 1
                    context.window_manager.progress_update(self.current_task_idx)

                    if self.task_queue:
                        self.start_next_render()
                    else:
                        return self.finish(context)

        elif event.type == 'ESC':
            self.report({'WARNING'}, "Batch Render Cancelled.")
            self.cancel_process()
            return self.finish(context)

        return {'PASS_THROUGH'}

    def start_next_render(self):
        if not self.task_queue:
            return

        version = self.task_queue.pop(0)
        self.current_version_id = version.version_id

        snapshot_path = find_snapshot_path(version.version_id)
        if not snapshot_path or not snapshot_path.exists():
            self.report({'WARNING'}, f"Skipping {version.version_id}: File not found.")
            self.current_task_idx += 1
            self.start_next_render()
            return

        blender_bin = bpy.app.binary_path

        cmd = [
            blender_bin,
            "-b",
            "--factory-startup",  # Clean environment
            str(snapshot_path),
            "-P", self.worker_script_path,
            "--",
            self.settings_path,
            self.output_dir,
            f"{version.version_id}_render"
        ]

        try:
            self._process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"[SavePoints] Rendering {self.current_version_id} (PID: {self._process.pid})")
        except Exception as e:
            self.report({'ERROR'}, f"Process start failed: {e}")
            self.cancel_process()
            return self.finish(bpy.context)

    def cancel_process(self):
        if self._process:
            try:
                self._process.kill()
            except OSError:
                pass
            self._process = None

    def finish(self, context):
        context.window_manager.progress_end()
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)

        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass

        return {'FINISHED'}


class SAVEPOINTS_OT_toggle_batch_mode(bpy.types.Operator):
    """Toggle Batch Operation Mode"""
    bl_idname = "savepoints.toggle_batch_mode"
    bl_label = "Toggle Batch Mode"
    bl_options = {'REGISTER'}

    def execute(self, context):
        settings = context.scene.savepoints_settings
        settings.is_batch_mode = not settings.is_batch_mode
        return {'FINISHED'}


class SAVEPOINTS_OT_select_all(bpy.types.Operator):
    """Select all visible versions for batch operations"""
    bl_idname = "savepoints.select_all"
    bl_label = "Select All"
    bl_options = {'REGISTER'}

    def execute(self, context):
        settings = context.scene.savepoints_settings
        filter_tag = settings.filter_tag

        for v in settings.versions:
            # Skip autosave or non-versions
            if not v.version_id.startswith('v'):
                continue

            # Apply Tag Filter
            match = True
            if filter_tag != 'ALL':
                if v.tag != filter_tag:
                    match = False

            if match:
                v.selected = True

        return {'FINISHED'}


class SAVEPOINTS_OT_deselect_all(bpy.types.Operator):
    """Deselect all versions"""
    bl_idname = "savepoints.deselect_all"
    bl_label = "Deselect All"
    bl_options = {'REGISTER'}

    def execute(self, context):
        settings = context.scene.savepoints_settings
        for v in settings.versions:
            v.selected = False
        return {'FINISHED'}
