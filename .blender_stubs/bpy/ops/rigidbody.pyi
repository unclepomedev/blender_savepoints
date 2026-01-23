# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def bake_to_keyframes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame_start: int = ..., frame_end: int = ..., step: int = ...) -> set[str]:
    """Bake rigid body transformations of selected objects to keyframes"""
    ...

def connect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, con_type: str = ..., pivot_type: str = ..., connection_pattern: str = ...) -> set[str]:
    """Create rigid body constraints between selected rigid bodies"""
    ...

def constraint_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add Rigid Body Constraint to active object"""
    ...

def constraint_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove Rigid Body Constraint from Object"""
    ...

def mass_calculate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, material: str = ..., density: float = ...) -> set[str]:
    """Automatically calculate mass values for Rigid Body Objects based on volume"""
    ...

def object_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add active object as Rigid Body"""
    ...

def object_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove Rigid Body settings from Object"""
    ...

def object_settings_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy Rigid Body settings from active object to selected"""
    ...

def objects_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add selected objects as Rigid Bodies"""
    ...

def objects_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove selected objects from Rigid Body simulation"""
    ...

def shape_change(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Change collision shapes for selected Rigid Body Objects"""
    ...

def world_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add Rigid Body simulation world to the current scene"""
    ...

def world_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove Rigid Body simulation world from the current scene"""
    ...
