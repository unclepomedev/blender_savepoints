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


def update_keep_daily_backups(self, context):
    if not self.keep_daily_backups:
        if context.window_manager.get("savepoints_daily_backup_confirmed"):
            context.window_manager["savepoints_daily_backup_confirmed"] = False
        else:
            self.keep_daily_backups = True

            def open_confirm():
                bpy.ops.savepoints.confirm_disable_daily_backups('INVOKE_DEFAULT')
                return None

            bpy.app.timers.register(open_confirm, first_interval=0.01)


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
        update=lambda self, context: context.area.tag_redraw() if context.area else None
    )

    show_save_dialog: bpy.props.BoolProperty(
        name="Show Save Dialog",
        description="Show the note input dialog when saving a version. Disable for instant 'Quick Save'",
        default=True
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

    keep_daily_backups: bpy.props.BoolProperty(
        name="Keep Daily Backups (Last 14 days)",
        description="Keep the last snapshot of each day for the past 14 days, even if the Max Count is exceeded",
        default=False,
        update=update_keep_daily_backups
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
