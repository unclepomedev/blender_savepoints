# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

from .i18n import AUTO_LANGUAGE, TranslatedOperatorMixin, iface, refresh, tooltip
from .translations import TRANSLATION_CONTEXT


def update_ui_language(_self, context):
    """Reload Blender-drawn text and redraw after a language change."""
    refresh()
    window_manager = getattr(context, "window_manager", None)
    if not window_manager:
        return
    for window in window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()


def _addon_preferences(context):
    """Find SavePoints preferences for legacy and extension installations."""
    addons = context.preferences.addons
    addon = addons.get(__package__ or "savepoints")
    if addon is None:
        for key, candidate in addons.items():
            if key.endswith("savepoints"):
                addon = candidate
                break
    return getattr(addon, "preferences", None)


_LANGUAGE_TOOLTIPS = {
    AUTO_LANGUAGE: "Use Blender's current interface language",
    "en_US": "Use English for SavePoints",
    "zh_HANS": "Use Simplified Chinese for SavePoints",
    "ja_JP": "Use Japanese for SavePoints",
}

_PREFERENCE_TOOLTIPS = {
    "enable_glb_export": "Enable the experimental background GLB export feature",
    "enable_post_save": "Execute a shell command after saving a version",
    "use_compression": "Compresses the snapshot file. Saves disk space (~40-60%) but increases save time.",
}

_SETTING_TOOLTIPS = {
    "show_save_dialog": "Show the note input dialog when saving a version. Disable for instant 'Quick Save'",
    "show_preview": "Show thumbnail preview in the version details panel",
    "use_limit_versions": "Enable automatic deletion of old versions to save disk space",
    "use_auto_save": "Enable auto-save to a dedicated 'autosave' slot",
}

_SETTING_VALUE_TOOLTIPS = {
    ("filter_tag", "ALL"): "Show versions with any tag",
    ("filter_tag", "STABLE"): "Show only stable versions",
    ("filter_tag", "MILESTONE"): "Show only milestone versions",
    ("filter_tag", "EXPERIMENT"): "Show only experiment versions",
    ("filter_tag", "BUG"): "Show only versions marked as bugs",
    ("batch_output_format", "SCENE"): "Use the format defined in the current scene",
    ("batch_output_format", "PNG"): "Force PNG format",
    ("batch_output_format", "JPEG"): "Force JPEG format",
    ("batch_burn_in_pos", "TL"): "Place the version ID in the top-left corner",
    ("batch_burn_in_pos", "TR"): "Place the version ID in the top-right corner",
    ("batch_burn_in_pos", "BL"): "Place the version ID in the bottom-left corner",
    ("batch_burn_in_pos", "BR"): "Place the version ID in the bottom-right corner",
}


class SAVEPOINTS_OT_set_language(TranslatedOperatorMixin, bpy.types.Operator):
    """Set SavePoints language without relying on an RNA property tooltip."""

    bl_idname = "savepoints.set_language"
    bl_label = "Set SavePoints Language"
    bl_options = {"INTERNAL"}

    language: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, properties):
        language = getattr(properties, "language", "")
        return tooltip(_LANGUAGE_TOOLTIPS.get(language, ""))

    def execute(self, context):
        preferences = _addon_preferences(context)
        if preferences is None or self.language not in _LANGUAGE_TOOLTIPS:
            return {"CANCELLED"}
        preferences.ui_language = self.language
        return {"FINISHED"}


class SAVEPOINTS_OT_toggle_preference(TranslatedOperatorMixin, bpy.types.Operator):
    """Toggle a SavePoints preference with a manually translated tooltip."""

    bl_idname = "savepoints.toggle_preference"
    bl_label = "Toggle SavePoints Preference"
    bl_options = {"INTERNAL"}

    preference: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, properties):
        preference = getattr(properties, "preference", "")
        return tooltip(_PREFERENCE_TOOLTIPS.get(preference, ""))

    def execute(self, context):
        preferences = _addon_preferences(context)
        if preferences is None or self.preference not in _PREFERENCE_TOOLTIPS:
            return {"CANCELLED"}
        setattr(preferences, self.preference, not getattr(preferences, self.preference))
        return {"FINISHED"}


class SAVEPOINTS_OT_toggle_setting(TranslatedOperatorMixin, bpy.types.Operator):
    """Toggle a scene setting with a manually translated tooltip."""

    bl_idname = "savepoints.toggle_setting"
    bl_label = "Toggle SavePoints Setting"
    bl_options = {"INTERNAL"}

    setting: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, properties):
        setting = getattr(properties, "setting", "")
        return tooltip(_SETTING_TOOLTIPS.get(setting, ""))

    def execute(self, context):
        if self.setting not in _SETTING_TOOLTIPS:
            return {"CANCELLED"}
        settings = context.scene.savepoints_settings
        setattr(settings, self.setting, not getattr(settings, self.setting))
        return {"FINISHED"}


