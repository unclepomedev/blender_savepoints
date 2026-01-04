# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

from .services.ghost import load_single_object_ghost, cleanup_single_object_ghost
from .services.object_history import compare_object_history


class SavePointsObjectHistoryItem(bpy.types.PropertyGroup):
    version_id: bpy.props.StringProperty()
    change_type: bpy.props.StringProperty()
    details: bpy.props.StringProperty()
    note: bpy.props.StringProperty()
    timestamp: bpy.props.StringProperty()


class SAVEPOINTS_UL_object_history(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row()

            # Version ID (30%)
            split = row.split(factor=0.25)
            split.label(text=item.version_id)

            # Type (25%)
            split2 = split.split(factor=0.33)
            icon_name = 'DOT'
            type_label = item.change_type

            if item.change_type == 'MAJOR':
                icon_name = 'MESH_DATA'
            elif item.change_type == 'MINOR':
                icon_name = 'MOD_EDGESPLIT'
            elif item.change_type == 'MOVED':
                icon_name = 'CON_LOCLIKE'
            elif item.change_type == 'UNCHANGED':
                icon_name = 'CHECKMARK'

            split2.label(text=type_label, icon=icon_name)

            # Details (45%)
            split3 = split2.split(factor=0.5)
            split3.label(text=item.details)

            # Note (Remaining)
            if item.note:
                split3.label(text=item.note, icon='TEXT')


def update_ghost_preview(self, context):
    wm = context.window_manager
    idx = wm.savepoints_object_history_index
    history = wm.savepoints_object_history

    # We rely on active object being the same as when dialog opened.
    obj = context.active_object
    if not obj:
        return

    if 0 <= idx < len(history):
        item = history[idx]
        try:
            load_single_object_ghost(item.version_id, obj.name, context)
        except Exception as e:
            print(f"[SavePoints] Ghost load error: {e}")
    else:
        cleanup_single_object_ghost(obj.name, context)


class SAVEPOINTS_OT_show_object_history(bpy.types.Operator):
    bl_idname = "savepoints.show_object_history"
    bl_label = "Object History"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):
        obj = context.active_object

        # Calculate history
        try:
            history_data = compare_object_history(obj)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to compute history: {e}")
            return {'CANCELLED'}

        wm = context.window_manager
        wm.savepoints_object_history.clear()

        if not history_data:
            self.report({'INFO'}, "No history changes found for this object.")
            # We can still show empty dialog or just return. 
            # Showing dialog confirms it worked but found nothing.

        for h in history_data:
            item = wm.savepoints_object_history.add()
            item.version_id = h['version_id']
            item.change_type = h['change_type']
            item.details = h['details']
            item.note = h['note']
            item.timestamp = h['timestamp']

        wm.savepoints_object_history_index = -1

        return context.window_manager.invoke_popup(self, width=600)

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        obj = context.active_object

        layout.label(text=f"History for: {obj.name}", icon='OBJECT_DATAMODE')

        row = layout.row()
        row.template_list(
            "SAVEPOINTS_UL_object_history", "",
            wm, "savepoints_object_history",
            wm, "savepoints_object_history_index",
            rows=10
        )

    def execute(self, context):
        # Cleanup on close (OK)
        obj = context.active_object
        if obj:
            cleanup_single_object_ghost(obj.name, context)
        return {'FINISHED'}

    def cancel(self, context):
        # Cleanup on close (Cancel/Esc)
        obj = context.active_object
        if obj:
            cleanup_single_object_ghost(obj.name, context)


def draw_object_context_menu(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(SAVEPOINTS_OT_show_object_history.bl_idname, text="Show Object History", icon='TIME')
