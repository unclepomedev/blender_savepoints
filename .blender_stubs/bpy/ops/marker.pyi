# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new time marker"""
    ...

def camera_bind(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Bind the selected camera to a marker on the current frame"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Delete selected time marker(s)"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frames: int = ...) -> set[str]:
    """Duplicate selected time marker(s)"""
    ...

def make_links_scene(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, scene: str = ...) -> set[str]:
    """Copy selected markers to another scene"""
    ...

def move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frames: int = ..., tweak: bool = ...) -> set[str]:
    """Move selected time marker(s)"""
    ...

def rename(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Rename first selected time marker"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., camera: bool = ...) -> set[str]:
    """Select time marker(s)"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all time markers"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ..., tweak: bool = ...) -> set[str]:
    """Select all time markers using box selection"""
    ...

def select_leftright(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., extend: bool = ...) -> set[str]:
    """Select markers on and left/right of the current frame"""
    ...
