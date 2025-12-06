# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil
import time

import bpy

from .core import (
    get_history_dir,
    load_manifest,
    get_next_version_id,
    capture_thumbnail,
    add_version_to_manifest,
    delete_version_by_id,
    get_parent_path_from_snapshot,
)
from .ui_utils import sync_history_to_props


def check_for_relative_paths():
    """
    Scans the current blend file for data blocks with relative paths that refer to external files.
    Returns a list of strings describing the offenders (e.g., "Image: //textures/img.png").
    """
    offenders = []

    def check_collection(datablocks, type_name):
        for db in datablocks:
            if hasattr(db, "filepath") and db.filepath.startswith("//"):
                if db.filepath and len(db.filepath) > 2:
                    if hasattr(db, "packed_file") and db.packed_file:
                        continue
                    offenders.append(f"{type_name} '{db.name}': {db.filepath}")

    check_collection(bpy.data.images, "Image")
    check_collection(bpy.data.libraries, "Library")
    check_collection(bpy.data.texts, "Text")
    check_collection(bpy.data.fonts, "Font")
    check_collection(bpy.data.sounds, "Sound")
    check_collection(bpy.data.movieclips, "MovieClip")
    if hasattr(bpy.data, "cache_files"):
        check_collection(bpy.data.cache_files, "CacheFile")

    return offenders


