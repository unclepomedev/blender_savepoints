# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def action_pushdown(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, track_index: int = ...) -> Set[str]:
    """Push action down onto the top of the NLA stack as a new strip"""
    ...

def action_sync_length(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, active: bool = ...) -> Set[str]:
    """Synchronize the length of the referenced Action with the length used in the strip"""
    ...

def action_unlink(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, force_delete: bool = ...) -> Set[str]:
    """Unlink this action from the active action slot (and/or exit Tweak Mode)"""
    ...

def actionclip_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track"""
    ...

def apply_scale(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Apply scaling of selected strips to their referenced Actions"""
    ...

def bake(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame_start: int = ..., frame_end: int = ..., step: int = ..., only_selected: bool = ..., visual_keying: bool = ..., clear_constraints: bool = ..., clear_parents: bool = ..., use_current_action: bool = ..., clean_curves: bool = ..., bake_types: str = ..., channel_types: str = ...) -> Set[str]:
    """Bake all selected objects location/scale/rotation animation to an action"""
    ...

def channels_click(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> Set[str]:
    """Handle clicks to select NLA tracks"""
    ...

def clear_scale(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset scaling of selected strips"""
    ...

def click_select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., deselect_all: bool = ...) -> Set[str]:
    """Handle clicks to select NLA Strips"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete selected strips"""
    ...

def duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, linked: bool = ...) -> Set[str]:
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)"""
    ...

def duplicate_linked_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NLA_OT_duplicate: 'NLA_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> Set[str]:
    """Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)"""
    ...

def duplicate_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NLA_OT_duplicate: 'NLA_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> Set[str]:
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)"""
    ...

def fmodifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., only_active: bool = ...) -> Set[str]:
    """Add F-Modifier to the active/selected NLA-Strips"""
    ...

def fmodifier_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the F-Modifier(s) of the active NLA-Strip"""
    ...

def fmodifier_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_active: bool = ..., replace: bool = ...) -> Set[str]:
    """Add copied F-Modifiers to the selected NLA-Strips"""
    ...

def make_single_user(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Make linked action local to each strip"""
    ...

def meta_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new meta-strips incorporating the selected strips"""
    ...

def meta_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Separate out the strips held by the selected meta-strips"""
    ...

def move_down(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move selected strips down a track if there's room"""
    ...

def move_up(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move selected strips up a track if there's room"""
    ...

def mute_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Mute or un-mute selected strips"""
    ...

def previewrange_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set Preview Range based on extends of selected strips"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Select or deselect all NLA-Strips"""
    ...

def select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis_range: bool = ..., tweak: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Use box selection to grab NLA-Strips"""
    ...

def select_leftright(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., extend: bool = ...) -> Set[str]:
    """Select strips to the left or the right of the current frame"""
    ...

def selected_objects_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make selected objects appear in NLA Editor by adding Animation Data"""
    ...

def snap(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Move start of strips to specified time"""
    ...

def soundclip_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a strip for controlling when speaker plays its sound clip"""
    ...

def split(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Split selected strips at their midpoints"""
    ...

def swap(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Swap order of selected strips within tracks"""
    ...

def tracks_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, above_selected: bool = ...) -> Set[str]:
    """Add NLA-Tracks above/after the selected tracks"""
    ...

def tracks_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete selected NLA-Tracks and the strips they contain"""
    ...

def transition_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a transition strip between two adjacent selected strips"""
    ...

def tweakmode_enter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, isolate_action: bool = ..., use_upper_stack_evaluation: bool = ...) -> Set[str]:
    """Enter tweaking mode for the action referenced by the active strip to edit its keyframes"""
    ...

def tweakmode_exit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, isolate_action: bool = ...) -> Set[str]:
    """Exit tweaking mode for the action referenced by the active strip"""
    ...

def view_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset viewable area to show full strips range"""
    ...

def view_frame(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move the view to the current frame"""
    ...

def view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset viewable area to show selected strips range"""
    ...
