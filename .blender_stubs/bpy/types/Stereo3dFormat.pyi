# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Stereo3dFormat.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Stereo3dFormat(bpy_struct):

    @property
    def display_mode(self) -> Annotated[Literal['ANAGLYPH', 'INTERLACE', 'SIDEBYSIDE', 'TOPBOTTOM'], "is_animatable=False"]:

        ...
    @display_mode.setter
    def display_mode(self, value: Annotated[Literal['ANAGLYPH', 'INTERLACE', 'SIDEBYSIDE', 'TOPBOTTOM'], "is_animatable=False"]):
        ...
    @property
    def anaglyph_type(self) -> Annotated[Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], "is_animatable=False"]:

        ...
    @anaglyph_type.setter
    def anaglyph_type(self, value: Annotated[Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], "is_animatable=False"]):
        ...
    @property
    def interlace_type(self) -> Annotated[Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], "is_animatable=False"]:

        ...
    @interlace_type.setter
    def interlace_type(self, value: Annotated[Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], "is_animatable=False"]):
        ...
    @property
    def use_interlace_swap(self) -> Annotated[bool, "is_animatable=False"]:
        """Swap left and right stereo channels"""
        ...
    @use_interlace_swap.setter
    def use_interlace_swap(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_sidebyside_crosseyed(self) -> Annotated[bool, "is_animatable=False"]:
        """Right eye should see left image and vice versa"""
        ...
    @use_sidebyside_crosseyed.setter
    def use_sidebyside_crosseyed(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_squeezed_frame(self) -> Annotated[bool, "is_animatable=False"]:
        """Combine both views in a squeezed image"""
        ...
    @use_squeezed_frame.setter
    def use_squeezed_frame(self, value: Annotated[bool, "is_animatable=False"]):
        ...