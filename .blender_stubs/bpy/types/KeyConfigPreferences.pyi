# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyConfigPreferences.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class KeyConfigPreferences(bpy_struct):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...