def create_snapshot(context, version_id, note):
    """
    Helper to create a snapshot.
    Note: In interactive mode, this temporarily converts paths to absolute
    to prevent broken links in the subdirectory, utilizing the Undo stack.
    """
    history_dir = get_history_dir()
    if not history_dir:
        return

    manifest = load_manifest()

    folder_name = version_id
    version_dir = os.path.join(history_dir, folder_name)
    os.makedirs(version_dir, exist_ok=True)

    obj_count = len(bpy.data.objects)

    # Thumbnail
    thumb_filename = "thumbnail.png"
    thumb_path = os.path.join(version_dir, thumb_filename)
    capture_thumbnail(context, thumb_path)

    # Save Snapshot
    blend_filename = "snapshot.blend"
    snapshot_path = os.path.join(version_dir, blend_filename)

    # Workaround for relative paths breaking in subdirectories:
    # Temporarily make paths absolute, save copy, then undo.
    paths_changed = False

    # Find a valid window for context override (needed for ops in timers)
    found_window = None
    if context.window_manager.windows:
        found_window = context.window_manager.windows[0]

    if bpy.app.background:
        offenders = check_for_relative_paths()
        if offenders:
            msg = (
                    "SavePoints Error: Relative paths detected in Background Mode.\n"
                    "Snapshots saved in subdirectories will break these links.\n"
                    "Please pack resources or make paths absolute before running.\n"
                    "Offenders:\n" + "\n".join(offenders[:5])
            )
            if len(offenders) > 5:
                msg += f"\n...and {len(offenders) - 5} more."
            raise RuntimeError(msg)

    try:
        # Check if undo is available to safely revert changes
        # In background mode, undo is often unavailable or unreliable
        if not bpy.app.background and hasattr(bpy.ops.ed, "undo_push") and bpy.ops.ed.undo_push.poll():
            if found_window:
                with context.temp_override(window=found_window):
                    bpy.ops.ed.undo_push(message="SavePoints: Temp Absolute Paths")
                    bpy.ops.file.make_paths_absolute()
            else:
                bpy.ops.ed.undo_push(message="SavePoints: Temp Absolute Paths")
                bpy.ops.file.make_paths_absolute()
            paths_changed = True
    except Exception as e:
        print(f"SavePoints Warning: Could not prepare absolute paths: {e}")

    try:
        if found_window:
            with context.temp_override(window=found_window):
                bpy.ops.wm.save_as_mainfile(copy=True, filepath=snapshot_path)
        else:
            bpy.ops.wm.save_as_mainfile(copy=True, filepath=snapshot_path)
    finally:
        if paths_changed:
            try:
                if found_window:
                    with context.temp_override(window=found_window):
                        bpy.ops.ed.undo()
                else:
                    bpy.ops.ed.undo()
            except Exception as e:
                print(f"SavePoints Warning: Could not revert paths (undo failed): {e}")

    # Capture file size
    file_size = 0
    if os.path.exists(snapshot_path):
        file_size = os.path.getsize(snapshot_path)

    # Update Manifest
    add_version_to_manifest(
        manifest,
        version_id,
        note,
        os.path.join(folder_name, thumb_filename),
        os.path.join(folder_name, blend_filename),
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
            next_save = float(settings.next_autosave_timestamp)
        except ValueError:
            next_save = 0.0

        # Initialize next_save if not set
        if next_save == 0.0:
            # Try to base on last save if valid
            try:
                last_save = float(settings.last_autosave_timestamp)
            except ValueError:
                last_save = 0.0

            if last_save > 0:
                # If we have a last save, next is last + interval
                calculated_next = last_save + interval_sec
                if calculated_next > now:
                    settings.next_autosave_timestamp = str(calculated_next)
                    return check_interval

            # Otherwise schedule from now
            settings.next_autosave_timestamp = str(now + interval_sec)
            return check_interval

        if now < next_save:
            return check_interval

        # Check if we can save
        if not bpy.data.filepath:
            # If file not saved, we can't autosave.
            # Don't update next_timestamp, retry next tick (5s).
            return check_interval

        if get_parent_path_from_snapshot(bpy.data.filepath):
            return check_interval

        # Execute save
        try:
            delete_version_by_id("autosave")
            create_snapshot(context, "autosave", "Auto Save")

            # Success: Reset failure count and update timestamps
            settings.last_autosave_timestamp = str(now)
            settings.autosave_fail_count = 0
            settings.next_autosave_timestamp = str(now + interval_sec)

        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Auto Save failed: {e}")
            settings.autosave_fail_count += 1

            # Retry logic with backoff for transient errors
            # Backoff: 10s * 2^(n-1)
            count = settings.autosave_fail_count
            backoff = 10.0 * (2 ** (count - 1))
            # Cap backoff at interval_sec
            backoff = min(backoff, interval_sec)

            settings.next_autosave_timestamp = str(now + backoff)

        return check_interval

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Auto Save critical error: {e}")
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

    def execute(self, context):
        if not bpy.data.filepath:
            self.report({'ERROR'}, "Save the project first!")
            return {'CANCELLED'}

        manifest = load_manifest()
        new_id_str = get_next_version_id(manifest.get("versions", []))
        create_snapshot(context, new_id_str, self.note)

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
        history_dir = get_history_dir()
        if not history_dir:
            self.report({'ERROR'}, "History directory not found")
            return {'CANCELLED'}

        blend_path = os.path.join(history_dir, item.blend_rel_path)

        if not os.path.exists(blend_path):
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

        bpy.ops.wm.open_mainfile(filepath=blend_path, check_existing=False)
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


class SAVEPOINTS_OT_restore(bpy.types.Operator):
    """Restore this snapshot to the parent file, overwriting it."""
    bl_idname = "savepoints.restore"
    bl_label = "Save as Parent"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        from .core import get_parent_path_from_snapshot

        original_path = get_parent_path_from_snapshot(bpy.data.filepath)

        if not original_path:
            self.report({'ERROR'}, "Could not determine parent file path. Are you in a snapshot?")
            return {'CANCELLED'}

        # Verify if we can write to original path
        # Backup first
        if os.path.exists(original_path):
            timestamp = int(time.time())

            from .core import get_history_dir_for_path
            history_dir = get_history_dir_for_path(original_path)
            os.makedirs(history_dir, exist_ok=True)

            filename = os.path.basename(original_path)
            backup_filename = f"{filename}.{timestamp}.bak"
            backup_path = os.path.join(history_dir, backup_filename)

            try:
                shutil.copy2(original_path, backup_path)
                self.report({'INFO'}, f"Backup created: {backup_filename}")
            except Exception as e:
                self.report({'ERROR'}, f"Backup failed: {e}")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "Original file not found. Creating new one.")

        try:
            bpy.ops.wm.save_as_mainfile(filepath=original_path)
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
        parent_path = get_parent_path_from_snapshot(bpy.data.filepath)

        if not parent_path:
            self.report({'ERROR'}, "Could not determine parent file path. Are you in a snapshot?")
            return {'CANCELLED'}

        if not os.path.exists(parent_path):
            self.report({'ERROR'}, f"Parent file not found: {parent_path}")
            return {'CANCELLED'}

        # Open the parent file
        # Note: In UI, this might prompt to save changes if modified.
        bpy.ops.wm.open_mainfile(filepath=parent_path)
        return {'FINISHED'}
