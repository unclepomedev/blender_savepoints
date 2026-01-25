# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_point(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[int] = ...) -> set[str]:
    """Add New Paint Curve Point"""
    ...

def add_point_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, PAINTCURVE_OT_add_point: 'PAINTCURVE_OT_add_point' = ..., PAINTCURVE_OT_slide: 'PAINTCURVE_OT_slide' = ...) -> set[str]:
    """Add new curve point and slide it"""
    ...

def cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Place cursor"""
    ...

def delete_point(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove Paint Curve Point"""
    ...

def draw(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Draw curve"""
    ...

def new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add new paint curve"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[int] = ..., toggle: bool = ..., extend: bool = ...) -> set[str]:
    """Select a paint curve point"""
    ...

def slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: bool = ..., select: bool = ...) -> set[str]:
    """Select and slide paint curve point"""
    ...
