# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil
import time
from pathlib import Path

import bpy
from bpy_extras.io_utils import ImportHelper

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
    update_version_note,
    update_version_tag,
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


class SAVEPOINTS_OT_link_history(bpy.types.Operator, ImportHelper):
    """Link an existing history folder to this file"""
    bl_idname = "savepoints.link_history"
    bl_label = "Link Existing History Folder"
    bl_options = {'REGISTER', 'UNDO'}

    # Explicitly define directory to ensure it exists and can be passed
    directory: bpy.props.StringProperty(subtype='DIR_PATH', options={'HIDDEN'})
    filter_folder: bpy.props.BoolProperty(default=True, options={'HIDDEN'})

    def execute(self, context):
        from .core import link_history, MANIFEST_NAME

        selected_path = Path(self.filepath)

        # Robustness: If user selected the manifest.json file directly, handle it
        if selected_path.name == MANIFEST_NAME:
            selected_path = selected_path.parent

        # If selected_path is not a dir (e.g. user selected some other file or just opened dir),
        if not selected_path.is_dir():
            if self.directory:
                dir_path = Path(self.directory)
                if (dir_path / MANIFEST_NAME).exists():
                    selected_path = dir_path

        try:
            target_path_str = link_history(selected_path, bpy.data.filepath)
            self.report({'INFO'}, f"History linked successfully: {Path(target_path_str).name}")
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

        # Refresh UI
        sync_history_to_props(context)

        return {'FINISHED'}


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

    def _get_default_note(self, context):
        try:
            obj = context.active_object
            if not obj:
                return ""

            mode = obj.mode

            if mode == 'EDIT':
                friendly_mode = f"Edit {obj.type.title()}"
            else:
                mode_map = {
                    'OBJECT': 'Object',
                    'POSE': 'Pose',
                    'SCULPT': 'Sculpt',
                    'VERTEX_PAINT': 'Vertex Paint',
                    'WEIGHT_PAINT': 'Weight Paint',
                    'TEXTURE_PAINT': 'Texture Paint',
                    'PARTICLE_EDIT': 'Particle Edit',
                }
                friendly_mode = mode_map.get(mode, mode.replace('_', ' ').title())

            return f"{friendly_mode}: {obj.name}"
        except Exception:
            return ""

    def invoke(self, context, event):
        settings = context.scene.savepoints_settings

        default_note = self._get_default_note(context)

        if not self.note:
            self.note = default_note

        if settings.show_save_dialog and not self.force_quick:
            return context.window_manager.invoke_props_dialog(self)

        return self.execute(context)

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

        # Ensure default note is set if empty (especially for non-interactive execution)
        if not self.note:
            self.note = self._get_default_note(context)

        manifest = load_manifest()
        new_id_str = get_next_version_id(manifest.get("versions", []))
        create_snapshot(context, new_id_str, self.note)

        # Auto Pruning
        settings = context.scene.savepoints_settings
        if settings.use_limit_versions and settings.max_versions_to_keep > 0:
            deleted = prune_versions(settings.max_versions_to_keep, settings.keep_daily_backups)
            if deleted > 0:
                sync_history_to_props(context)

        self.report({'INFO'}, f"Version {new_id_str} saved.")
        return {'FINISHED'}


class SAVEPOINTS_OT_edit_note(bpy.types.Operator):
    """Edit the note of an existing version"""
    bl_idname = "savepoints.edit_note"
    bl_label = "Edit Note"
    bl_options = {'REGISTER'}

    version_id: bpy.props.StringProperty(options={'HIDDEN'})
    new_note: bpy.props.StringProperty(name="Note")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "new_note")

    def execute(self, context):
        if not self.version_id:
            return {'CANCELLED'}

        try:
            update_version_note(self.version_id, self.new_note)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to update note: {e}")
            return {'CANCELLED'}

        sync_history_to_props(context)

        # Force UI redraw to update the note in the list immediately
        for area in context.window.screen.areas:
            area.tag_redraw()

        return {'FINISHED'}


