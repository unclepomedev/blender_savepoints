# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from pathlib import Path

from .services.asset_path import unmap_snapshot_paths
from .services.backup import create_backup, HistoryDirectoryUnavailableError
from .services.fork import make_all_local_and_clear_assets
from .services.manifest import initialize_history_for_path
from .services.storage import (
    get_parent_path_from_snapshot,
    get_fork_target_path, SNAPSHOT_EXT,
)
from .ui_utils import force_redraw_areas


class SAVEPOINTS_OT_restore(bpy.types.Operator):
    """Restore this snapshot to the parent file, overwriting it."""
    bl_idname = "savepoints.restore"
    bl_label = "Save as Parent"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        original_path_str = get_parent_path_from_snapshot(bpy.data.filepath)

        if not original_path_str:
            self.report({'ERROR'}, "Could not determine parent file path. Are you in a snapshot?")
            return {'CANCELLED'}

        original_path = Path(original_path_str)

        # Verify if we can write to original path
        # Backup first
        if original_path.exists():
            try:
                backup_path = create_backup(original_path)
                self.report({'INFO'}, f"Backup created: {backup_path.name}")
            except HistoryDirectoryUnavailableError:
                self.report({'WARNING'}, "Could not create backup: history directory unavailable.")
            except Exception as e:
                self.report({'ERROR'}, f"Backup failed: {e}")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "Original file not found. Creating new one.")

        try:
            bpy.ops.wm.save_as_mainfile(filepath=str(original_path))
            self.report({'INFO'}, "Restored to parent file successfully.")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save: {e}")
            return {'CANCELLED'}

        # Force redraw to remove HUD
        force_redraw_areas(context)

        return {'FINISHED'}


class SAVEPOINTS_OT_open_parent(bpy.types.Operator):
    """Return to the parent file without saving current snapshot as parent."""
    bl_idname = "savepoints.open_parent"
    bl_label = "Return to Parent"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        parent_path_str = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path_str:
            self.report({'ERROR'}, "Could not determine parent file path. Are you in a snapshot?")
            return {'CANCELLED'}

        parent_path = Path(parent_path_str)

        if not parent_path.exists():
            self.report({'ERROR'}, f"Parent file not found: {parent_path}")
            return {'CANCELLED'}

        # Open the parent file
        # Note: In UI, this might prompt to save changes if modified.
        bpy.ops.wm.open_mainfile(filepath=str(parent_path))
        return {'FINISHED'}


class SAVEPOINTS_OT_fork_version(bpy.types.Operator):
    """Save the current snapshot as a new project file"""
    bl_idname = "savepoints.fork_version"
    bl_label = "Fork (Save as New)"
    bl_options = {'REGISTER', 'UNDO'}

    unbind_linked_assets: bpy.props.BoolProperty(
        name="Detach from Library (Make Local & Clear Assets)",
        description="Converts linked data to local and clears asset tags to prevent Asset Browser duplication. Creates a fully independent file (may increase file size).",
        default=False,
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "unbind_linked_assets")

    def execute(self, context):
        if not bpy.data.filepath:
            return {'CANCELLED'}

        source_path = Path(bpy.data.filepath)

        # Determine the target path
        try:
            target_path = get_fork_target_path(source_path)
        except Exception as e:
            self.report({'ERROR'}, f"Could not determine paths: {e}")
            return {'CANCELLED'}

        if source_path == target_path:
            self.report({'ERROR'}, "Source and target paths are identical.")
            return {'CANCELLED'}

        # Ensure history directory is created for the new file
        try:
            initialize_history_for_path(target_path)
        except Exception as e:
            self.report({'WARNING'}, f"History creation failed: {e}")

        try:
            # 1. Save to new location
            bpy.ops.wm.save_as_mainfile(filepath=str(target_path))

            needs_save = False

            if self.unbind_linked_assets:
                changed, cleared_count = make_all_local_and_clear_assets()
                if changed:
                    self.report({"INFO"}, f"Forked: Detached from library (Cleared {cleared_count} asset marks).")
                    needs_save = True
                else:
                    self.report({'INFO'}, "Forked: No linked assets required unbinding.")

            if unmap_snapshot_paths():
                self.report({'INFO'}, "Fixed relative paths for forked project.")
                needs_save = True

            if needs_save:
                bpy.ops.wm.save_mainfile()

        except Exception as e:
            self.report({'ERROR'}, f"Failed to fork file: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Forked to {target_path.name}")

        # Force redraw to remove HUD
        force_redraw_areas(context)

        return {'FINISHED'}


class SAVEPOINTS_OT_guard_save(bpy.types.Operator):
    """Intercept Ctrl+S to prevent saving over snapshots."""
    bl_idname = "savepoints.guard_save"
    bl_label = "Guard Save"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        filepath = bpy.data.filepath
        if filepath and filepath.lower().endswith(SNAPSHOT_EXT):
            msg = "Snapshot Mode (Review Mode): Please use Fork or Save as Parent."
            self.report({'WARNING'}, msg)

            if not bpy.app.background:
                def draw_popup(self, context):
                    layout = self.layout
                    layout.label(text="Snapshot Mode (Review Mode)")
                    layout.label(text="Please use 'Fork' or 'Save as Parent'.")

                context.window_manager.popup_menu(draw_popup, title="Save Prevented", icon='ERROR')

            return {'CANCELLED'}

        # Normal Save
        try:
            return bpy.ops.wm.save_mainfile('INVOKE_DEFAULT')
        except RuntimeError:
            # Can happen if cancelled or other internal issues, usually safe to ignore in wrapper
            return {'CANCELLED'}
