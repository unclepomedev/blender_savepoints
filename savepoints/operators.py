# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy
from bpy_extras.io_utils import ImportHelper

from .handler_manager import RescuePostLoadHandler
from .services.backup import create_backup, HistoryDirectoryUnavailableError
from .services.ghost import get_ghost_collection_name, load_ghost, unload_ghost
from .services.linking import link_history, resolve_history_path_from_selection
from .services.rescue import (
    cleanup_rescue_temp_files,
    create_rescue_temp_file,
    delete_rescue_temp_file,
    get_rescue_append_dir
)
from .services.snapshot import create_snapshot, find_snapshot_path
from .services.storage import (
    get_parent_path_from_snapshot,
    load_manifest,
    get_history_dir,
    get_fork_target_path,
    initialize_history_for_path
)
from .services.versioning import (
    get_next_version_id,
    delete_version_by_id,
    set_version_protection,
    update_version_note,
    update_version_tag,
    is_safe_filename,
    prune_versions
)
from .ui_utils import sync_history_to_props, force_redraw_areas, find_3d_view_override


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

    def invoke(self, context, event):
        return self._run(context)

    def execute(self, context):
        return self._run(context)

    def _run(self, context):
        if not is_safe_filename(self.version_id):
            self.report({'ERROR'}, "Invalid version ID")
            return {'CANCELLED'}

        snapshot_path = find_snapshot_path(self.version_id)
        if not snapshot_path:
            self.report({'ERROR'}, f"Snapshot file not found for version: {self.version_id}")
            return {'CANCELLED'}

        try:
            temp_blend_path = create_rescue_temp_file(snapshot_path)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to create temp file: {e}")
            return {'CANCELLED'}

        append_dir = get_rescue_append_dir(temp_blend_path)

        # Capture initial state to detect changes
        initial_obj_count = len(bpy.data.objects)

        # Register handler using the new manager
        handler = RescuePostLoadHandler(temp_blend_path, initial_obj_count)
        handler.register()

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')

        if not self._open_append_dialog(context, append_dir):
            handler.unregister()
            delete_rescue_temp_file(temp_blend_path)
            return {'CANCELLED'}

        return {'FINISHED'}

    def _open_append_dialog(self, context, append_dir):
        found_context = find_3d_view_override(context)

        if found_context:
            try:
                with context.temp_override(**found_context):
                    bpy.ops.wm.append('INVOKE_DEFAULT', filepath=append_dir, directory=append_dir, filename="")
                return True
            except Exception as e:
                print(f"[SavePoints] Append Error: {e}")
                self.report({'ERROR'}, f"Rescue failed due to context error: {e}")
                return False
        else:
            self.report({'ERROR'}, "Could not find a valid 3D Viewport to open the Append dialog.")
            return False


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
        cleanup_rescue_temp_files()
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
            # Save the current snapshot (with remapped paths in memory) to the new location.
            # Blender automatically fixes relative paths when saving to a new location.
            bpy.ops.wm.save_as_mainfile(filepath=str(target_path))
        except Exception as e:
            self.report({'ERROR'}, f"Failed to fork file: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Forked to {target_path.name}")

        # Force redraw to remove HUD (no longer in snapshot mode)
        force_redraw_areas(context)

        return {'FINISHED'}
