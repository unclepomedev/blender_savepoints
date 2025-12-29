# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


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
        default=False
    )
    tag: bpy.props.EnumProperty(
        name="Tag",
        items=[
            ('NONE', "None", "", 'NONE', 0),
            ('STABLE', "Stable", "", 'CHECKMARK', 1),
            ('MILESTONE', "Milestone", "", 'BOOKMARKS', 2),
            ('EXPERIMENT', "Experiment", "", 'EXPERIMENTAL', 3),
            ('BUG', "Bug", "", 'ERROR', 4),
        ],
        default='NONE'
    )


def update_filter_tag(self, context):
    if context.area:
        context.area.tag_redraw()

    # Deselect items that do not match the new filter
    if self.filter_tag != 'ALL':
        for version in self.versions:
            if version.tag != self.filter_tag:
                version.selected = False


class SavePointsSettings(bpy.types.PropertyGroup):
    versions: bpy.props.CollectionProperty(type=SavePointsVersion)
    active_version_index: bpy.props.IntProperty(name="Active Version Index", default=-1)

    filter_tag: bpy.props.EnumProperty(
        name="Filter Tag",
        items=[
            ('ALL', "All", "", 'FILTER', 0),
            ('STABLE', "Stable", "", 'CHECKMARK', 1),
            ('MILESTONE', "Milestone", "", 'BOOKMARKS', 2),
            ('EXPERIMENT', "Experiment", "", 'EXPERIMENTAL', 3),
            ('BUG', "Bug", "", 'ERROR', 4),
        ],
        default='ALL',
        update=update_filter_tag
    )

    show_save_dialog: bpy.props.BoolProperty(
        name="Show Save Dialog",
        description="Show the note input dialog when saving a version. Disable for instant 'Quick Save'",
        default=True
    )

    show_preview: bpy.props.BoolProperty(
        name="Show Preview",
        description="Show thumbnail preview in the version details panel",
        default=True
    )

    use_compression: bpy.props.BoolProperty(
        name="Compress Snapshots",
        description="Compresses the snapshot file. Saves disk space (~40-60%) but increases save time.",
        default=False,
    )

    use_limit_versions: bpy.props.BoolProperty(
        name="Limit Versions",
        description="Enable automatic deletion of old versions to save disk space",
        default=False
    )

    max_versions_to_keep: bpy.props.IntProperty(
        name="Max Versions",
        description="Number of versions to keep (when enabled)",
        default=50,
        min=1
    )

    # Auto Save Settings
    use_auto_save: bpy.props.BoolProperty(
        name="Auto Save",
        description="Enable auto-save to a dedicated 'autosave' slot",
        default=True
    )
    auto_save_interval: bpy.props.IntProperty(
        name="Interval (min)",
        description="Auto-save interval in minutes",
        default=10,
        min=1
    )
    last_autosave_timestamp: bpy.props.StringProperty(default="0.0")

    is_batch_mode: bpy.props.BoolProperty(
        name="Batch Mode",
        description="Toggle batch operation mode",
        default=False,
        update=lambda self, context: context.area.tag_redraw() if context.area else None
    )

    batch_output_format: bpy.props.EnumProperty(
        name="Output Format",
        description="Select the output file format for batch rendering",
        items=[
            ('SCENE', "Scene Settings", "Use the format defined in the current scene"),
            ('PNG', "PNG", "Force PNG format"),
            ('JPEG', "JPEG", "Force JPEG format"),
        ],
        default='SCENE'
    )
