# SPDX-License-Identifier: GPL-3.0-or-later

import os

import bpy

from . import core, ui_utils


class SAVEPOINTS_UL_version_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        pcoll = ui_utils.preview_collections.get("main")
        icon_val = 0
        if pcoll and item.version_id in pcoll:
            icon_val = pcoll[item.version_id].icon_id

        if icon_val:
            layout.label(text=f"{item.version_id} - {item.note} ({item.timestamp})", icon_value=icon_val)
        else:
            layout.label(text=f"{item.version_id} - {item.note} ({item.timestamp})", icon='FILE_BACKUP')

        if item.version_id != "autosave":
            edit_op = layout.operator("savepoints.edit_note", text="", icon='GREASEPENCIL', emboss=False)
            edit_op.version_id = item.version_id
            edit_op.new_note = item.note

            rescue_op = layout.operator("savepoints.rescue_assets", text="", icon='IMPORT', emboss=False)
            rescue_op.version_id = item.version_id

            ghost_col_name = f"Ghost_Reference_{item.version_id}"
            is_ghost_active = bool(bpy.data.collections.get(ghost_col_name))
            ghost_icon = 'ONIONSKIN_ON' if is_ghost_active else 'ONIONSKIN_OFF'

            ghost_op = layout.operator("savepoints.toggle_ghost", text="", icon=ghost_icon, emboss=False,
                                       depress=is_ghost_active)
            ghost_op.version_id = item.version_id

            lock_icon = 'LOCKED' if item.is_protected else 'UNLOCKED'
            op = layout.operator("savepoints.toggle_protection", text="", icon=lock_icon, emboss=False)
            op.version_id = item.version_id

    def filter_items(self, context, data, propname):
        items = getattr(data, propname)
        flt_flags = []
        flt_neworder = []

        if self.filter_name:
            filter_text = self.filter_name.lower()
            for item in items:
                if (filter_text in item.version_id.lower() or
                        filter_text in item.note.lower()):
                    flt_flags.append(self.bitflag_filter_item)
                else:
                    flt_flags.append(0)
        else:
            flt_flags = [self.bitflag_filter_item] * len(items)

        return flt_flags, flt_neworder


def _draw_snapshot_mode(layout, parent_filepath):
    box = layout.box()
    box.label(text="Snapshot Mode", icon='INFO')
    # Show only filename to keep it short
    filename = os.path.basename(parent_filepath)
    box.label(text=f"Parent: {filename}")

    col = box.column(align=True)
    col.operator("savepoints.restore", text="Save as Parent", icon='FILE_TICK')
    col.operator("savepoints.fork_version", text="Fork (Save as New)", icon='DUPLICATE')
    col.operator("savepoints.open_parent", text="Return to Parent", icon='LOOP_BACK')

    layout.separator()
    layout.label(text="To view history, restore to parent.")


def _draw_history_list(layout, settings):
    layout.operator("savepoints.commit", text="Save Version", icon='FILE_TICK')

    layout.separator()
    layout.label(text="History:")

    row = layout.row()
    row.template_list("SAVEPOINTS_UL_version_list", "", settings, "versions", settings, "active_version_index")

    col = row.column(align=True)
    col.operator("savepoints.refresh", text="", icon='FILE_REFRESH')
    col.operator("savepoints.delete", text="", icon='TRASH')


def _draw_version_details(layout, settings):
    if settings.active_version_index >= 0 and len(settings.versions) > settings.active_version_index:
        item = settings.versions[settings.active_version_index]

        box = layout.box()

        pcoll = ui_utils.preview_collections.get("main")
        has_preview = False
        if pcoll and item.version_id in pcoll:
            has_preview = True

        if has_preview:
            row = box.row()
            row.alignment = 'CENTER'
            row.template_icon(icon_value=pcoll[item.version_id].icon_id, scale=8)
        else:
            row = box.row()
            row.alignment = 'CENTER'
            row.label(text="No Preview", icon='IMAGE_DATA')

        box.label(text=f"ID: {item.version_id}")
        box.label(text=f"Date: {item.timestamp}")
        box.label(text=f"Note: {item.note}")
        box.label(text=f"Objects: {item.object_count} | Size: {item.file_size_display}")

        layout.operator("savepoints.checkout", text="Checkout (Restore)", icon='RECOVER_LAST')


def _draw_empty_state(layout):
    box = layout.box()
    box.label(text="No history found for this file.")
    box.operator("savepoints.link_history", text="Link Existing History Folder", icon='FILE_FOLDER')

    layout.separator()
    layout.label(text="Or start a new history:")
    layout.operator("savepoints.commit", text="Create First Version", icon='FILE_TICK')


def _draw_general_settings(layout, settings):
    box = layout.box()
    box.label(text="General", icon='PREFERENCES')
    box.prop(settings, "show_save_dialog")


def _draw_auto_save_settings(layout, settings):
    box = layout.box()
    box.label(text="Auto Save", icon='TIME')
    box.prop(settings, "use_auto_save")
    if settings.use_auto_save:
        box.prop(settings, "auto_save_interval")


def _draw_disk_management_settings(layout, settings):
    box = layout.box()
    box.label(text="Disk Management", icon='DISK_DRIVE')
    box.prop(settings, "use_limit_versions")
    if settings.use_limit_versions:
        box.prop(settings, "max_versions_to_keep")
        box.prop(settings, "keep_daily_backups")


class SAVEPOINTS_PT_main(bpy.types.Panel):
    bl_label = "SavePoints"
    bl_idname = "SAVEPOINTS_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SavePoints'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        settings = scene.savepoints_settings

        if not bpy.data.filepath:
            layout.label(text="Please save the file first.", icon='INFO')
            return

        # Dynamic check for Snapshot Mode
        parent_filepath = core.get_parent_path_from_snapshot(bpy.data.filepath)

        if parent_filepath:
            _draw_snapshot_mode(layout, parent_filepath)
            return

        history_dir = core.get_history_dir()
        has_history = history_dir and os.path.exists(history_dir)

        if has_history:
            _draw_history_list(layout, settings)
            _draw_version_details(layout, settings)
        else:
            _draw_empty_state(layout)

        layout.separator()
        _draw_general_settings(layout, settings)

        layout.separator()
        _draw_auto_save_settings(layout, settings)

        layout.separator()
        _draw_disk_management_settings(layout, settings)
