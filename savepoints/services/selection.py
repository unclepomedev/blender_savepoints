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
    # 1. Capture State
    active_obj = bpy.context.view_layer.objects.active
    active_name = active_obj.name if active_obj else None

    # Store names to be robust against object pointer invalidation (though less likely in same session)
    selected_names = [obj.name for obj in bpy.context.selected_objects]

    # Capture mode from the active object if it exists, otherwise context
    original_mode = None
    if active_obj:
        original_mode = active_obj.mode
    else:
        # Fallback if no active object (unlikely to be in a mode other than OBJECT, but possible)
        if bpy.context.mode != 'OBJECT':
            # Mapping might be needed if context.mode differs from mode_set params
            # For now, rely on Object mode fallback
            pass

    try:
        yield
    finally:
        # 2. Restore State

        # Ensure we are in a state where we can select objects (OBJECT mode is safest)
        if bpy.context.mode != 'OBJECT':
            try:
                if bpy.ops.object.mode_set.poll():
                    bpy.ops.object.mode_set(mode='OBJECT')
            except Exception as e:
                print(f"[SavePoints] Warning: Failed to switch to OBJECT mode for selection restore: {e}")

        # Restore Active Object
        # We restore active object first because setting mode requires it
        if active_name and active_name in bpy.data.objects:
            obj = bpy.data.objects[active_name]
            bpy.context.view_layer.objects.active = obj

        # Clear current selection
        if bpy.ops.object.select_all.poll():
            bpy.ops.object.select_all(action='DESELECT')

        # Restore Selected Objects
        for name in selected_names:
            if name in bpy.data.objects:
                bpy.data.objects[name].select_set(True)

        # Restore Mode
        # Only try to restore mode if we have an active object that was in that mode
        if active_name and original_mode and original_mode != 'OBJECT':
            if bpy.context.view_layer.objects.active and bpy.context.view_layer.objects.active.mode != original_mode:
                try:
                    bpy.ops.object.mode_set(mode=original_mode)
                except Exception as e:
                    print(f"[SavePoints] Warning: Failed to restore mode {original_mode}: {e}")
