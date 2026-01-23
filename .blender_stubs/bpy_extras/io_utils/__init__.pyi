"""
Online Documentation:
https://docs.blender.org/api/current/bpy_extras.io_utils.html
"""

# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

def BoolProperty(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def EnumProperty(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

class ExportHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def check(self, _context) -> Any: ...
    def invoke(self, context, _event) -> Any: ...

class ImportHelper:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    def check(self, _context) -> Any: ...
    def invoke(self, context, _event) -> Any: ...
    def invoke_popup(self, context, confirm_text='') -> Any: ...

def StringProperty(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def axis_conversion_ensure(operator, forward_attr, up_attr) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def create_derived_objects(depsgraph, objects) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def data_(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

i18n_contexts: Any
def iface_(*args, **kwargs) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def orientation_helper(axis_forward='Y', axis_up='Z') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def path_reference_copy(copy_set, report=<built-in function print>) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

path_reference_mode: Any
def poll_file_object_drop(context) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.') -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def unpack_face_list(list_of_tuples) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...

def unpack_list(list_of_tuples) -> Any:
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy_extras.io_utils.html
    """
    ...
