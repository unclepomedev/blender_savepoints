# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def attribute_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value_float: float = ..., value_float_vector_2d: list[float] = ..., value_float_vector_3d: list[float] = ..., value_int: int = ..., value_int_vector_2d: list[int] = ..., value_color: list[float] = ..., value_bool: bool = ...) -> set[str]:
    """Set values of the active attribute for selected elements"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove selected points"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy selected points"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, POINTCLOUD_OT_duplicate: 'POINTCLOUD_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Make copies of selected elements and move them"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """(De)select all point cloud"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, seed: int = ..., probability: float = ...) -> set[str]:
    """Randomizes existing selection or create new random selection"""
    ...

def separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Separate selected geometry into a new point cloud"""
    ...
