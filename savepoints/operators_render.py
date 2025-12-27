# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import shutil
import subprocess
import tempfile

import bpy

from .services.batch_render import extract_render_settings, get_worker_script_path, get_batch_render_output_dir, \
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
        scene = context.scene

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

            main_settings = scene.render.image_settings
            col.separator()
            sub = col.column(align=True)
            sub.scale_y = 0.8
            sub.label(text="Output Settings (Inherited):", icon='PREFERENCES')

            fmt = scene.savepoints_settings.batch_output_format
            if fmt == 'SCENE':
                fmt_label = main_settings.file_format
                details = f"{main_settings.color_mode}, {main_settings.color_depth}-bit"
                if fmt_label == 'JPEG':
                    details += f", Q:{main_settings.quality}"
                elif fmt_label == 'PNG':
                    details += f", Comp:{main_settings.compression}%"
            else:
                fmt_label = fmt
                details = "Override Active"

            sub.label(text=f"  Format: {fmt_label}")
            if fmt == 'SCENE':
                sub.label(text=f"  Details: {details}")

            box.label(text="This may take a while.", icon='INFO')

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
        self.worker_script_path = get_worker_script_path()
        if not os.path.exists(self.worker_script_path):
            self.report({'ERROR'}, f"Worker script not found at {self.worker_script_path}")
            return {'CANCELLED'}

        try:
            render_settings = extract_render_settings(context, dry_run=self.dry_run)
            with open(self.settings_path, 'w') as f:
                json.dump(render_settings, f, indent=4)
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
                    self._cleanup_current_log()

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
            self.report({'WARNING'}, "Batch Render Cancelled by User.")
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

            break
        else:
            return False

        blender_bin = bpy.app.binary_path
        log_filename = f"render_log_{self.current_version_id}.txt"
        self.current_log_path = os.path.join(self.temp_dir, log_filename)
        self.current_log_handle = open(self.current_log_path, 'w', encoding='utf-8')

        cmd = [
            blender_bin,
            "-b",
            "--factory-startup",
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
            self._cleanup_current_log()
            self._process = None
            return False

    def cancel_process(self):
        if self._process:
            print(f"[SavePoints] Killing process PID: {self._process.pid}")
            try:
                self._process.kill()
                self._process.wait(timeout=1)
            except Exception as e:
                print(f"Error killing process: {e}")
            self._process = None

        self._cleanup_current_log()

    def _cleanup_current_log(self):
        if hasattr(self, 'current_log_handle') and self.current_log_handle:
            try:
                self.current_log_handle.close()
            except:
                pass
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
            if not self._process:
                self.report({'INFO'}, f"Batch Render Complete! ({self.current_task_idx} versions)")
                open_folder_platform_independent(self.output_dir)

                if not self.dry_run:
                    self._process_timelapse_creation(context)

                send_os_notification(
                    title="SavePoints Batch Render",
                    message=f"Completed! {self.current_task_idx} versions rendered.",
                )
        else:
            if not self._process:
                self.report({'WARNING'}, "Batch Render finished but no tasks were completed.")

        return {'FINISHED'}

    def _process_timelapse_creation(self, context):
        try:
            scene_name = create_vse_timelapse(self.output_dir)
            if scene_name:
                self.report({'INFO'}, f"Timelapse scene created: '{scene_name}'")

                if not bpy.app.background:
                    count = self.current_task_idx

                    def draw_notification(self, context):
                        layout = self.layout
                        layout.label(text=f"Successfully processed {count} versions.")

                        layout.separator()

                        layout.label(text="Auto-Timelapse created:", icon='SEQUENCE')
                        row = layout.row()
                        row.label(text=f"  Scene: {scene_name}")
                        layout.label(text="  (Switch scene to view playback)", icon='INFO')

                    context.window_manager.popup_menu(
                        draw_notification,
                        title="Batch Render Complete",
                        icon='CHECKMARK'
                    )
            else:
                self.report({'WARNING'}, "Could not create timelapse scene.")

        except Exception as e:
            print(f"[SavePoints] Post-process error: {e}")
            import traceback
            traceback.print_exc()
            self.report({'WARNING'}, "Error during post-processing. See console.")


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
