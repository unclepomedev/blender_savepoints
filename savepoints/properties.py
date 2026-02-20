# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


class RetrieveObjectItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Name")
    selected: bpy.props.BoolProperty(name="Select", default=False)


class SavePointsVersion(bpy.types.PropertyGroup):
    version_id: bpy.props.StringProperty(name="ID")
    timestamp: bpy.props.StringProperty(name="Time")
    note: bpy.props.StringProperty(name="Note")
    thumbnail_rel_path: bpy.props.StringProperty(name="Thumbnail Path")
    blend_rel_path: bpy.props.StringProperty(name="Blend Path")
    object_count: bpy.props.IntProperty(name="Object Count", default=0)
    file_size_display: bpy.props.StringProperty(name="File Size", default="")
    is_protected: bpy.props.BoolProperty(name="Protected", default=False)
    selected: bpy.props.BoolProperty(
        name="Selected",
        description="Select this version for batch operations",
        default=False,
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
    active_version_index: bpy.props.IntProperty(name="Active Version Index", default=-1)

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
    )

    show_save_dialog: bpy.props.BoolProperty(
        name="Show Save Dialog",
        description="Show the note input dialog when saving a version. Disable for instant 'Quick Save'",
        default=True,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    show_preview: bpy.props.BoolProperty(
        name="Show Preview",
        description="Show thumbnail preview in the version details panel",
        default=True,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    use_limit_versions: bpy.props.BoolProperty(
        name="Limit Versions",
        description="Enable automatic deletion of old versions to save disk space",
        default=False,
    )

    max_versions_to_keep: bpy.props.IntProperty(
        name="Max Versions",
        description="Number of versions to keep (when enabled)",
        default=50,
        min=1,
    )

    # Auto Save Settings
    use_auto_save: bpy.props.BoolProperty(
        name="Auto Save",
        description="Enable auto-save to a dedicated 'autosave' slot",
        default=True,
    )
    auto_save_interval: bpy.props.IntProperty(
        name="Interval (min)",
        description="Auto-save interval in minutes",
        default=10,
        min=1,
    )
    last_autosave_timestamp: bpy.props.StringProperty(default="0.0")

    show_autosave_warning: bpy.props.BoolProperty(
        name="Show Autosave Warning",
        default=False,
    )

    autosave_warning_message: bpy.props.StringProperty(
        name="Autosave Warning Message",
        default="",
    )

    is_batch_mode: bpy.props.BoolProperty(
        name="Batch Mode",
        description="Toggle batch operation mode",
        default=False,
        update=lambda self, context: (
            context.area.tag_redraw() if context.area else None
        ),
    )

    batch_output_format: bpy.props.EnumProperty(
        name="Output Format",
        description="Select the output file format for batch rendering",
        items=[
            ("SCENE", "Scene Settings", "Use the format defined in the current scene"),
            ("PNG", "PNG", "Force PNG format"),
            ("JPEG", "JPEG", "Force JPEG format"),
        ],
        default="SCENE",
    )

    batch_create_mp4: bpy.props.BoolProperty(
        name="Create Timelapse MP4",
        description="Automatically create and export an MP4 timelapse after batch rendering",
        default=False,
    )

    batch_burn_in: bpy.props.BoolProperty(
        name="Burn-in Version ID",
        description="Overlay version ID on the video",
        default=False,
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
    )

    glb_export_path: bpy.props.StringProperty(
        name="Export Path",
        description="Directory to export .glb files",
        default="//",
        subtype="DIR_PATH",
    )

    glb_export_filename: bpy.props.StringProperty(
        name="Filename",
        description="Filename (stem) for the exported .glb file. Default (empty) is .blend filename. Use {version} for version string.",
        default="",
    )


class SavePointsPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__ or "savepoints"

    enable_glb_export: bpy.props.BoolProperty(
        name="Enable Background GLB Export",
        description="Enable the experimental background GLB export feature",
        default=False,
    )

    enable_post_save: bpy.props.BoolProperty(
        name="Enable Post-Save Command",
        description="Execute a shell command after saving a version",
        default=False,
    )

    post_save_command: bpy.props.StringProperty(
        name="Post-Save Command",
        description="Shell command to execute. Supports {filepath}, {version}, {history_dir}, {version_dir}, {note}",
        default="",
    )

    use_compression: bpy.props.BoolProperty(
        name="Compress Snapshots",
        description="Compresses the snapshot file. Saves disk space (~40-60%) but increases save time.",
        default=True,
    )

    def draw(self, _context):
        layout = self.layout
        box_glb = layout.box()
        box_glb.prop(self, "enable_glb_export")

        box_cmd = layout.box()
        box_cmd.prop(self, "enable_post_save")
        if self.enable_post_save:
            col = box_cmd.column()
            col.separator()
            col.prop(self, "post_save_command", text="Command")
            col.label(
                text="Placeholders: {filepath}, {version}, {history_dir}, {version_dir}, {note}",
                icon="INFO",
            )

        box_comp = layout.box()
        box_comp.prop(self, "use_compression")
