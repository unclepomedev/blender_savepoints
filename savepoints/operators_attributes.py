# SPDX-License-Identifier: GPL-3.0-or-later
# pyright: reportOptionalMemberAccess=false

import bpy
from .i18n import TranslatedOperatorMixin, iface, report as rpt
from .translations import TRANSLATION_CONTEXT
from .services.versioning import (
    update_version_note,
    update_version_tag,
    set_version_protection,
)
from .ui_utils import sync_history_to_props


class SAVEPOINTS_OT_edit_note(TranslatedOperatorMixin, bpy.types.Operator):
    """Edit the note of an existing version"""

    bl_idname = "savepoints.edit_note"
    bl_label = "Edit Note"
    bl_options = {"REGISTER"}
    translation_description = "Edit the note of an existing version"

    version_id: bpy.props.StringProperty(options={"HIDDEN"})
    new_note: bpy.props.StringProperty(
        name="Note", translation_context=TRANSLATION_CONTEXT
    )

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

    def draw(self, _context):
        layout = self.layout
        layout.prop(self, "new_note", text=iface("Note"))

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id
        if not version_id:
            return {"CANCELLED"}

        try:
            update_version_note(version_id, self.new_note)
        except Exception as e:
            self.report(
                {"ERROR"}, rpt("Failed to update note: {error}").format(error=e)
            )
            return {"CANCELLED"}

        sync_history_to_props(context)

        # Force UI redraw to update the note in the list immediately
        for area in context.window.screen.areas:
            area.tag_redraw()

        return {"FINISHED"}


class SAVEPOINTS_OT_set_tag(TranslatedOperatorMixin, bpy.types.Operator):
    """Set tag for a version"""

    bl_idname = "savepoints.set_tag"
    bl_label = "Set Tag"
    bl_options = {"REGISTER", "UNDO"}
    translation_description = "Set a tag for this version"

    version_id: bpy.props.StringProperty(options={"HIDDEN"})
    tag: bpy.props.EnumProperty(
        items=[
            ("NONE", "None", "", "NONE", 0),
            ("STABLE", "Stable", "", "CHECKMARK", 1),
            ("MILESTONE", "Milestone", "", "BOOKMARKS", 2),
            ("EXPERIMENT", "Experiment", "", "LAB", 3),
            ("BUG", "Bug", "", "ERROR", 4),
        ],
        translation_context=TRANSLATION_CONTEXT,
    )

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id
        if not version_id:
            return {"CANCELLED"}

        try:
            update_version_tag(version_id, self.tag)
        except Exception as e:
            self.report({"ERROR"}, rpt("Failed to set tag: {error}").format(error=e))
            return {"CANCELLED"}

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

        for area in context.window.screen.areas:
            area.tag_redraw()

        return {"FINISHED"}


class SAVEPOINTS_OT_toggle_protection(TranslatedOperatorMixin, bpy.types.Operator):
    """Toggle protection for a version"""

    bl_idname = "savepoints.toggle_protection"
    bl_label = "Toggle Protection"
    bl_options = {"REGISTER", "UNDO"}
    translation_description = "Lock or unlock this version"

    version_id: bpy.props.StringProperty()

    def execute(self, context):
        item = getattr(context, "savepoints_item", None)
        if item:
            version_id = item.version_id
        else:
            version_id = self.version_id

        if version_id == "autosave":
            return {"CANCELLED"}

        settings = context.scene.savepoints_settings

        target_item = None
        for v in settings.versions:
            if v.version_id == version_id:
                target_item = v
                break

        if not target_item:
            return {"CANCELLED"}

        new_state = not target_item.is_protected
        set_version_protection(version_id, new_state)
        target_item.is_protected = new_state
        return {"FINISHED"}