class SAVEPOINTS_OT_set_tag(bpy.types.Operator):
    """Set tag for a version"""
    bl_idname = "savepoints.set_tag"
    bl_label = "Set Tag"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty(options={'HIDDEN'})
    tag: bpy.props.EnumProperty(
        items=[
            ('NONE', "None", "", 'NONE', 0),
            ('STABLE', "Stable", "", 'CHECKMARK', 1),
            ('MILESTONE', "Milestone", "", 'BOOKMARKS', 2),
            ('EXPERIMENT', "Experiment", "", 'LAB', 3),
            ('BUG', "Bug", "", 'ERROR', 4),
        ]
    )

    def execute(self, context):
        if not self.version_id:
            return {'CANCELLED'}

        try:
            update_version_tag(self.version_id, self.tag)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to set tag: {e}")
            return {'CANCELLED'}

        # Update UI property directly instead of full sync
        settings = context.scene.savepoints_settings
        found = False
        for item in settings.versions:
            if item.version_id == self.version_id:
                item.tag = self.tag
                found = True
                break
        if not found:
            sync_history_to_props(context)

        # Force UI redraw
        for area in context.window.screen.areas:
            area.tag_redraw()

        return {'FINISHED'}


class SAVEPOINTS_OT_rescue_assets(bpy.types.Operator):
    """Rescue Assets: Append objects from this version"""
    bl_idname = "savepoints.rescue_assets"
    bl_label = "Rescue Assets"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        history_dir_str = get_history_dir()
        if not history_dir_str:
            self.report({'ERROR'}, "History directory not found")
            return {'CANCELLED'}

        history_dir = Path(history_dir_str)
        snapshot_path = history_dir / self.version_id / "snapshot.blend_snapshot"

        if not snapshot_path.exists():
            self.report({'ERROR'}, f"Snapshot file not found: {snapshot_path}")
            return {'CANCELLED'}

        temp_blend_path = history_dir / self.version_id / "snapshot_rescue_temp.blend"

        try:
            shutil.copy2(str(snapshot_path), str(temp_blend_path))
            print(f"[SavePoints] Created temp file for rescue: {temp_blend_path}")

        except Exception as e:
            self.report({'ERROR'}, f"Failed to create temp file: {e}")
            return {'CANCELLED'}

        virtual_dir = temp_blend_path / "Object"
        append_dir = str(virtual_dir) + os.sep
        bpy.ops.wm.append('INVOKE_DEFAULT', filepath=append_dir, directory=append_dir, filename="")
        return {'FINISHED'}


class SAVEPOINTS_OT_toggle_protection(bpy.types.Operator):
    """Toggle protection for a version"""
    bl_idname = "savepoints.toggle_protection"
    bl_label = "Toggle Protection"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        if self.version_id == "autosave":
            return {'CANCELLED'}

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


