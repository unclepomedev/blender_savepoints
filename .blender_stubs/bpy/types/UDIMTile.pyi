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

    label: Annotated[str, "is_animatable=False"]
    """Tile label"""
    number: Annotated[int, "step=1"]
    """Number of the position that this tile covers"""
    @property
    def size(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Width and height of the tile buffer in pixels, zero when image data cannot be loaded"""
        ...
    @property
    def channels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of channels in the tile pixels buffer"""
        ...
    generated_type: Annotated[Literal['BLANK', 'UV_GRID', 'COLOR_GRID'], "is_animatable=False"]
    """Generated image type"""
    generated_width: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Generated image width"""
    generated_height: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Generated image height"""
    use_generated_float: Annotated[bool, "is_animatable=False"]
    """Generate floating-point buffer"""
    @property
    def is_generated_tile(self) -> bool:
        """Is this image tile generated"""
        ...
    generated_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Fill color for the generated image"""