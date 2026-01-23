# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import shutil
import tempfile

import bpy

from .services.batch_executor import BatchRenderExecutor
from .services.batch_render import extract_render_settings, get_worker_script_path, get_batch_render_output_dir, \
    create_error_log_text_block
from .services.post_process import open_folder_platform_independent, create_vse_timelapse, send_os_notification, \
    launch_timelapse_mp4_generation
from .services.selection import get_selected_versions


def draw_batch_dialog(operator, layout, context):
    """Draws the content of the batch render dialog."""
    scene = context.scene
    settings = scene.savepoints_settings

    # Dry Run Toggle
    row = layout.row()
    row.scale_y = 1.2
    row.prop(operator, "dry_run", toggle=True)

    if operator.dry_run:
        _draw_dry_run_info(layout)
    else:
        _draw_final_render_info(layout, scene, settings)


def _draw_dry_run_info(layout):
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


def _draw_final_render_info(layout, scene, settings):
    count = len(get_selected_versions(settings))
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

    # Format Display Logic
    fmt = settings.batch_output_format
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

    # Timelapse Settings
    sub.separator()
    row = sub.row()
    row.prop(settings, "batch_create_mp4")
    if settings.batch_create_mp4:
        row.label(text="", icon='FILE_MOVIE')
        split = sub.split(factor=0.05)
        split.separator()
        col_sub = split.column(align=True)
        col_sub.prop(settings, "batch_burn_in")
        if settings.batch_burn_in:
            col_sub.prop(settings, "batch_burn_in_pos")

    box.label(text="This may take a while.", icon='INFO')


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

    def draw(self, context):
        draw_batch_dialog(self, self.layout, context)

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Blend file must be saved before batch rendering.")
            return {'CANCELLED'}

        try:
            self._prepare_execution(context)
        except Exception as e:
            self.report({'ERROR'}, str(e))
            if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
            return {'CANCELLED'}

        total_tasks = len(self.target_versions)
        self.report({'INFO'}, f"Batch Render Started: {total_tasks} versions.")
        context.window_manager.progress_begin(0, total_tasks)

        self._timer = context.window_manager.event_timer_add(0.5, window=context.window)
        context.window_manager.modal_handler_add(self)

        return self._handle_executor_update(context)

    def modal(self, context, event):
        if event.type == 'TIMER':
            return self._handle_executor_update(context)
        elif event.type == 'ESC':
            self.executor.cancel()
            self.report({'WARNING'}, "Batch Render Cancelled by User.")
            return self.finish(context)

        return {'PASS_THROUGH'}

    def _prepare_execution(self, context):
        """Initializes directories, json config, and executor."""
        self.settings = context.scene.savepoints_settings
        self.target_versions = get_selected_versions(self.settings)

        if not self.target_versions:
            raise Exception("No versions found to render.")

        self.temp_dir = tempfile.mkdtemp(prefix="sp_batch_")
        self.settings_path = os.path.join(self.temp_dir, "render_config.json")
        self.worker_script_path = get_worker_script_path()

        if not os.path.exists(self.worker_script_path):
            raise FileNotFoundError(f"Worker script not found at {self.worker_script_path}")

        try:
            render_settings = extract_render_settings(context, dry_run=self.dry_run)
            with open(self.settings_path, 'w') as f:
                json.dump(render_settings, f, indent=4)
        except Exception as e:
            raise Exception(f"Initialization failed: {e}")

        self.output_dir = get_batch_render_output_dir(dry_run=self.dry_run)
        os.makedirs(self.output_dir, exist_ok=True)

        self.executor = BatchRenderExecutor(
            tasks=self.target_versions,
            temp_dir=self.temp_dir,
            output_dir=self.output_dir,
            settings_path=self.settings_path,
            worker_script_path=self.worker_script_path,
            blender_bin=bpy.app.binary_path
        )

    def _handle_executor_update(self, context):
        """Delegates update logic to executor and handles status."""
        status_info = self.executor.update()
        status = status_info.get('status')

        if status == 'TASK_FINISHED':
            self._on_task_finished(context, status_info)
        elif status == 'SKIPPED':
            self._on_task_skipped(context, status_info)
        elif status == 'FINISHED':
            return self.finish(context)
        elif status == 'CANCELLED':
            return self.finish(context)

        return {'RUNNING_MODAL'}

    def _on_task_finished(self, context, info):
        vid = info['version_id']
        if info['return_code'] == 0:
            self.report({'INFO'}, f"Finished: {vid}")
        else:
            self.report({'ERROR'}, f"Failed: {vid} (Code {info['return_code']})")
            create_error_log_text_block(vid, info['log_path'])
            self.report({'WARNING'}, f"Check Text Editor 'Log_{vid}' for details.")

        context.window_manager.progress_update(info['progress'][0])
        msg = f"SavePoints Batch: Processed {info['progress'][0]}/{info['progress'][1]} versions..."
        context.workspace.status_text_set(msg)

    def _on_task_skipped(self, context, info):
        self.report({'WARNING'}, f"Skipping {info['version_id']}: File not found.")
        context.window_manager.progress_update(info['progress'][0])

    def finish(self, context):
        # Cleanup UI
        context.window_manager.progress_end()
        context.workspace.status_text_set(None)

        if self._timer:
            context.window_manager.event_timer_remove(self._timer)

        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass

        # Check Results
        completed_count = 0
        is_cancelled = False
        if hasattr(self, 'executor'):
            completed_count = self.executor.current_task_idx
            is_cancelled = self.executor.is_cancelled

        if completed_count > 0:
            if is_cancelled:
                self.report({'WARNING'}, f"Batch Render Interrupted. ({completed_count} completed)")
            else:
                self.report({'INFO'}, f"Batch Render Complete! ({completed_count} versions)")

            open_folder_platform_independent(self.output_dir)

            if not self.dry_run and not is_cancelled:
                self._process_timelapse_creation(context)
                send_os_notification("SavePoints Batch Render", f"Completed! {completed_count} versions.")
        else:
            self.report({'WARNING'}, "Batch Render finished but no tasks were completed.")

        return {'FINISHED'}

    def _process_timelapse_creation(self, context):
        """Handles VSE creation and Background MP4 generation."""
        try:
            scene_name = create_vse_timelapse(self.output_dir)

            mp4_triggered = False
            if context.scene.savepoints_settings.batch_create_mp4:
                output_file = os.path.join(self.output_dir, "timelapse.mp4")
                success = launch_timelapse_mp4_generation(
                    self.output_dir,
                    output_file,
                    context.scene.render.fps,
                    context.scene.savepoints_settings.batch_burn_in,
                    context.scene.savepoints_settings.batch_burn_in_pos
                )
                if success:
                    mp4_triggered = True
                    self.report({'INFO'}, "MP4 generation started in background...")
                else:
                    self.report({'ERROR'}, "Failed to start MP4 generation.")

            if scene_name and not bpy.app.background:
                count = self.executor.current_task_idx if hasattr(self, 'executor') else 0
                self._show_timelapse_notification(context, scene_name, mp4_triggered, count)
            elif not scene_name:
                self.report({'WARNING'}, "Could not create timelapse scene.")

        except Exception as e:
            print(f"[SavePoints] Post-process error: {e}")
            import traceback
            traceback.print_exc()

    def _show_timelapse_notification(self, context, scene_name, mp4_triggered, count):
        def draw_notification(self, _context):
            layout = self.layout
            layout.label(text=f"Successfully processed {count} versions.")
            layout.separator()
            layout.label(text="Auto-Timelapse created:", icon='SEQUENCE')
            layout.label(text=f"  Scene: {scene_name}")
            layout.label(text="  (Switch scene to view playback)", icon='INFO')

            if mp4_triggered:
                layout.separator()
                layout.label(text="Exporting MP4 in background...", icon='FILE_MOVIE')
                layout.label(text="Check folder later.", icon='FILE_FOLDER')

        context.window_manager.popup_menu(draw_notification, title="Batch Render Complete", icon='CHECKMARK')


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
            if not v.version_id.startswith('v'):
                continue
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
