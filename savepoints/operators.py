# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy
from bpy_extras.io_utils import ImportHelper

from .properties import RetrieveObjectItem
from .services.asset_path import unmap_snapshot_paths
from .services.backup import create_backup, HistoryDirectoryUnavailableError
from .services.ghost import get_ghost_collection_name, load_ghost, unload_ghost
from .services.linking import link_history, resolve_history_path_from_selection
from .services.manifest import (
    load_manifest,
    initialize_history_for_path

)
from .services.retrieve import (
    cleanup_retrieve_temp_files,
    create_retrieve_temp_file,
    delete_retrieve_temp_file,
    get_importable_objects,
    append_objects
)
from .services.snapshot import create_snapshot, find_snapshot_path
from .services.storage import (
    get_parent_path_from_snapshot,
    get_fork_target_path, SNAPSHOT_EXT,
)
from .services.versioning import (
    get_next_version_id,
    delete_version_by_id,
    set_version_protection,
    update_version_note,
    update_version_tag,
    is_safe_filename,
    prune_versions,
    generate_default_note
)
from .ui_utils import sync_history_to_props, force_redraw_areas


class SAVEPOINTS_OT_link_history(bpy.types.Operator, ImportHelper):
    """Link an existing history folder to this file"""
    bl_idname = "savepoints.link_history"
    bl_label = "Link Existing History Folder"
    bl_options = {'REGISTER', 'UNDO'}

    # Explicitly define directory to ensure it exists and can be passed
    directory: bpy.props.StringProperty(subtype='DIR_PATH', options={'HIDDEN'})
    filter_folder: bpy.props.BoolProperty(default=True, options={'HIDDEN'})

    def execute(self, context):
        selected_path = resolve_history_path_from_selection(self.filepath, self.directory)

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


class SAVEPOINTS_OT_edit_note(bpy.types.Operator):
    """Edit the note of an existing version"""
    bl_idname = "savepoints.edit_note"
    bl_label = "Edit Note"
    bl_options = {'REGISTER'}

    version_id: bpy.props.StringProperty(options={'HIDDEN'})
    new_note: bpy.props.StringProperty(name="Note")

    def invoke(self, context, event):
        item = getattr(context, "savepoints_item", None)
        if not item and self.version_id:
            settings = context.scene.savepoints_settings
            for v in settings.versions:
                if v.version_id == self.version_id:
                    item = v
                    break
        if item:
            self.version_id = item.version_id
            self.new_note = item.note
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "new_note")

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id
        if not version_id:
            return {'CANCELLED'}

        try:
            update_version_note(version_id, self.new_note)
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
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id
        if not version_id:
            return {'CANCELLED'}

        try:
            update_version_tag(version_id, self.tag)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to set tag: {e}")
            return {'CANCELLED'}

        # Update UI property directly instead of full sync
        settings = context.scene.savepoints_settings
        found = False
        for v in settings.versions:
            if v.version_id == version_id:
                v.tag = self.tag
                found = True
                break
        if not found:
            sync_history_to_props(context)

        # Force UI redraw
        for area in context.window.screen.areas:
            area.tag_redraw()

        return {'FINISHED'}


class SAVEPOINTS_OT_retrieve_objects(bpy.types.Operator):
    """Retrieve Objects: Append objects from this version"""
    bl_idname = "savepoints.retrieve_objects"
    bl_label = "Retrieve Objects"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    objects: bpy.props.CollectionProperty(type=RetrieveObjectItem)
    temp_file_path: bpy.props.StringProperty(options={'HIDDEN'})

    def invoke(self, context, event):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id

        if not is_safe_filename(version_id):
            self.report({'ERROR'}, "Invalid version ID")
            return {'CANCELLED'}

        snapshot_path = find_snapshot_path(version_id)
        if not snapshot_path:
            self.report({'ERROR'}, f"Snapshot file not found for version: {version_id}")
            return {'CANCELLED'}

        try:
            temp_path = create_retrieve_temp_file(snapshot_path)
            self.temp_file_path = str(temp_path)

            # Populate object list
            object_names = get_importable_objects(temp_path)
            self.objects.clear()
            for name in object_names:
                obj_item = self.objects.add()
                obj_item.name = name
                obj_item.selected = False

        except Exception as e:
            self.report({'ERROR'}, f"Failed to prepare retrieve file: {e}")
            return {'CANCELLED'}

        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Select Objects to Retrieve:")

        box = layout.box()
        col = box.column()
        for item in self.objects:
            col.prop(item, "selected", text=item.name)

    def execute(self, context):
        if not self.temp_file_path:
            return {'CANCELLED'}

        temp_path = Path(self.temp_file_path)

        try:
            target_objects = [item.name for item in self.objects if item.selected]

            if not target_objects:
                self.report({'WARNING'}, "No objects selected.")
                return {'CANCELLED'}

            appended = append_objects(temp_path, target_objects)
            self.report({'INFO'}, f"Retrieved {len(appended)} objects.")

        except Exception as e:
            self.report({'ERROR'}, f"Retrieve failed: {e}")
            return {'CANCELLED'}
        finally:
            # Always cleanup
            delete_retrieve_temp_file(temp_path)

        return {'FINISHED'}


class SAVEPOINTS_OT_toggle_protection(bpy.types.Operator):
    """Toggle protection for a version"""
    bl_idname = "savepoints.toggle_protection"
    bl_label = "Toggle Protection"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id

        if version_id == "autosave":
            return {'CANCELLED'}

        settings = context.scene.savepoints_settings

        target_item = None
        for v in settings.versions:
            if v.version_id == version_id:
                target_item = v
                break

        if not target_item:
            return {'CANCELLED'}

        new_state = not target_item.is_protected
        set_version_protection(version_id, new_state)
        target_item.is_protected = new_state
        return {'FINISHED'}


class SAVEPOINTS_OT_toggle_ghost(bpy.types.Operator):
    """Toggle Ghost Reference: Overlay this version as wireframe"""
    bl_idname = "savepoints.toggle_ghost"
    bl_label = "Toggle Ghost Reference"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id
        collection_name = get_ghost_collection_name(version_id)

        # Check if exists
        existing_col = bpy.data.collections.get(collection_name)

        if existing_col:
            unload_ghost(version_id, context)
            self.report({'INFO'}, f"Ghost Reference {version_id} removed.")
            return {'FINISHED'}

        else:
            try:
                count = load_ghost(version_id, context)
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

        # Ensure history directory is created for the new file (so link_history is suppressed)
        try:
            initialize_history_for_path(target_path)
        except Exception as e:
            self.report({'WARNING'}, f"History creation failed: {e}")

        try:
            # 1. Save to new location (Blender tries to fix paths, but often fails for Deep -> Shallow move)
            bpy.ops.wm.save_as_mainfile(filepath=str(target_path))

            if unmap_snapshot_paths():
                self.report({'INFO'}, "Fixed relative paths for forked project.")
                bpy.ops.wm.save_mainfile()

        except Exception as e:
            self.report({'ERROR'}, f"Failed to fork file: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Forked to {target_path.name}")

        # Force redraw to remove HUD (no longer in snapshot mode)
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
