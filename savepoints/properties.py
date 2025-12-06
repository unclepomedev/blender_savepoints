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



def update_auto_save_interval(self, context):
    import time
    
    interval_min = self.auto_save_interval
    if interval_min < 1:
        interval_min = 1
    
    interval_sec = interval_min * 60.0
    now = time.time()
    
    try:
        last_save = float(self.last_autosave_timestamp)
    except ValueError:
        last_save = 0.0
        
    if last_save > 0:
        new_next = last_save + interval_sec
        # If we missed the window, schedule immediately
        if new_next < now:
            self.next_autosave_timestamp = str(now)
        else:
            self.next_autosave_timestamp = str(new_next)
    else:
        # If never saved, schedule from now
        self.next_autosave_timestamp = str(now + interval_sec)


class SavePointsSettings(bpy.types.PropertyGroup):
    versions: bpy.props.CollectionProperty(type=SavePointsVersion)
    active_version_index: bpy.props.IntProperty(name="Active Version Index", default=-1)

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
        min=1,
        update=update_auto_save_interval
    )
    last_autosave_timestamp: bpy.props.StringProperty(default="0.0")
    next_autosave_timestamp: bpy.props.StringProperty(default="0.0")
    autosave_fail_count: bpy.props.IntProperty(default=0)