class SAVEPOINTS_OT_toggle_ghost(bpy.types.Operator):
    """Toggle Ghost Reference: Overlay this version as wireframe"""
    bl_idname = "savepoints.toggle_ghost"
    bl_label = "Toggle Ghost Reference"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        version_id = self.version_id
        collection_name = f"Ghost_Reference_{version_id}"

        # Check if exists
        existing_col = bpy.data.collections.get(collection_name)

        if existing_col:
            # --- Toggle OFF (Cleanup) ---

            # 1. Identify objects to remove
            objects_to_remove = [obj for obj in existing_col.objects]

            # 2. Unlink collection from scene
            if context.scene.collection.children.get(collection_name):
                context.scene.collection.children.unlink(existing_col)

            # 3. Remove collection data
            bpy.data.collections.remove(existing_col)

            # 4. Remove objects
            for obj in objects_to_remove:
                try:
                    bpy.data.objects.remove(obj, do_unlink=True)
                except Exception:
                    pass

            # 5. Cleanup unused libraries
            history_dir_str = get_history_dir()
            if history_dir_str:
                # Look for libraries that seem to be from this snapshot
                libs_to_process = []
                for lib in bpy.data.libraries:
                    path_norm = lib.filepath.replace("\\", "/")
                    if (f"/{version_id}/snapshot.blend_snapshot" in path_norm or
                            f"/{version_id}/snapshot.blend" in path_norm):
                        libs_to_process.append(lib)

                # Collections to check for linked data
                data_collections = [
                    bpy.data.objects, bpy.data.meshes, bpy.data.materials,
                    bpy.data.textures, bpy.data.images, bpy.data.armatures,
                    bpy.data.actions, bpy.data.curves, bpy.data.lights,
                    bpy.data.cameras, bpy.data.node_groups, bpy.data.fonts,
                    bpy.data.cache_files, bpy.data.movieclips
                ]

                for lib in libs_to_process:
                    # Force remove all data blocks linked from this library
                    for col in data_collections:
                        items = [item for item in col if getattr(item, "library", None) == lib]
                        for item in items:
                            try:
                                col.remove(item, do_unlink=True)
                            except Exception:
                                pass

                    # Now remove the library itself
                    try:
                        bpy.data.libraries.remove(lib)
                    except Exception:
                        pass

            self.report({'INFO'}, f"Ghost Reference {version_id} removed.")
            return {'FINISHED'}

        else:
            # --- Toggle ON (Load) ---
            history_dir_str = get_history_dir()
            if not history_dir_str:
                self.report({'ERROR'}, "History directory not found")
                return {'CANCELLED'}

            version_dir = Path(history_dir_str) / version_id
            snapshot_path = version_dir / "snapshot.blend_snapshot"

            if not snapshot_path.exists():
                # Check for legacy snapshot file (.blend)
                legacy_snapshot_path = version_dir / "snapshot.blend"
                if legacy_snapshot_path.exists():
                    snapshot_path = legacy_snapshot_path
                else:
                    self.report({'ERROR'}, f"Snapshot file not found: {snapshot_path}")
                    return {'CANCELLED'}

            try:
                # Load Objects
                with bpy.data.libraries.load(str(snapshot_path), link=True) as (data_from, data_to):
                    # Link all objects
                    data_to.objects = data_from.objects

                # Create Collection
                new_col = bpy.data.collections.new(collection_name)
                context.scene.collection.children.link(new_col)

                # Link objects and setup viz
                count = 0
                for obj in data_to.objects:
                    if obj:
                        new_col.objects.link(obj)
                        obj.display_type = 'WIRE'
                        obj.hide_select = True
                        obj.show_in_front = False
                        count += 1

                self.report({'INFO'}, f"Ghost Reference {version_id} loaded ({count} objects).")
                return {'FINISHED'}

            except Exception as e:
                self.report({'ERROR'}, f"Failed to load ghost: {e}")
                return {'CANCELLED'}


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


class SAVEPOINTS_OT_fork_version(bpy.types.Operator):
    """Save the current snapshot as a new project file"""
    bl_idname = "savepoints.fork_version"
    bl_label = "Fork (Save as New)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if not bpy.data.filepath:
            return {'CANCELLED'}

        source_path = Path(bpy.data.filepath)

        # Determine the project root (parent of the history folder)
        try:
            # source_path is .../history_dir/version_id/snapshot.blend
            # parent is .../history_dir/version_id
            # grandparent is .../history_dir
            # great-grandparent is project root
            version_dir = source_path.parent
            version_id = version_dir.name

            history_dir = version_dir.parent
            history_dirname = history_dir.name

            project_root = history_dir.parent

            if not project_root.exists():
                raise FileNotFoundError(f"Project root not found: {project_root}")

            # Calculate filename
            stem = "project"
            if history_dirname.startswith(".") and history_dirname.endswith("_history"):
                # Extract original stem
                stem = history_dirname[1:-8]  # remove '.' and '_history'

            filename = f"{stem}_{version_id}.blend"

        except Exception as e:
            self.report({'ERROR'}, f"Could not determine paths: {e}")
            return {'CANCELLED'}

        target_path = project_root / filename

        if source_path == target_path:
            self.report({'ERROR'}, "Source and target paths are identical.")
            return {'CANCELLED'}

        try:
            shutil.copy2(source_path, target_path)
        except PermissionError:
            self.report({'ERROR'}, "Permission denied when saving file.")
            return {'CANCELLED'}
        except OSError as e:
            self.report({'ERROR'}, f"Failed to save file: {e}")
            return {'CANCELLED'}

        # Open the new file
        bpy.ops.wm.open_mainfile(filepath=str(target_path))

        self.report({'INFO'}, f"Forked to {target_path.name}")
        return {'FINISHED'}
