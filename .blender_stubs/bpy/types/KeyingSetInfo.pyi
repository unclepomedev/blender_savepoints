# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyingSetInfo.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class KeyingSetInfo(bpy_struct):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")"""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_description(self) -> Annotated[str, "is_animatable=False"]:
        """A short description of the keying set"""
        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_options(self) -> set[str]:
        """Keying Set options to use when inserting keyframes"""
        ...
    @bl_options.setter
    def bl_options(self, value: set[str]):
        ...
    def poll(self, *args, **kwargs) -> Any: ...
    def iterator(self, *args, **kwargs) -> Any: ...
    def generate(self, *args, **kwargs) -> Any: ...