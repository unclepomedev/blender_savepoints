# SPDX-License-Identifier: GPL-3.0-or-later

import os

import bpy

from .utils import (
    get_history_dir,
    load_manifest,
    sync_history_to_props,
    get_next_version_id,
    capture_thumbnail,
    add_version_to_manifest,
    delete_version_by_id,
)


class SAVEPOINTS_OT_commit(bpy.types.Operator):
    """Save a new version of the current project"""
    bl_idname = "savepoints.commit"
    bl_label = "Save Version"
    bl_options = {'REGISTER', 'UNDO'}

    note: bpy.props.StringProperty(name="Commit Message", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Save the project first!")
            return {'CANCELLED'}

        # 1. Setup paths
        history_dir = get_history_dir()
        manifest = load_manifest()

        # Determine new ID
        new_id_str = get_next_version_id(manifest.get("versions", []))
        folder_name = new_id_str
        version_dir = os.path.join(history_dir, folder_name)
        os.makedirs(version_dir, exist_ok=True)

        # Capture stats
        obj_count = len(bpy.data.objects)

        # 2. Thumbnail
        thumb_filename = "thumbnail.png"
        thumb_path = os.path.join(version_dir, thumb_filename)
        capture_thumbnail(context, thumb_path)

        # 3. Save Snapshot
        blend_filename = "snapshot.blend"
        snapshot_path = os.path.join(version_dir, blend_filename)
        bpy.ops.wm.save_as_mainfile(copy=True, filepath=snapshot_path)

        # Capture file size
        file_size = 0
        if os.path.exists(snapshot_path):
            file_size = os.path.getsize(snapshot_path)

        # 4. Update Manifest
        add_version_to_manifest(
            manifest,
            new_id_str,
            self.note,
            os.path.join(folder_name, thumb_filename),
            os.path.join(folder_name, blend_filename),
            object_count=obj_count,
            file_size=file_size
        )

        # 5. Update UI
        sync_history_to_props(context)

        self.report({'INFO'}, f"Version {new_id_str} saved.")
        return {'FINISHED'}


class SAVEPOINTS_OT_checkout(bpy.types.Operator):
    """Restore selected version"""
    bl_idname = "savepoints.checkout"
    bl_label = "Checkout"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        settings = context.scene.savepoints_settings
        if settings.active_version_index < 0 or settings.active_version_index >= len(settings.versions):
            self.report({'ERROR'}, "No version selected")
            return {'CANCELLED'}

        item = settings.versions[settings.active_version_index]
        history_dir = get_history_dir()
        if not history_dir:
            self.report({'ERROR'}, "History directory not found")
            return {'CANCELLED'}

        blend_path = os.path.join(history_dir, item.blend_rel_path)

        if not os.path.exists(blend_path):
            self.report({'ERROR'}, f"File not found: {blend_path}")
            return {'CANCELLED'}

        bpy.ops.wm.open_mainfile(filepath=blend_path)
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
        delete_version_by_id(item.version_id)

        sync_history_to_props(context)
        return {'FINISHED'}


class SAVEPOINTS_OT_refresh(bpy.types.Operator):
    """Refresh list"""
    bl_idname = "savepoints.refresh"
    bl_label = "Refresh"

    def execute(self, context):
        sync_history_to_props(context)
        return {'FINISHED'}