class SAVEPOINTS_OT_toggle_version_selection(
    TranslatedOperatorMixin, bpy.types.Operator
):
    """Toggle a history item's batch selection with a translated tooltip."""

    bl_idname = "savepoints.toggle_version_selection"
    bl_label = "Toggle Version Selection"
    bl_options = {"INTERNAL"}

    version_id: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, _properties):
        return tooltip("Select this version for batch operations")

    def execute(self, context):
        settings = context.scene.savepoints_settings
        for version in settings.versions:
            if version.version_id == self.version_id:
                version.selected = not version.selected
                return {"FINISHED"}
        return {"CANCELLED"}


class SAVEPOINTS_OT_set_setting_value(TranslatedOperatorMixin, bpy.types.Operator):
    """Set a whitelisted enum setting with a translated tooltip."""

    bl_idname = "savepoints.set_setting_value"
    bl_label = "Set SavePoints Setting"
    bl_options = {"INTERNAL"}

    setting: bpy.props.StringProperty(options={"HIDDEN"})
    value: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, properties):
        key = (
            getattr(properties, "setting", ""),
            getattr(properties, "value", ""),
        )
        return tooltip(_SETTING_VALUE_TOOLTIPS.get(key, ""))

    def execute(self, context):
        if (self.setting, self.value) not in _SETTING_VALUE_TOOLTIPS:
            return {"CANCELLED"}
        setattr(context.scene.savepoints_settings, self.setting, self.value)
        return {"FINISHED"}


class SAVEPOINTS_OT_help(TranslatedOperatorMixin, bpy.types.Operator):
    """Display a translated tooltip for controls Blender draws from RNA."""

    bl_idname = "savepoints.help"
    bl_label = "SavePoints Help"
    bl_options = {"INTERNAL"}

    message: bpy.props.StringProperty(options={"HIDDEN"})

    @classmethod
    def description(cls, _context, properties):
        return tooltip(getattr(properties, "message", ""))

    def execute(self, _context):
        return {"FINISHED"}


def draw_setting_toggle(layout, settings, property_name: str, *, text: str):
    """Draw a checkbox-style scene setting with a dynamic tooltip."""
    operator = layout.operator(
        SAVEPOINTS_OT_toggle_setting.bl_idname,
        text=text,
        icon="CHECKBOX_HLT" if getattr(settings, property_name) else "CHECKBOX_DEHLT",
        emboss=False,
    )
    operator.setting = property_name
    return operator


def draw_property_with_help(
    layout,
    data,
    property_name: str,
    *,
    text: str,
    message: str,
    **property_options,
):
    """Draw an editable RNA property beside a dynamic translated tooltip."""
    row = layout.row(align=True)
    row.prop(data, property_name, text=text, **property_options)
    help_operator = row.operator(
        SAVEPOINTS_OT_help.bl_idname,
        text="",
        icon="QUESTION",
        emboss=False,
    )
    help_operator.message = message
    return row


def draw_setting_value(
    layout,
    settings,
    property_name: str,
    value: str,
    *,
    text: str,
    icon: str = "NONE",
):
    """Draw an explicit enum-value button independent of Blender translations."""
    operator = layout.operator(
        SAVEPOINTS_OT_set_setting_value.bl_idname,
        text=text,
        icon=icon,
        depress=getattr(settings, property_name) == value,
    )
    operator.setting = property_name
    operator.value = value
    return operator


class RetrieveObjectItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Name", translation_context=TRANSLATION_CONTEXT)
    selected: bpy.props.BoolProperty(
        name="Select", default=False, translation_context=TRANSLATION_CONTEXT
    )


