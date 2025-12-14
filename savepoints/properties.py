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


class SavePointsSettings(bpy.types.PropertyGroup):
    versions: bpy.props.CollectionProperty(type=SavePointsVersion)
    active_version_index: bpy.props.IntProperty(name="Active Version Index", default=-1)

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
