# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilTimeModifierSegment.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class GreasePencilTimeModifierSegment(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the dash segment"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def segment_start(self) -> Annotated[int, "step=1"]:
        """First frame of the segment"""
        ...
    @segment_start.setter
    def segment_start(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def segment_end(self) -> Annotated[int, "step=1"]:
        """Last frame of the segment"""
        ...
    @segment_end.setter
    def segment_end(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def segment_repeat(self) -> Annotated[int, "step=1"]:
        """Number of cycle repeats"""
        ...
    @segment_repeat.setter
    def segment_repeat(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def segment_mode(self) -> Literal['NORMAL', 'REVERSE', 'PINGPONG']:

        ...
    @segment_mode.setter
    def segment_mode(self, value: Literal['NORMAL', 'REVERSE', 'PINGPONG']) -> None:
        ...