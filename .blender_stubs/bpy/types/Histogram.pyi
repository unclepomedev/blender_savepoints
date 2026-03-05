# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Histogram.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Histogram(bpy_struct):

    @property
    def mode(self) -> Literal['LUMA', 'RGB', 'R', 'G', 'B', 'A']:
        """Channels to display in the histogram"""
        ...
    @mode.setter
    def mode(self, value: Literal['LUMA', 'RGB', 'R', 'G', 'B', 'A']):
        ...
    @property
    def show_line(self) -> bool:
        """Display lines rather than filled shapes"""
        ...
    @show_line.setter
    def show_line(self, value: bool):
        ...