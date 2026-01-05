# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

from .services.ghost import load_single_object_ghost, cleanup_single_object_ghost
from .services.object_history import compare_object_history

CHANGE_TYPE_ICONS = {
    'MAJOR': 'MESH_DATA',
    'MINOR': 'MOD_EDGESPLIT',
    'MOVED': 'CON_LOCLIKE',
    'UNCHANGED': 'CHECKMARK',
}


class SavePointsObjectHistoryItem(bpy.types.PropertyGroup):
    """Data storage for a single history entry in the UI list."""
    version_id: bpy.props.StringProperty()
    change_type: bpy.props.StringProperty()
    details: bpy.props.StringProperty()
    note: bpy.props.StringProperty()
    timestamp: bpy.props.StringProperty()


class SAVEPOINTS_UL_object_history(bpy.types.UIList):
    """UI List to display object history versions."""

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        # Ensure we are in a valid layout mode
        if self.layout_type not in {'DEFAULT', 'COMPACT'}:
            return

        row = layout.row()

        # --- Column 1: Version ID (10%) ---
        split = row.split(factor=0.10)
        split.label(text=item.version_id)

        # --- Column 2: Change Type (25%) ---
        # Split the remaining 90% by 0.25 -> 22.5% of total
        split_2 = split.split(factor=0.25)

        icon_name = CHANGE_TYPE_ICONS.get(item.change_type, 'DOT')
        split_2.label(text=item.change_type, icon=icon_name)

        # --- Column 3: Details (Remaining space split) ---
        # Allocate approx 50% of the remaining space to details
        split_3 = split_2.split(factor=0.5)
        split_3.label(text=item.details)

        # --- Column 4: Note (Remaining) ---
        if item.note:
            split_3.label(text=item.note, icon='TEXT')


def update_ghost_preview(self, context):
    """
    Callback triggered when the history list index changes.
    Loads the ghost overlay for the selected version.
    """
    wm = context.window_manager
    idx = wm.savepoints_object_history_index
    history = wm.savepoints_object_history

    # Active object is required for context
    obj = context.active_object
    if not obj:
        return

    # Valid selection: Load ghost
    if 0 <= idx < len(history):
        item = history[idx]
        try:
            load_single_object_ghost(item.version_id, obj.name, context)
        except Exception as e:
            print(f"[SavePoints] Ghost load error for {item.version_id}: {e}")

    # No selection or invalid index: Cleanup ghost
    else:
        cleanup_single_object_ghost(obj.name, context)


class SAVEPOINTS_OT_show_object_history(bpy.types.Operator):
    """Show history and ghost previews for the active object"""
    bl_idname = "savepoints.show_object_history"
    bl_label = "Object History"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):
        obj = context.active_object
        wm = context.window_manager

        # Compute history
        try:
            history_data = compare_object_history(obj)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to compute history: {e}")
            return {'CANCELLED'}

        # Populate UI List
        wm.savepoints_object_history.clear()

        if not history_data:
            self.report({'INFO'}, "No history changes found for this object.")
            # Still showing the dialog to confirm we checked.

        for h in history_data:
            item = wm.savepoints_object_history.add()
            item.version_id = h['version_id']
            item.change_type = h['change_type']
            item.details = h['details']
            item.note = h['note']
            item.timestamp = h['timestamp']

        # Reset selection (triggers update_ghost_preview via property update if bound correctly)
        wm.savepoints_object_history_index = -1

        # Explicit cleanup to ensure clean slate
        cleanup_single_object_ghost(obj.name, context)

        return context.window_manager.invoke_popup(self, width=600)

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        obj = context.active_object

        layout.label(text=f"History for: {obj.name}", icon='OBJECT_DATAMODE')

        layout.template_list(
            "SAVEPOINTS_UL_object_history", "",
            wm, "savepoints_object_history",
            wm, "savepoints_object_history_index",
            rows=10
        )

        layout.separator()
        layout.label(text="Click an entry to preview ghost overlay", icon='INFO')

    def execute(self, context):
        self._cleanup(context)
        return {'FINISHED'}

    def cancel(self, context):
        self._cleanup(context)

    def _cleanup(self, context):
        obj = context.active_object
        if obj:
            cleanup_single_object_ghost(obj.name, context)


def draw_object_context_menu(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_DEFAULT'
    layout.operator(SAVEPOINTS_OT_show_object_history.bl_idname, text="Show Object History", icon='TIME')
