# SPDX-License-Identifier: GPL-3.0-or-later

from contextlib import contextmanager

import bpy


@contextmanager
def preserve_selection():
    """
    Context manager to preserve the current selection state and active object.
    
    Restores:
    - Active Object
    - Selected Objects
    - Mode (e.g. EDIT, SCULPT, POSE)
    """
    view_layer = bpy.context.view_layer
    active_obj = view_layer.objects.active
    active_name = active_obj.name if active_obj else None

    selected_names = [obj.name for obj in bpy.context.selected_objects]

    original_mode = active_obj.mode if active_obj else bpy.context.mode

    try:
        yield
    finally:
        if bpy.context.mode != 'OBJECT':
            try:
                poll_func = getattr(bpy.ops.object.mode_set, "poll", None)
                if poll_func and poll_func():
                    bpy.ops.object.mode_set(mode='OBJECT')
            except Exception as e:
                print(f"[SavePoints] Warning: Failed to switch to OBJECT mode: {e}")

        for obj in bpy.context.selected_objects:
            obj.select_set(False)

        view_layer.objects.active = None
        if active_name and active_name in bpy.data.objects:
            obj = bpy.data.objects[active_name]
            view_layer.objects.active = obj

        for name in selected_names:
            if name in bpy.data.objects:
                bpy.data.objects[name].select_set(True)

        if active_name and original_mode != 'OBJECT':
            if view_layer.objects.active and view_layer.objects.active.name == active_name:
                try:
                    bpy.ops.object.mode_set(mode=original_mode)
                except Exception as e:
                    print(f"[SavePoints] Warning: Failed to restore mode {original_mode}: {e}")


def get_selected_versions(settings):
    """
    Returns a list of versions that are currently selected in the UI.
    Excludes 'autosave' or invalid IDs.

    Args:
        settings (SavePointsSettings): The settings property group containing versions.

    Returns:
        list[SavePointsVersion]: List of selected version items.
    """
    return [
        v for v in settings.versions
        if v.version_id.startswith('v') and v.selected
    ]
