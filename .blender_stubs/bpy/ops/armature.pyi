# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def align(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Align selected bones to the active bone (or to their parent)"""
    ...

def assign_to_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection_index: int = ..., new_collection_name: str = ...) -> set[str]:
    """Assign all selected bones to a collection, or unassign them, depending on whether the active bone is already assigned or not"""
    ...

def autoside_names(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Automatically renames the selected bones according to which side of the target axis they fall on"""
    ...

def bone_primitive_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Add a new bone located at the 3D cursor"""
    ...

def calculate_roll(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., axis_flip: bool = ..., axis_only: bool = ...) -> set[str]:
    """Automatically fix alignment of select bones' axes"""
    ...

def click_extrude(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create a new bone going from the last selected joint to the mouse position"""
    ...

def collection_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new bone collection"""
    ...

def collection_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Add selected bones to the chosen bone collection"""
    ...

def collection_create_and_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Create a new bone collection and assign all selected bones"""
    ...

def collection_deselect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect bones of active Bone Collection"""
    ...

def collection_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Change position of active Bone Collection in list of Bone collections"""
    ...

def collection_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the active bone collection"""
    ...

def collection_remove_unused(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove all bone collections that have neither bones nor children. This is done recursively, so bone collections that only have unused children are also removed"""
    ...

def collection_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select bones in active Bone Collection"""
    ...

def collection_show_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Show all bone collections"""
    ...

def collection_unassign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Remove selected bones from the active bone collection"""
    ...

def collection_unassign_named(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., bone_name: str = ...) -> set[str]:
    """Unassign the named bone from this bone collection"""
    ...

def collection_unsolo_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the 'solo' setting on all bone collections"""
    ...

def copy_bone_color_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, bone_type: str = ...) -> set[str]:
    """Copy the bone color of the active bone to all selected bones"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Remove selected bones from the armature"""
    ...

def dissolve(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Dissolve selected bones from the armature"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, do_flip_names: bool = ...) -> set[str]:
    """Make copies of the selected bones within the same armature"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ARMATURE_OT_duplicate: 'ARMATURE_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Make copies of the selected bones within the same armature and move them"""
    ...

def extrude(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, forked: bool = ...) -> set[str]:
    """Create new bones from the selected joints"""
    ...

def extrude_forked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ARMATURE_OT_extrude: 'ARMATURE_OT_extrude' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Create new bones from the selected joints and move them"""
    ...

def extrude_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ARMATURE_OT_extrude: 'ARMATURE_OT_extrude' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Create new bones from the selected joints and move them"""
    ...

def fill(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add bone between selected joint(s) and/or 3D cursor"""
    ...

def flip_names(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, do_strip_numbers: bool = ...) -> set[str]:
    """Flips (and corrects) the axis suffixes of the names of selected bones"""
    ...

def hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Tag selected bones to not be visible in Edit Mode"""
    ...

def move_to_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection_index: int = ..., new_collection_name: str = ...) -> set[str]:
    """Move bones to a collection"""
    ...

def parent_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Remove the parent-child relationship between selected bones and their parents"""
    ...

def parent_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set the active bone as the parent of the selected bones"""
    ...

def reveal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal all bones hidden in Edit Mode"""
    ...

def roll_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, roll: float = ...) -> set[str]:
    """Clear roll for selected bones"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Toggle selection status of all bones"""
    ...

def select_hierarchy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., extend: bool = ...) -> set[str]:
    """Select immediate parent/children of selected bones"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect those bones at the boundary of each selection region"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all_forks: bool = ...) -> set[str]:
    """Select all bones linked by parent/child connections to the current selection"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ..., all_forks: bool = ...) -> set[str]:
    """(De)select bones linked by parent/child connections under the mouse cursor"""
    ...

def select_mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_active: bool = ..., extend: bool = ...) -> set[str]:
    """Mirror the bone selection"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select those bones connected to the initial selection"""
    ...

def select_similar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., threshold: float = ...) -> set[str]:
    """Select similar bones by property types"""
    ...

def separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Isolate selected bones into a separate armature"""
    ...

def shortest_path_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select shortest path between two bones"""
    ...

def split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split off selected bones from connected unselected bones"""
    ...

def subdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ...) -> set[str]:
    """Break selected bones into chains of smaller bones"""
    ...

def switch_direction(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Change the direction that a chain of bones points in (head and tail swap)"""
    ...

def symmetrize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., copy_bone_colors: bool = ...) -> set[str]:
    """Enforce symmetry, make copies of the selection or use existing"""
    ...
