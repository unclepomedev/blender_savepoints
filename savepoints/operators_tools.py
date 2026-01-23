# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy
from bpy_extras.io_utils import ImportHelper

from .properties import RetrieveObjectItem
from .services.ghost import get_ghost_collection_name, load_ghost, unload_ghost
from .services.linking import link_history, resolve_history_path_from_selection
from .services.retrieve import (
    create_retrieve_temp_file,
    delete_retrieve_temp_file,
    get_importable_objects,
    append_objects
)
from .services.snapshot import find_snapshot_path
from .services.versioning import is_safe_filename
from .ui_utils import sync_history_to_props


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


class SAVEPOINTS_OT_retrieve_objects(bpy.types.Operator):
    """Retrieve Objects: Append objects from this version"""
    bl_idname = "savepoints.retrieve_objects"
    bl_label = "Retrieve Objects"
    bl_options = {'REGISTER', 'UNDO'}

    version_id: bpy.props.StringProperty()

    objects: bpy.props.CollectionProperty(type=RetrieveObjectItem)

    def invoke(self, context, _event):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id

        self.version_id = version_id

        if not is_safe_filename(version_id):
            self.report({'ERROR'}, "Invalid version ID")
            return {'CANCELLED'}

        snapshot_path = find_snapshot_path(version_id)
        if not snapshot_path:
            self.report({'ERROR'}, f"Snapshot file not found for version: {version_id}")
            return {'CANCELLED'}

        try:
            object_names = get_importable_objects(snapshot_path)
            self.objects.clear()
            for name in object_names:
                obj_item = self.objects.add()
                obj_item.name = name
                obj_item.selected = False

        except Exception as e:
            self.report({'ERROR'}, f"Failed to read snapshot: {e}")
            return {'CANCELLED'}

        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, _context):
        layout = self.layout
        layout.label(text="Select Objects to Retrieve:")

        box = layout.box()
        col = box.column()
        for item in self.objects:
            col.prop(item, "selected", text=item.name)

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item and not self.version_id:
            self.version_id = item.version_id

        if not self.version_id:
            # Try to get from active
            if context.scene.savepoints_settings.active_version_index >= 0:
                idx = context.scene.savepoints_settings.active_version_index
                if idx < len(context.scene.savepoints_settings.versions):
                    self.version_id = context.scene.savepoints_settings.versions[idx].version_id

        if not self.version_id:
            self.report({'ERROR'}, "No version specified")
            return {'CANCELLED'}

        snapshot_path = find_snapshot_path(self.version_id)
        if not snapshot_path:
            self.report({'ERROR'}, f"Snapshot not found: {self.version_id}")
            return {'CANCELLED'}

        temp_path = None
        try:
            target_objects = [item.name for item in self.objects if item.selected]

            if not target_objects:
                self.report({'WARNING'}, "No objects selected.")
                return {'CANCELLED'}

            temp_path = create_retrieve_temp_file(snapshot_path)

            appended = append_objects(temp_path, target_objects)
            self.report({'INFO'}, f"Retrieved {len(appended)} objects.")

        except Exception as e:
            self.report({'ERROR'}, f"Retrieve failed: {e}")
            return {'CANCELLED'}
        finally:
            if temp_path:
                delete_retrieve_temp_file(temp_path)

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
        if not version_id:
            self.report({'ERROR'}, "No version specified")
            return {'CANCELLED'}
        collection_name = get_ghost_collection_name(version_id)

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
