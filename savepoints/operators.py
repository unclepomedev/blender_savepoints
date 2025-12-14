# SPDX-License-Identifier: GPL-3.0-or-later

import shutil
import time
from pathlib import Path

import bpy

from .core import (
    get_history_dir,
    load_manifest,
    get_next_version_id,
    capture_thumbnail,
    add_version_to_manifest,
    delete_version_by_id,
    get_parent_path_from_snapshot,
    prune_versions,
    set_version_protection,
)
from .ui_utils import sync_history_to_props


def create_snapshot(context, version_id, note, skip_thumbnail=False):
    """Helper to create a snapshot."""
    history_dir_str = get_history_dir()
    if not history_dir_str:
        return

    history_dir = Path(history_dir_str)
    manifest = load_manifest()

    folder_name = version_id
    version_dir = history_dir / folder_name
    version_dir.mkdir(parents=True, exist_ok=True)

    obj_count = len(bpy.data.objects)

    # Thumbnail
    thumb_filename = "thumbnail.png"
    thumb_path = version_dir / thumb_filename
    if not skip_thumbnail:
        capture_thumbnail(context, str(thumb_path))

    # Save Snapshot
    blend_filename = "snapshot.blend_snapshot"
    snapshot_path = version_dir / blend_filename

    bpy.ops.wm.save_as_mainfile(copy=True, filepath=str(snapshot_path))

    # Capture file size
    file_size = 0
    if snapshot_path.exists():
        file_size = snapshot_path.stat().st_size

    # Update Manifest
    add_version_to_manifest(
        manifest,
        version_id,
        note,
        str(Path(folder_name) / thumb_filename),
        str(Path(folder_name) / blend_filename),
        object_count=obj_count,
        file_size=file_size
    )

    # Update UI
    sync_history_to_props(context)


def autosave_timer():
    """Timer function for auto-save."""
    # Check every 5 seconds for responsiveness
    check_interval = 5.0

    try:
        context = bpy.context
        scene = getattr(context, "scene", None)
        if not scene:
            return check_interval

        settings = getattr(scene, "savepoints_settings", None)
        if not settings:
            return check_interval

        if not settings.use_auto_save:
            return check_interval

        interval_min = settings.auto_save_interval
        if interval_min < 1:
            interval_min = 1

        interval_sec = interval_min * 60.0

        now = time.time()
        try:
            last_save = float(settings.last_autosave_timestamp)
        except ValueError:
            last_save = 0.0

        # If last_save is 0 (initial), set it to now so we don't save immediately
        if last_save == 0.0:
            settings.last_autosave_timestamp = str(now)
            return check_interval

        if (now - last_save) < interval_sec:
            return check_interval

        # Check if we can save
        if not bpy.data.filepath:
            return check_interval

        if get_parent_path_from_snapshot(bpy.data.filepath):
            return check_interval

        # Execute save
        delete_version_by_id("autosave")
        create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)
        settings.last_autosave_timestamp = str(time.time())

        return check_interval

    except Exception as e:
        print(f"Auto Save failed: {e}")
        return check_interval


class SAVEPOINTS_OT_commit(bpy.types.Operator):
    """Save a new version of the current project"""
    bl_idname = "savepoints.commit"
    bl_label = "Save Version"
    bl_options = {'REGISTER', 'UNDO'}

    note: bpy.props.StringProperty(name="Commit Message", default="")

    @classmethod
    def poll(cls, context):
        return not bool(get_parent_path_from_snapshot(bpy.data.filepath))

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "note")

        settings = context.scene.savepoints_settings
        if settings.use_limit_versions:
            protected_count = sum(1 for v in settings.versions if v.version_id != "autosave" and v.is_protected)
            if protected_count >= settings.max_versions_to_keep:
                layout.label(text="Warning: Locked versions limit reached.", icon='ERROR')
                layout.label(text="Auto-deletion will be skipped.", icon='INFO')

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Save the project first!")
            return {'CANCELLED'}

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


class SAVEPOINTS_OT_toggle_protection(bpy.types.Operator):
    """Toggle protection for a version"""
    bl_idname = "savepoints.toggle_protection"
    bl_label = "Toggle Protection"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        settings = context.scene.savepoints_settings

        target_item = None
        for item in settings.versions:
            if item.version_id == self.version_id:
                target_item = item
                break

        if not target_item:
            return {'CANCELLED'}

        new_state = not target_item.is_protected
        set_version_protection(self.version_id, new_state)
        target_item.is_protected = new_state
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
        history_dir_str = get_history_dir()
        if not history_dir_str:
            self.report({'ERROR'}, "History directory not found")
            return {'CANCELLED'}

        history_dir = Path(history_dir_str)
        blend_path = history_dir / item.blend_rel_path

        if not blend_path.exists():
            self.report({'ERROR'}, f"File not found: {blend_path}")
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
        sync_history_to_props(context)
        return {'FINISHED'}


class SAVEPOINTS_OT_restore(bpy.types.Operator):
    """Restore this snapshot to the parent file, overwriting it."""
    bl_idname = "savepoints.restore"
    bl_label = "Save as Parent"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        from .core import get_parent_path_from_snapshot

        original_path_str = get_parent_path_from_snapshot(bpy.data.filepath)

        if not original_path_str:
            self.report({'ERROR'}, "Could not determine parent file path. Are you in a snapshot?")
            return {'CANCELLED'}

        original_path = Path(original_path_str)

        # Verify if we can write to original path
        # Backup first
        if original_path.exists():
            timestamp = int(time.time())

            from .core import get_history_dir_for_path
            history_dir_str = get_history_dir_for_path(str(original_path))
            if history_dir_str:
                history_dir = Path(history_dir_str)
                history_dir.mkdir(parents=True, exist_ok=True)

                filename = original_path.name
                backup_filename = f"{filename}.{timestamp}.bak"
                backup_path = history_dir / backup_filename

                try:
                    shutil.copy2(original_path, backup_path)
                    self.report({'INFO'}, f"Backup created: {backup_filename}")
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
