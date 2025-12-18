# SPDX-License-Identifier: GPL-3.0-or-later

import zipfile
from pathlib import Path

import bpy
from bpy_extras.io_utils import ExportHelper

from .services.storage import get_history_dir_for_path


class SAVEPOINTS_OT_export_project_zip(bpy.types.Operator, ExportHelper):
    """Export the current project and its history as a ZIP archive"""
    bl_idname = "savepoints.export_project_zip"
    bl_label = "SavePoints Project (.zip)"
    bl_description = "Export current project and history as ZIP"

    filename_ext = ".zip"

    filter_glob: bpy.props.StringProperty(
        default="*.zip",
        options={'HIDDEN'},
        maxlen=255,
    )

    def invoke(self, context, event):
        if not bpy.data.is_saved:
            self.report({'ERROR'}, "Save the file first")
            return {'CANCELLED'}

        # Ensure default filename is set correctly
        if not self.filepath:
            filepath = bpy.data.filepath
            stem = Path(filepath).stem
            self.filepath = f"{stem}.zip"

        return super().invoke(context, event)

    def execute(self, context):
        if not bpy.data.is_saved:
            self.report({'ERROR'}, "Project must be saved before exporting.")
            return {'CANCELLED'}

        project_path = Path(bpy.data.filepath)
        # Get history directory using core utility
        history_dir_str = get_history_dir_for_path(str(project_path))
        history_dir = Path(history_dir_str) if history_dir_str else None

        output_zip_path = Path(self.filepath)

        if context.window:
            context.window.cursor_set("WAIT")
        wm = context.window_manager
        wm.progress_begin(0, 100)

        try:
            with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_STORED) as zf:
                # 1. Add the main .blend file
                zf.write(project_path, arcname=project_path.name)

                # 2. Add the history directory if it exists
                if history_dir and history_dir.exists():
                    # Collect all files to calculate progress
                    files_to_zip = [f for f in history_dir.rglob('*') if f.is_file()]
                    total_files = len(files_to_zip) + 1  # +1 for main blend file

                    processed = 1
                    wm.progress_update(int(processed / total_files * 100))

                    for file_path in files_to_zip:
                        # Create arcname relative to the project root (parent of .blend file)
                        # e.g., /path/to/.history/v001/file -> .history/v001/file
                        arcname = file_path.relative_to(project_path.parent)
                        zf.write(file_path, arcname=arcname)

                        processed += 1
                        wm.progress_update(int(processed / total_files * 100))

            self.report({'INFO'}, f"Exported project to {output_zip_path.name}")
            return {'FINISHED'}

        except Exception as e:
            self.report({'ERROR'}, f"Export failed: {str(e)}")
            return {'CANCELLED'}

        finally:
            wm.progress_end()
            if context.window:
                context.window.cursor_set("DEFAULT")


def menu_func(self, context):
    self.layout.operator(SAVEPOINTS_OT_export_project_zip.bl_idname, text="SavePoints Project (.zip)")


def register():
    bpy.utils.register_class(SAVEPOINTS_OT_export_project_zip)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)


def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)
    bpy.utils.unregister_class(SAVEPOINTS_OT_export_project_zip)
