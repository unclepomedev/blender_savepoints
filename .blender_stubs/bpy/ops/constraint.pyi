# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_target(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a target to the constraint"""
    ...

def apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ..., report: bool = ...) -> set[str]:
    """Apply constraint and remove from the stack"""
    ...

def childof_clear_inverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Clear inverse correction for Child Of constraint"""
    ...

def childof_set_inverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Set inverse correction for Child Of constraint"""
    ...

def copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ..., report: bool = ...) -> set[str]:
    """Duplicate constraint at the same position in the stack"""
    ...

def copy_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Copy constraint to other selected objects/bones"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ..., report: bool = ...) -> set[str]:
    """Remove constraint from constraint stack"""
    ...

def disable_keep_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation"""
    ...

def followpath_path_animate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ..., frame_start: int = ..., length: int = ...) -> set[str]:
    """Add default animation for path used by constraint if it isn't animated already"""
    ...

def limitdistance_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Reset limiting distance for Limit Distance Constraint"""
    ...

def move_down(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Move constraint down in constraint stack"""
    ...

def move_to_index(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ..., index: int = ...) -> set[str]:
    """Change the constraint's position in the list so it evaluates after the set number of others"""
    ...

def move_up(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Move constraint up in constraint stack"""
    ...

def normalize_target_weights(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Normalize weights of all target bones"""
    ...

def objectsolver_clear_inverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Clear inverse correction for Object Solver constraint"""
    ...

def objectsolver_set_inverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Set inverse correction for Object Solver constraint"""
    ...

def remove_target(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Remove the target from the constraint"""
    ...

def stretchto_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, constraint: str = ..., owner: str = ...) -> set[str]:
    """Reset original length of bone for Stretch To Constraint"""
    ...
