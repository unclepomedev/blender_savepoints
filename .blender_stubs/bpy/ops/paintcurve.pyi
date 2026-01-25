# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def add_point(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: int = ...) -> Set[str]:
    """Add New Paint Curve Point"""
    ...

def add_point_slide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, PAINTCURVE_OT_add_point: 'PAINTCURVE_OT_add_point' = ..., PAINTCURVE_OT_slide: 'PAINTCURVE_OT_slide' = ...) -> Set[str]:
    """Add new curve point and slide it"""
    ...

def cursor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Place cursor"""
    ...

def delete_point(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove Paint Curve Point"""
    ...

def draw(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Draw curve"""
    ...

def new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new paint curve"""
    ...

def select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: int = ..., toggle: bool = ..., extend: bool = ...) -> Set[str]:
    """Select a paint curve point"""
    ...

def slide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: bool = ..., select: bool = ...) -> Set[str]:
    """Select and slide paint curve point"""
    ...
