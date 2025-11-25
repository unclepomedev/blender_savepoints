# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


class SAVEPOINTS_UL_version_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.label(text=f"{item.version_id} - {item.note} ({item.timestamp})")


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

        layout.operator("savepoints.commit", text="Save Version", icon='FILE_TICK')

        layout.separator()
        layout.label(text="History:")

        row = layout.row()
        row.template_list("SAVEPOINTS_UL_version_list", "", settings, "versions", settings, "active_version_index")

        col = row.column(align=True)
        col.operator("savepoints.refresh", text="", icon='FILE_REFRESH')
        col.operator("savepoints.delete", text="", icon='TRASH')

        if settings.active_version_index >= 0 and len(settings.versions) > settings.active_version_index:
            item = settings.versions[settings.active_version_index]

            box = layout.box()
            box.label(text=f"ID: {item.version_id}")
            box.label(text=f"Date: {item.timestamp}")
            box.label(text=f"Note: {item.note}")

            layout.operator("savepoints.checkout", text="Checkout (Restore)", icon='RECOVER_LAST')
