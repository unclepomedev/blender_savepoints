# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def change_frame(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: float = ..., snap: bool = ..., seq_solo_preview: bool = ...) -> Set[str]:
    """Interactively change the current frame number"""
    ...

def channel_select_keys(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> Set[str]:
    """Select all keyframes of channel under mouse"""
    ...

def channel_view_pick(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, include_handles: bool = ..., use_preview_range: bool = ...) -> Set[str]:
    """Reset viewable area to show the channel under the cursor"""
    ...

def channels_bake(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, range: int = ..., step: float = ..., remove_outside_range: bool = ..., interpolation_type: str = ..., bake_modifiers: bool = ...) -> Set[str]:
    """Create keyframes following the current shape of F-Curves of selected channels"""
    ...

def channels_clean_empty(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete all empty animation data containers from visible data-blocks"""
    ...

def channels_click(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., extend_range: bool = ..., children_only: bool = ...) -> Set[str]:
    """Handle mouse clicks over animation channels"""
    ...

def channels_collapse(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Collapse (close) all selected expandable animation channels"""
    ...

def channels_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete all selected animation channels"""
    ...

def channels_editable_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., type: str = ...) -> Set[str]:
    """Toggle editability of selected channels"""
    ...

def channels_expand(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Expand (open) all selected expandable animation channels"""
    ...

def channels_fcurves_enable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear 'disabled' tag from all F-Curves to get broken F-Curves working again"""
    ...

def channels_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Add selected F-Curves to a new group"""
    ...

def channels_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Rearrange selected animation channels"""
    ...

def channels_rename(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Rename animation channel under mouse"""
    ...

def channels_select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Toggle selection of all animation channels"""
    ...

def channels_select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., deselect: bool = ..., extend: bool = ...) -> Set[str]:
    """Select all animation channels within the specified region"""
    ...

def channels_select_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Start entering text which filters the set of channels shown to only include those with matching names"""
    ...

def channels_setting_disable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., type: str = ...) -> Set[str]:
    """Disable specified setting on all selected animation channels"""
    ...

def channels_setting_enable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., type: str = ...) -> Set[str]:
    """Enable specified setting on all selected animation channels"""
    ...

def channels_setting_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., type: str = ...) -> Set[str]:
    """Toggle specified setting on all selected animation channels"""
    ...

def channels_ungroup(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove selected F-Curves from their current groups"""
    ...

def channels_view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, include_handles: bool = ..., use_preview_range: bool = ...) -> Set[str]:
    """Reset viewable area to show the selected channels"""
    ...

def clear_useless_actions(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_unused: bool = ...) -> Set[str]:
    """Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries" """
    ...

def convert_legacy_action(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Convert a legacy Action to a layered Action on the active object"""
    ...

def copy_driver_button(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the driver for the highlighted button"""
    ...

def driver_button_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add driver for the property under the cursor"""
    ...

def driver_button_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Edit the drivers for the connected property represented by the highlighted button"""
    ...

def driver_button_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Remove the driver(s) for the connected property(s) represented by the highlighted button"""
    ...

def end_frame_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set the current frame as the preview or scene end frame"""
    ...

def keyframe_clear_button(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Clear all keyframes on the currently active property"""
    ...

def keyframe_clear_v3d(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Remove all keyframe animation for selected objects"""
    ...

def keyframe_clear_vse(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Remove all keyframe animation for selected strips"""
    ...

def keyframe_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Delete keyframes on the current frame for all properties in the specified Keying Set"""
    ...

def keyframe_delete_button(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Delete current keyframe of current UI-active property"""
    ...

def keyframe_delete_by_name(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Alternate access to 'Delete Keyframe' for keymaps to use"""
    ...

def keyframe_delete_v3d(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Remove keyframes on current frame for selected objects and bones"""
    ...

def keyframe_delete_vse(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Remove keyframes on current frame for selected strips"""
    ...

def keyframe_insert(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Insert keyframes on the current frame using either the active keying set, or the user preferences if no keying set is active"""
    ...

def keyframe_insert_button(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Insert a keyframe for current UI-active property"""
    ...

def keyframe_insert_by_name(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Alternate access to 'Insert Keyframe' for keymaps to use"""
    ...

def keyframe_insert_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., always_prompt: bool = ...) -> Set[str]:
    """Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined"""
    ...

def keying_set_active_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set a new active keying set"""
    ...

def keying_set_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new (empty) keying set to the active Scene"""
    ...

def keying_set_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., filter_folder: bool = ..., filter_text: bool = ..., filter_python: bool = ...) -> Set[str]:
    """Export Keying Set to a Python script"""
    ...

def keying_set_path_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add empty path to active keying set"""
    ...

def keying_set_path_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove active Path from active keying set"""
    ...

def keying_set_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the active keying set"""
    ...

def keyingset_button_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Add current UI-active property to current keying set"""
    ...

def keyingset_button_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove current UI-active property from current keying set"""
    ...

def merge_animation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this, but might end up with zero users"""
    ...

def paste_driver_button(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Paste the driver in the internal clipboard to the highlighted button"""
    ...

def previewrange_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear preview range"""
    ...

def previewrange_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """Interactively define frame range used for playback"""
    ...

def scene_range_frame(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active"""
    ...

def separate_slots(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move all slots of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action won't be deleted but will be empty and might end up having zero users"""
    ...

def slot_channels_move_to_new_action(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move the selected slots into a newly created action"""
    ...

def slot_new_for_id(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new action slot for this data-block, to hold its animation"""
    ...

def slot_unassign_from_constraint(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Un-assign the action slot from this constraint"""
    ...

def slot_unassign_from_id(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Un-assign the action slot, effectively making this data-block non-animated"""
    ...

def slot_unassign_from_nla_strip(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Un-assign the action slot from this NLA strip, effectively making it non-animated"""
    ...

def start_frame_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set the current frame as the preview or scene start frame"""
    ...

def update_animated_transform_constraints(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_convert_to_radians: bool = ...) -> Set[str]:
    """Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)"""
    ...

def version_bone_hide_property(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Moves any F-Curves for the `hide` property of selected armatures into the action of the object. This will only operate on the first layer and strip of the action"""
    ...

def view_curve_in_graph_editor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ..., isolate: bool = ...) -> Set[str]:
    """Frame the property under the cursor in the Graph Editor"""
    ...