class SavePointsVersion(bpy.types.PropertyGroup):
    version_id: bpy.props.StringProperty(
        name="ID", translation_context=TRANSLATION_CONTEXT
    )
    timestamp: bpy.props.StringProperty(
        name="Time", translation_context=TRANSLATION_CONTEXT
    )
    note: bpy.props.StringProperty(name="Note", translation_context=TRANSLATION_CONTEXT)
    thumbnail_rel_path: bpy.props.StringProperty(
        name="Thumbnail Path", translation_context=TRANSLATION_CONTEXT
    )
    blend_rel_path: bpy.props.StringProperty(
        name="Blend Path", translation_context=TRANSLATION_CONTEXT
    )
    object_count: bpy.props.IntProperty(
        name="Object Count", default=0, translation_context=TRANSLATION_CONTEXT
    )
    file_size_display: bpy.props.StringProperty(
        name="File Size", default="", translation_context=TRANSLATION_CONTEXT
    )
    is_protected: bpy.props.BoolProperty(
        name="Protected", default=False, translation_context=TRANSLATION_CONTEXT
    )
    selected: bpy.props.BoolProperty(
        name="Selected",
        description="",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )
    tag: bpy.props.EnumProperty(
        name="Tag",
        items=[
            ("NONE", "None", "", "NONE", 0),
            ("STABLE", "Stable", "", "CHECKMARK", 1),
            ("MILESTONE", "Milestone", "", "BOOKMARKS", 2),
            ("EXPERIMENT", "Experiment", "", "EXPERIMENTAL", 3),
            ("BUG", "Bug", "", "ERROR", 4),
        ],
        default="NONE",
        translation_context=TRANSLATION_CONTEXT,
    )


def update_filter_tag(self, context):
    if context.area:
        context.area.tag_redraw()

    # Deselect items that do not match the new filter
    if self.filter_tag != "ALL":
        for version in self.versions:
            if version.tag != self.filter_tag:
                version.selected = False


