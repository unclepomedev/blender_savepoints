# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import shutil
import tempfile

import bpy

from .services.batch_executor import BatchRenderExecutor
from .services.batch_render import extract_render_settings, get_worker_script_path, get_batch_render_output_dir, \
    create_error_log_text_block
from .services.post_process import open_folder_platform_independent, create_vse_timelapse, send_os_notification
from .services.selection import get_selected_versions


class SAVEPOINTS_OT_batch_render(bpy.types.Operator):
    """
    Batch Render selected versions. (Shift+Click to Skip Dialog & RENDER)

    NOTE: This operator runs Blender with '--factory-startup' flag for stability.
    - User addons and startup scripts are DISABLED during batch rendering.
    - Only data embedded in the blend file (shaders, modifiers, etc.) will be rendered.
    - Addons that generate content at render-time will not function.
    """
    bl_idname = "savepoints.batch_render"
    bl_label = "Batch Render Snapshots"
    bl_options = {'REGISTER'}

    _timer = None

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
        self._is_cancelled = False

        if not self.target_versions:
            self.report({'WARNING'}, "No versions found to render.")
            return {'CANCELLED'}

        self.temp_dir = tempfile.mkdtemp(prefix="sp_batch_")
        self.settings_path = os.path.join(self.temp_dir, "render_config.json")
        self.worker_script_path = get_worker_script_path()
        if not os.path.exists(self.worker_script_path):
            self.report({'ERROR'}, f"Worker script not found at {self.worker_script_path}")
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
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

        # Initialize Executor
        blender_bin = bpy.app.binary_path
        self.executor = BatchRenderExecutor(
            tasks=self.target_versions,
            temp_dir=self.temp_dir,
            output_dir=self.output_dir,
            settings_path=self.settings_path,
            worker_script_path=self.worker_script_path,
            blender_bin=blender_bin
        )

        total_tasks = len(self.target_versions)
        self.report({'INFO'}, f"Batch Render Started: {total_tasks} versions.")
        context.window_manager.progress_begin(0, total_tasks)

        self._timer = context.window_manager.event_timer_add(0.5, window=context.window)
        context.window_manager.modal_handler_add(self)

        # Initial update to start first task or finish if empty
        status_info = self.executor.update()
        if status_info.get('status') == 'FINISHED':
            return self.finish(context)

        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'TIMER':
            status_info = self.executor.update()
            status = status_info.get('status')

            if status == 'TASK_FINISHED':
                version_id = status_info.get('version_id')
                ret_code = status_info.get('return_code')
                log_path = status_info.get('log_path')
                progress = status_info.get('progress')

                if ret_code == 0:
                    self.report({'INFO'}, f"Finished: {version_id}")
                else:
                    error_msg = f"Failed: {version_id} (Code {ret_code})"
                    self.report({'ERROR'}, error_msg)
                    create_error_log_text_block(version_id, log_path)
                    self.report({'WARNING'}, f"Check Text Editor 'Log_{version_id}' for details.")

                context.window_manager.progress_update(progress[0])
                msg = f"SavePoints Batch: Processed {progress[0]}/{progress[1]} versions..."
                context.workspace.status_text_set(msg)

            elif status == 'SKIPPED':
                version_id = status_info.get('version_id')
                progress = status_info.get('progress')
                self.report({'WARNING'}, f"Skipping {version_id}: File not found.")
                context.window_manager.progress_update(progress[0])

            elif status == 'FINISHED':
                return self.finish(context)

            elif status == 'CANCELLED':
                return self.finish(context)

        elif event.type == 'ESC':
            self.executor.cancel()
            self.report({'WARNING'}, "Batch Render Cancelled by User.")
            return self.finish(context)

        return {'PASS_THROUGH'}

    def finish(self, context):
        context.window_manager.progress_end()
        context.workspace.status_text_set(None)

        if self._timer:
            context.window_manager.event_timer_remove(self._timer)

        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass

        completed_count = 0
        is_cancelled = False
        total_tasks = 0

        if hasattr(self, 'executor'):
            completed_count = self.executor.current_task_idx
            is_cancelled = self.executor.is_cancelled
            total_tasks = self.executor.total_tasks

        if completed_count > 0:
            if is_cancelled:
                self.report({'WARNING'},
                            f"Batch Render Interrupted. ({completed_count}/{total_tasks} completed)")
                open_folder_platform_independent(self.output_dir)

            else:
                self.report({'INFO'}, f"Batch Render Complete! ({completed_count} versions)")
                open_folder_platform_independent(self.output_dir)

                if not self.dry_run:
                    self._process_timelapse_creation(context)

                send_os_notification(
                    title="SavePoints Batch Render",
                    message=f"Completed! {completed_count} versions rendered.",
                )
        else:
            if is_cancelled:
                self.report({'WARNING'}, "Batch Render Cancelled.")
            else:
                self.report({'WARNING'}, "Batch Render finished but no tasks were completed.")

        return {'FINISHED'}

    def _process_timelapse_creation(self, context):
        try:
            scene_name = create_vse_timelapse(self.output_dir)
            if scene_name:
                self.report({'INFO'}, f"Timelapse scene created: '{scene_name}'")

                if not bpy.app.background:
                    count = self.executor.current_task_idx if hasattr(self, 'executor') else 0

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
