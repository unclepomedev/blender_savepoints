# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.USDHook.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class USDHook(bpy_struct):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:

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
        """A short description of the USD hook"""
        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]):
        ...