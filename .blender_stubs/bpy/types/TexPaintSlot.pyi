# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TexPaintSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TexPaintSlot(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the slot"""
        ...
    @property
    def icon_value(self) -> Annotated[int, "step=1"]:
        """Paint slot icon"""
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """Name of UV map"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """Slot has a valid image and UV map"""
        ...