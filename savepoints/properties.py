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


class SavePointsSettings(bpy.types.PropertyGroup):
    versions: bpy.props.CollectionProperty(type=SavePointsVersion)
    active_version_index: bpy.props.IntProperty(name="Active Version Index", default=-1)
