# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def edge_pan(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, inside_padding: float = ..., outside_padding: float = ..., speed_ramp: float = ..., max_speed: float = ..., delay: float = ..., zoom_influence: float = ...) -> Set[str]:
    """Pan the view when the mouse is held at an edge"""
    ...

def ndof(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Use a 3D mouse device to pan/zoom the view"""
    ...

def pan(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: int = ..., deltay: int = ...) -> Set[str]:
    """Pan the view"""
    ...

def reset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset the view"""
    ...

def scroll_down(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: int = ..., deltay: int = ..., page: bool = ...) -> Set[str]:
    """Scroll the view down"""
    ...

def scroll_left(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: int = ..., deltay: int = ...) -> Set[str]:
    """Scroll the view left"""
    ...

def scroll_right(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: int = ..., deltay: int = ...) -> Set[str]:
    """Scroll the view right"""
    ...

def scroll_up(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: int = ..., deltay: int = ..., page: bool = ...) -> Set[str]:
    """Scroll the view up"""
    ...

def scroller_activate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Scroll view by mouse click and drag"""
    ...

def smoothview(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def zoom(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deltax: float = ..., deltay: float = ..., use_cursor_init: bool = ...) -> Set[str]:
    """Zoom in/out the view"""
    ...

def zoom_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., zoom_out: bool = ...) -> Set[str]:
    """Zoom in the view to the nearest item contained in the border"""
    ...

def zoom_in(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, zoomfacx: float = ..., zoomfacy: float = ...) -> Set[str]:
    """Zoom in the view"""
    ...

def zoom_out(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, zoomfacx: float = ..., zoomfacy: float = ...) -> Set[str]:
    """Zoom out the view"""
    ...
