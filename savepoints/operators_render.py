# SPDX-License-Identifier: GPL-3.0-or-later
import json
import os
import shutil
import subprocess
import tempfile

import bpy

from .services.batch_render import extract_render_settings, get_worker_script_content, get_batch_render_output_dir, \
    create_error_log_text_block
from .services.post_process import open_folder_platform_independent, create_vse_timelapse, send_os_notification
from .services.selection import get_selected_versions
from .services.snapshot import find_snapshot_path


class SAVEPOINTS_OT_batch_render(bpy.types.Operator):
    """Batch Render selected versions. (Shift+Click to Skip Dialog & RENDER)"""
    bl_idname = "savepoints.batch_render"
    bl_label = "Batch Render Snapshots"
    bl_options = {'REGISTER'}

    _timer = None
    _process = None

    dry_run: bpy.props.BoolProperty(
        name="Dry Run (Low Quality)",
        description="Render low quality JPEG for quick check (_dryrun suffix)",
        default=False
    )

    def invoke(self, context, event):
        if event.shift:
            self.dry_run = False
            self.report({'INFO'}, "🚀 Instant Batch Render Started! (Shift+Click)")
            return self.execute(context)
        return context.window_manager.invoke_props_dialog(self, width=400)

    def check(self, context):
        return True

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.scale_y = 1.2
        row.prop(self, "dry_run", toggle=True)

        if self.dry_run:
            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text="🚀 DRY RUN MODE", icon='TIME')

            col.separator()
            col.label(text="• Resolution: 25% (Fast)")
            col.label(text="• Samples: 1 + Denoise")
            col.label(text="• Output: JPEG (Quality 70)")
            col.label(text="• Folder: ..._dryrun")

            box.label(text="Files will be saved for quick review.", icon='INFO')

        else:
            count = len(get_selected_versions(context.scene.savepoints_settings))

            box = layout.box()
            col = box.column(align=True)
            row = col.row()
            row.alignment = 'CENTER'
            row.label(text=f"🎬 FINAL RENDER ({count} Versions)", icon='RENDER_STILL')

            col.separator()
            col.label(text="• Settings: User Defined / Override")
            col.label(text="• Output: Selected Format")

            box.label(text="This may take a while.", icon='ERROR')

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Blend file must be saved before batch rendering.")
            return {'CANCELLED'}

        self.settings = context.scene.savepoints_settings

        self.target_versions = get_selected_versions(self.settings)

        if not self.target_versions:
            self.report({'WARNING'}, "No versions found to render.")
            return {'CANCELLED'}

        self.temp_dir = tempfile.mkdtemp(prefix="sp_batch_")
        self.settings_path = os.path.join(self.temp_dir, "render_config.json")
        self.worker_script_path = os.path.join(self.temp_dir, "worker_render.py")

        try:
            render_settings = extract_render_settings(context, dry_run=self.dry_run)
            with open(self.settings_path, 'w') as f:
                json.dump(render_settings, f, indent=4)

            with open(self.worker_script_path, 'w') as f:
                f.write(get_worker_script_content())
        except Exception as e:
            self.report({'ERROR'}, f"Initialization failed: {e}")
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
            return {'CANCELLED'}

        self.output_dir = get_batch_render_output_dir(dry_run=self.dry_run)
        os.makedirs(self.output_dir, exist_ok=True)

        self.task_queue = list(self.target_versions)
        self.total_tasks = len(self.task_queue)
        self.current_task_idx = 0
        self.current_version_id = ""

        self.report({'INFO'}, f"Batch Render Started: {self.total_tasks} versions.")
        context.window_manager.progress_begin(0, self.total_tasks)

        self._timer = context.window_manager.event_timer_add(0.5, window=context.window)
        context.window_manager.modal_handler_add(self)

        if not self.start_next_render(context):
            return self.finish(context)

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'TIMER':
            if self._process:
                ret_code = self._process.poll()

                if ret_code is None:
                    return {'PASS_THROUGH'}
                else:
                    if self.current_log_handle:
                        self.current_log_handle.close()
                        self.current_log_handle = None

                    if ret_code == 0:
                        self.report({'INFO'}, f"Finished: {self.current_version_id}")
                    else:
                        error_msg = f"Failed: {self.current_version_id} (Code {ret_code})"
                        self.report({'ERROR'}, error_msg)

                        create_error_log_text_block(self.current_version_id, self.current_log_path)
                        self.report({'WARNING'}, f"Check Text Editor 'Log_{self.current_version_id}' for details.")

                    self._process = None
                    self.current_task_idx += 1
                    context.window_manager.progress_update(self.current_task_idx)

                    if not self.start_next_render(context):
                        return self.finish(context)

        elif event.type == 'ESC':
            self.report({'WARNING'}, "Batch Render Cancelled.")
            self.cancel_process()
            return self.finish(context)

        return {'PASS_THROUGH'}

    def start_next_render(self, context):
        if self._process:
            return True

        while self.task_queue:
            version = self.task_queue.pop(0)
            self.current_version_id = version.version_id

            snapshot_path = find_snapshot_path(version.version_id)
            if not snapshot_path or not snapshot_path.exists():
                self.report({'WARNING'}, f"Skipping {version.version_id}: File not found.")
                self.current_task_idx += 1
                context.window_manager.progress_update(self.current_task_idx)
                continue

            # Found valid snapshot, proceed with render
            break
        else:
            # No more tasks
            return False

        blender_bin = bpy.app.binary_path

        log_filename = f"render_log_{self.current_version_id}.txt"
        self.current_log_path = os.path.join(self.temp_dir, log_filename)
        self.current_log_handle = open(self.current_log_path, 'w', encoding='utf-8')

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
                stdout=self.current_log_handle,
                stderr=self.current_log_handle
            )
            print(f"[SavePoints] Rendering {self.current_version_id} (PID: {self._process.pid})")
            return True
        except Exception as e:
            self.report({'ERROR'}, f"Process start failed: {e}")

            if self.current_log_handle:
                self.current_log_handle.close()
                self.current_log_handle = None

            # Set flag to signal modal to finish
            self.task_queue.clear()
            self._process = None
            return False

    def cancel_process(self):
        if self._process:
            try:
                self._process.kill()
            except OSError:
                pass
            self._process = None

        if hasattr(self, 'current_log_handle') and self.current_log_handle:
            self.current_log_handle.close()
            self.current_log_handle = None

    def finish(self, context):
        context.window_manager.progress_end()
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)

        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass

        if self.current_task_idx > 0:
            print(f"[SavePoints] Batch Render Complete! Processed {self.current_task_idx} versions.")
            self.report({'INFO'}, f"Batch Render Complete! ({self.current_task_idx} versions)")

            open_folder_platform_independent(self.output_dir)

            try:
                scene_name = create_vse_timelapse(self.output_dir)

                if scene_name:
                    def draw_notification(self, context):
                        self.layout.label(text="Timelapse Scene Created!")
                        row = self.layout.row()
                        row.label(text=f"Scene: {scene_name}")

                    context.window_manager.popup_menu(draw_notification, title="Render Finished", icon='SEQUENCE')
                    self.report({'INFO'}, f"Timelapse scene created: '{scene_name}'")
                else:
                    self.report({'WARNING'}, "Could not create timelapse scene (Check System Console).")

            except Exception as e:
                print(f"[SavePoints] Post-process error: {e}")
                import traceback
                traceback.print_exc()
                self.report({'WARNING'}, "Error during post-processing. See console.")

            send_os_notification(
                title="SavePoints Batch Render",
                message=f"Completed! {self.current_task_idx} versions rendered.",
            )

        else:
            self.report({'WARNING'}, "Batch Render finished but no tasks were completed.")

        return {'FINISHED'}


class SAVEPOINTS_OT_switch_scene(bpy.types.Operator):
    """Switch to the specified scene"""
    bl_idname = "savepoints.switch_scene"
    bl_label = "Switch Scene"

    scene_name: bpy.props.StringProperty()

    def execute(self, context):
        if self.scene_name not in bpy.data.scenes:
            self.report({'WARNING'}, f"Scene '{self.scene_name}' not found.")
            return {'CANCELLED'}

        if not context.window:
            self.report({'WARNING'}, "Cannot switch scene: No active window found.")
            return {'CANCELLED'}

        context.window.scene = bpy.data.scenes[self.scene_name]
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
