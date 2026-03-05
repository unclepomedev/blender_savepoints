# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripCrop.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StripCrop(bpy_struct):

    @property
    def max_y(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to crop from the top"""
        ...
    @max_y.setter
    def max_y(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def min_y(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to crop from the bottom"""
        ...
    @min_y.setter
    def min_y(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def min_x(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to crop from the left side"""
        ...
    @min_x.setter
    def min_x(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def max_x(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Number of pixels to crop from the right side"""
        ...
    @max_x.setter
    def max_x(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...