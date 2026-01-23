# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def armature_apply(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, selected: bool = ...) -> Set[str]:
    """Apply the current pose as the new rest pose"""
    ...

def autoside_names(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis: str = ...) -> Set[str]:
    """Automatically renames the selected bones according to which side of the target axis they fall on"""
    ...

def blend_to_neighbor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., prev_frame: int = ..., next_frame: int = ..., channels: str = ..., axis_lock: str = ...) -> Set[str]:
    """Blend from current position to previous or next keyframe"""
    ...

def blend_with_rest(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., prev_frame: int = ..., next_frame: int = ..., channels: str = ..., axis_lock: str = ...) -> Set[str]:
    """Make the current pose more similar to, or further away from, the rest pose"""
    ...

def breakdown(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., prev_frame: int = ..., next_frame: int = ..., channels: str = ..., axis_lock: str = ...) -> Set[str]:
    """Create a suitable breakdown pose on the current frame"""
    ...

def constraint_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a constraint to the active bone"""
    ...

def constraint_add_with_targets(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones"""
    ...

def constraints_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear all constraints from the selected bones"""
    ...

def constraints_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy constraints to other selected bones"""
    ...

def copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the current pose of the selected bones to the internal clipboard"""
    ...

def flip_names(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, do_strip_numbers: bool = ...) -> Set[str]:
    """Flips (and corrects) the axis suffixes of the names of selected bones"""
    ...

def hide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> Set[str]:
    """Tag selected bones to not be visible in Pose Mode"""
    ...

def ik_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, with_targets: bool = ...) -> Set[str]:
    """Add an IK Constraint to the active Bone. The target can be a selected bone or object"""
    ...

def ik_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove all IK Constraints from selected bones"""
    ...

def loc_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset locations of selected bones to their default values"""
    ...

def paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, flipped: bool = ..., selected_mask: bool = ...) -> Set[str]:
    """Paste the stored pose on to the current pose"""
    ...

def paths_calculate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, display_type: str = ..., range: str = ..., bake_location: str = ...) -> Set[str]:
    """Calculate paths for the selected bones"""
    ...

def paths_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_selected: bool = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def paths_range_update(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Update frame range for motion paths from the Scene's current frame range"""
    ...

def paths_update(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Recalculate paths for bones that already have them"""
    ...

def propagate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., end_frame: float = ...) -> Set[str]:
    """Copy selected aspects of the current pose to subsequent poses already keyframed"""
    ...

def push(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., prev_frame: int = ..., next_frame: int = ..., channels: str = ..., axis_lock: str = ...) -> Set[str]:
    """Exaggerate the current pose in regards to the breakdown pose"""
    ...

def quaternions_flip(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Flip quaternion values to achieve desired rotations, while maintaining the same orientations"""
    ...

def relax(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., prev_frame: int = ..., next_frame: int = ..., channels: str = ..., axis_lock: str = ...) -> Set[str]:
    """Make the current pose more similar to its breakdown pose"""
    ...

def reveal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> Set[str]:
    """Reveal all bones hidden in Pose Mode"""
    ...

def rot_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset rotations of selected bones to their default values"""
    ...

def rotation_mode_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set the rotation representation used by selected bones"""
    ...

def scale_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset scaling of selected bones to their default values"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Toggle selection status of all bones"""
    ...

def select_constraint_target(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select bones used as targets for the currently selected bones"""
    ...

def select_grouped(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> Set[str]:
    """Select all visible bones grouped by similar properties"""
    ...

def select_hierarchy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., extend: bool = ...) -> Set[str]:
    """Select immediate parent/children of selected bones"""
    ...

def select_linked(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select all bones linked by parent/child connections to the current selection"""
    ...

def select_linked_pick(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> Set[str]:
    """Select bones linked by parent/child connections under the mouse cursor"""
    ...

def select_mirror(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_active: bool = ..., extend: bool = ...) -> Set[str]:
    """Mirror the bone selection"""
    ...

def select_parent(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select bones that are parents of the currently selected bones"""
    ...

def selection_set_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new empty Selection Set"""
    ...

def selection_set_add_and_assign(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new Selection Set with the currently selected bones"""
    ...

def selection_set_assign(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add selected bones to Selection Set"""
    ...

def selection_set_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the selected Selection Set(s) to the clipboard"""
    ...

def selection_set_delete_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove all Selection Sets from this Armature"""
    ...

def selection_set_deselect(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove Selection Set bones from current selection"""
    ...

def selection_set_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Move the active Selection Set up/down the list of sets"""
    ...

def selection_set_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new Selection Set(s) from the clipboard"""
    ...

def selection_set_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove a Selection Set from this Armature"""
    ...

def selection_set_remove_bones(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the selected bones from all Selection Sets"""
    ...

def selection_set_select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, selection_set_index: int = ...) -> Set[str]:
    """Select the bones from this Selection Set"""
    ...

def selection_set_unassign(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove selected bones from Selection Set"""
    ...

def transforms_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset location, rotation, and scaling of selected bones to their default values"""
    ...

def user_transforms_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_selected: bool = ...) -> Set[str]:
    """Reset pose bone transforms to keyframed state"""
    ...

def visual_transform_apply(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Apply final constrained position of pose bones to their transform"""
    ...
