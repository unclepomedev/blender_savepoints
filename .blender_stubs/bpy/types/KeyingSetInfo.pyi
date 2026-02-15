# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class KeyingSetInfo(bpy_struct):
    bl_idname: Annotated[str, "is_animatable=False"]
    """If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")"""
    bl_label: Annotated[str, "is_animatable=False"]
    bl_description: Annotated[str, "is_animatable=False"]
    """A short description of the keying set"""
    bl_options: set[str]
    """Keying Set options to use when inserting keyframes"""
    def poll(self, *args, **kwargs) -> Any: ...
    def iterator(self, *args, **kwargs) -> Any: ...
    def generate(self, *args, **kwargs) -> Any: ...