# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Stereo3dDisplay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Stereo3dDisplay(bpy_struct):

    @property
    def display_mode(self) -> Literal['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM']:

        ...
    @display_mode.setter
    def display_mode(self, value: Literal['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM']) -> None:
        ...
    @property
    def anaglyph_type(self) -> Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE']:

        ...
    @anaglyph_type.setter
    def anaglyph_type(self, value: Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE']) -> None:
        ...
    @property
    def interlace_type(self) -> Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED']:

        ...
    @interlace_type.setter
    def interlace_type(self, value: Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED']) -> None:
        ...
    @property
    def use_interlace_swap(self) -> bool:
        """Swap left and right stereo channels"""
        ...
    @use_interlace_swap.setter
    def use_interlace_swap(self, value: bool) -> None:
        ...
    @property
    def use_sidebyside_crosseyed(self) -> bool:
        """Right eye should see left image and vice versa"""
        ...
    @use_sidebyside_crosseyed.setter
    def use_sidebyside_crosseyed(self, value: bool) -> None:
        ...