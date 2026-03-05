# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UDIMTile.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UDIMTile(bpy_struct):

    @property
    def label(self) -> Annotated[str, "is_animatable=False"]:
        """Tile label"""
        ...
    @label.setter
    def label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def number(self) -> Annotated[int, "step=1"]:
        """Number of the position that this tile covers"""
        ...
    @number.setter
    def number(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def size(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Width and height of the tile buffer in pixels, zero when image data cannot be loaded"""
        ...
    @property
    def channels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of channels in the tile pixels buffer"""
        ...
    @property
    def generated_type(self) -> Annotated[Literal['BLANK', 'UV_GRID', 'COLOR_GRID'], "is_animatable=False"]:
        """Generated image type"""
        ...
    @generated_type.setter
    def generated_type(self, value: Annotated[Literal['BLANK', 'UV_GRID', 'COLOR_GRID'], "is_animatable=False"]):
        ...
    @property
    def generated_width(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Generated image width"""
        ...
    @generated_width.setter
    def generated_width(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def generated_height(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Generated image height"""
        ...
    @generated_height.setter
    def generated_height(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_generated_float(self) -> Annotated[bool, "is_animatable=False"]:
        """Generate floating-point buffer"""
        ...
    @use_generated_float.setter
    def use_generated_float(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_generated_tile(self) -> bool:
        """Is this image tile generated"""
        ...
    @property
    def generated_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Fill color for the generated image"""
        ...
    @generated_color.setter
    def generated_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...