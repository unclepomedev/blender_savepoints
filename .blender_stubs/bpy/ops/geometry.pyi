# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def attribute_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., domain: str = ..., data_type: str = ...) -> set[str]:
    """Add attribute to geometry"""
    ...

def attribute_convert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., domain: str = ..., data_type: str = ...) -> set[str]:
    """Change how the attribute is stored"""
    ...

def attribute_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove attribute from geometry"""
    ...

def color_attribute_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., domain: str = ..., data_type: str = ..., color: list[float] = ...) -> set[str]:
    """Add color attribute to geometry"""
    ...

def color_attribute_convert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, domain: str = ..., data_type: str = ...) -> set[str]:
    """Change how the color attribute is stored"""
    ...

def color_attribute_duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate color attribute"""
    ...

def color_attribute_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove color attribute from geometry"""
    ...

def color_attribute_render_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Set default color attribute used for rendering"""
    ...

def execute_node_group(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ..., name: str = ..., session_uid: int = ..., mouse_position: list[int] = ..., region_size: list[int] = ..., cursor_position: list[float] = ..., cursor_rotation: list[float] = ..., viewport_projection_matrix: list[float] = ..., viewport_view_matrix: list[float] = ..., viewport_is_perspective: bool = ...) -> set[str]:
    """Execute a node group on geometry"""
    ...

def geometry_randomization(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: bool = ...) -> set[str]:
    """Toggle geometry randomization for debugging purposes"""
    ...
