# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from .services.manifest import load_manifest
from .services.snapshot import create_snapshot, find_snapshot_path
from .services.storage import get_parent_path_from_snapshot
from .services.versioning import (
    get_next_version_id,
    delete_version_by_id,
    prune_versions,
    generate_default_note
)
from .ui_utils import sync_history_to_props
from .services.retrieve import cleanup_retrieve_temp_files


class SAVEPOINTS_OT_commit(bpy.types.Operator):
    """Save a new version of the current project"""
    bl_idname = "savepoints.commit"
    bl_label = "Save Version"
    bl_options = {'REGISTER', 'UNDO'}

    note: bpy.props.StringProperty(name="Commit Message", default="", options={'SKIP_SAVE'})
    force_quick: bpy.props.BoolProperty(name="Force Quick Save", default=False, options={'SKIP_SAVE', 'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return not bool(get_parent_path_from_snapshot(bpy.data.filepath))

    def invoke(self, context, event):
        settings = context.scene.savepoints_settings

        default_note = generate_default_note(context)

        if not self.note:
            self.note = default_note

        if settings.show_save_dialog and not self.force_quick:
            return context.window_manager.invoke_props_dialog(self)

        return self.execute(context)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "note")

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Save the project first!")
            return {'CANCELLED'}

        # Ensure default note is set if empty (especially for non-interactive execution)
        if not self.note:
            self.note = generate_default_note(context)

        manifest = load_manifest()
        new_id_str = get_next_version_id(manifest.get("versions", []))

        create_snapshot(context, new_id_str, self.note)

        # Auto Pruning
        settings = context.scene.savepoints_settings
        if settings.use_limit_versions and settings.max_versions_to_keep > 0:
            deleted = prune_versions(settings.max_versions_to_keep)
            if deleted > 0:
                sync_history_to_props(context)

        self.report({'INFO'}, f"Version {new_id_str} saved.")
        return {'FINISHED'}


class SAVEPOINTS_OT_checkout(bpy.types.Operator):
    """Restore selected version"""
    bl_idname = "savepoints.checkout"
    bl_label = "Checkout"
    bl_options = {'REGISTER', 'UNDO'}

    confirm_save: bpy.props.BoolProperty(
        name="Save current changes",
        description="Save current file before opening version",
        default=True,
        options={'SKIP_SAVE'}
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.alignment = 'LEFT'
        row.prop(self, "confirm_save")

    def invoke(self, context, event):
        if bpy.data.is_dirty:
            return context.window_manager.invoke_props_dialog(self)
        return self.execute(context)

    def execute(self, context):
        settings = context.scene.savepoints_settings
        if settings.active_version_index < 0 or settings.active_version_index >= len(settings.versions):
            self.report({'ERROR'}, "No version selected")
            return {'CANCELLED'}

        item = settings.versions[settings.active_version_index]
        blend_path = find_snapshot_path(item.version_id)

        if not blend_path:
            # Automatically clean up ghost entry
            version_id = item.version_id
            self.report({'WARNING'}, f"Snapshot file not found. Removed version {version_id} from list.")
            delete_version_by_id(version_id)
            sync_history_to_props(context)
            return {'CANCELLED'}

        # Handle unsaved changes (Interactive only)
        if not bpy.app.background and bpy.data.is_dirty:
            if self.confirm_save:
                if bpy.data.filepath:
                    try:
                        bpy.ops.wm.save_mainfile()
                    except Exception as e:
                        self.report({'ERROR'}, f"Failed to save current file: {e}")
                        return {'CANCELLED'}
                else:
                    self.report({'ERROR'}, "Current file is not saved. Cannot overwrite.")
                    return {'CANCELLED'}

        bpy.ops.wm.open_mainfile(filepath=str(blend_path), check_existing=False)
        return {'FINISHED'}


class SAVEPOINTS_OT_delete(bpy.types.Operator):
    """Delete selected version"""
    bl_idname = "savepoints.delete"
    bl_label = "Delete"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        settings = context.scene.savepoints_settings
        idx = settings.active_version_index
        if idx < 0 or idx >= len(settings.versions):
            return {'CANCELLED'}

        item = settings.versions[idx]

        if item.is_protected:
            self.report({'WARNING'}, f"Cannot delete locked version: {item.version_id}")
            return {'CANCELLED'}

        delete_version_by_id(item.version_id)

        sync_history_to_props(context)
        return {'FINISHED'}


class SAVEPOINTS_OT_refresh(bpy.types.Operator):
    """Refresh list"""
    bl_idname = "savepoints.refresh"
    bl_label = "Refresh"

    def execute(self, context):
        cleanup_retrieve_temp_files()

        settings = context.scene.savepoints_settings
        if settings.use_limit_versions:
            prune_versions(
                max_keep=settings.max_versions_to_keep,
            )

        sync_history_to_props(context)
        return {'FINISHED'}
