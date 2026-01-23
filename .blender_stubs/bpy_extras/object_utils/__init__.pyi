"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.object_utils.html
"""

# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class AddObjectHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def align_update_callback(self, _context) -> Any: ...
    def poll(context) -> Any: ...

def EnumProperty(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def FloatVectorProperty(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def add_object_align_init(context, operator) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

annotations: Any
def object_add_grid_scale(context) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def object_add_grid_scale_apply_operator(operator, context) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def object_data_add(context, obdata, operator=None, name=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def object_report_if_active_shape_key_is_locked(obj, operator) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...

def world_to_camera_view(scene, obj, coord) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.object_utils.html
    """
    ...