class SavePointsSettings(bpy.types.PropertyGroup):
    versions: bpy.props.CollectionProperty(type=SavePointsVersion)
    active_version_index: bpy.props.IntProperty(
        name="Active Version Index",
        default=-1,
        translation_context=TRANSLATION_CONTEXT,
    )

    filter_tag: bpy.props.EnumProperty(
        name="Filter Tag",
        items=[
            ("ALL", "All", "", "FILTER", 0),
            ("STABLE", "Stable", "", "CHECKMARK", 1),
            ("MILESTONE", "Milestone", "", "BOOKMARKS", 2),
            ("EXPERIMENT", "Experiment", "", "EXPERIMENTAL", 3),
            ("BUG", "Bug", "", "ERROR", 4),
        ],
        default="ALL",
        update=update_filter_tag,
        translation_context=TRANSLATION_CONTEXT,
    )

    show_save_dialog: bpy.props.BoolProperty(
        name="Show Save Dialog",
        description="Show the note input dialog when saving a version. Disable for instant 'Quick Save'",
        default=True,
        translation_context=TRANSLATION_CONTEXT,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    show_preview: bpy.props.BoolProperty(
        name="Show Preview",
        description="Show thumbnail preview in the version details panel",
        default=True,
        translation_context=TRANSLATION_CONTEXT,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    use_limit_versions: bpy.props.BoolProperty(
        name="Limit Versions",
        description="Enable automatic deletion of old versions to save disk space",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    max_versions_to_keep: bpy.props.IntProperty(
        name="Max Versions",
        description="",
        default=50,
        min=1,
        translation_context=TRANSLATION_CONTEXT,
    )

    # Auto Save Settings
    use_auto_save: bpy.props.BoolProperty(
        name="Auto Save",
        description="Enable auto-save to a dedicated 'autosave' slot",
        default=True,
        translation_context=TRANSLATION_CONTEXT,
    )
    auto_save_interval: bpy.props.IntProperty(
        name="Interval (min)",
        description="",
        default=10,
        min=1,
        translation_context=TRANSLATION_CONTEXT,
    )
    last_autosave_timestamp: bpy.props.StringProperty(default="0.0")

    show_autosave_warning: bpy.props.BoolProperty(
        name="Show Autosave Warning",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    autosave_warning_message: bpy.props.StringProperty(
        name="Autosave Warning Message",
        default="",
        translation_context=TRANSLATION_CONTEXT,
    )

    is_batch_mode: bpy.props.BoolProperty(
        name="Batch Mode",
        description="Toggle batch operation mode",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    batch_output_format: bpy.props.EnumProperty(
        name="Output Format",
        description="",
        items=[
            ("SCENE", "Scene Settings", ""),
            ("PNG", "PNG", ""),
            ("JPEG", "JPEG", ""),
        ],
        default="SCENE",
        translation_context=TRANSLATION_CONTEXT,
    )

    batch_create_mp4: bpy.props.BoolProperty(
        name="Create Timelapse MP4",
        description="",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    batch_burn_in: bpy.props.BoolProperty(
        name="Burn-in Version ID",
        description="",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    batch_burn_in_pos: bpy.props.EnumProperty(
        name="Position",
        items=[
            ("TL", "Top-Left", ""),
            ("TR", "Top-Right", ""),
            ("BL", "Bottom-Left", ""),
            ("BR", "Bottom-Right", ""),
        ],
        default="BL",
        translation_context=TRANSLATION_CONTEXT,
    )

    glb_export_path: bpy.props.StringProperty(
        name="Export Path",
        description="",
        default="//",
        subtype="DIR_PATH",
        translation_context=TRANSLATION_CONTEXT,
    )

    glb_export_filename: bpy.props.StringProperty(
        name="Filename",
        description="",
        default="",
        translation_context=TRANSLATION_CONTEXT,
    )


class SavePointsPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__ or "savepoints"
    bl_translation_context = TRANSLATION_CONTEXT

    ui_language: bpy.props.EnumProperty(
        name="SavePoints Language",
        description="",
        items=[
            (
                AUTO_LANGUAGE,
                "Auto (Follow Blender)",
                "Use Blender's current interface language",
                "WORLD",
                0,
            ),
            ("en_US", "English", "English", "NONE", 1),
            ("zh_HANS", "简体中文", "简体中文", "NONE", 2),
            ("ja_JP", "日本語", "日本語", "NONE", 3),
        ],
        default=AUTO_LANGUAGE,
        update=update_ui_language,
        translation_context=TRANSLATION_CONTEXT,
    )

    enable_glb_export: bpy.props.BoolProperty(
        name="Enable Background GLB Export",
        description="Enable the experimental background GLB export feature",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    enable_post_save: bpy.props.BoolProperty(
        name="Enable Post-Save Command",
        description="Execute a shell command after saving a version",
        default=False,
        translation_context=TRANSLATION_CONTEXT,
    )

    post_save_command: bpy.props.StringProperty(
        name="Post-Save Command",
        description="",
        default="",
        translation_context=TRANSLATION_CONTEXT,
    )

    use_compression: bpy.props.BoolProperty(
        name="Compress Snapshots",
        description="Compresses the snapshot file. Saves disk space (~40-60%) but increases save time.",
        default=True,
        translation_context=TRANSLATION_CONTEXT,
    )

    def draw(self, _context):
        layout = self.layout
        language = self.ui_language

        box_language = layout.box()
        box_language.label(text=iface("Language", language=language))
        auto_op = box_language.operator(
            SAVEPOINTS_OT_set_language.bl_idname,
            text=iface("Auto (Follow Blender)", language=language),
            icon="WORLD",
            depress=language == AUTO_LANGUAGE,
        )
        auto_op.language = AUTO_LANGUAGE

        language_row = box_language.row(align=True)
        for language_id, label in (
            ("en_US", "English"),
            ("zh_HANS", "简体中文"),
            ("ja_JP", "日本語"),
        ):
            language_op = language_row.operator(
                SAVEPOINTS_OT_set_language.bl_idname,
                text=label,
                depress=language == language_id,
            )
            language_op.language = language_id

        box_glb = layout.box()
        glb_op = box_glb.operator(
            SAVEPOINTS_OT_toggle_preference.bl_idname,
            text=iface("Enable Background GLB Export", language=language),
            icon="CHECKBOX_HLT" if self.enable_glb_export else "CHECKBOX_DEHLT",
            emboss=False,
        )
        glb_op.preference = "enable_glb_export"

        box_cmd = layout.box()
        command_op = box_cmd.operator(
            SAVEPOINTS_OT_toggle_preference.bl_idname,
            text=iface("Enable Post-Save Command", language=language),
            icon="CHECKBOX_HLT" if self.enable_post_save else "CHECKBOX_DEHLT",
            emboss=False,
        )
        command_op.preference = "enable_post_save"
        if self.enable_post_save:
            col = box_cmd.column()
            col.separator()
            command_row = col.row(align=True)
            command_row.prop(
                self,
                "post_save_command",
                text=iface("Command", language=language),
            )
            command_help = command_row.operator(
                SAVEPOINTS_OT_help.bl_idname,
                text="",
                icon="QUESTION",
                emboss=False,
            )
            command_help.message = (
                "Shell command to execute. Supports {filepath}, {version}, "
                "{history_dir}, {version_dir}, {note}"
            )
            col.label(
                text=iface(
                    "Placeholders: {filepath}, {version}, {history_dir}, {version_dir}, {note}",
                    language=language,
                ),
                icon="INFO",
            )

        box_comp = layout.box()
        compression_op = box_comp.operator(
            SAVEPOINTS_OT_toggle_preference.bl_idname,
            text=iface("Compress Snapshots", language=language),
            icon="CHECKBOX_HLT" if self.use_compression else "CHECKBOX_DEHLT",
            emboss=False,
        )
        compression_op.preference = "use_compression"
