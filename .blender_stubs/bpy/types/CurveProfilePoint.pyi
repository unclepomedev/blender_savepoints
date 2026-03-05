# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurveProfilePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class CurveProfilePoint(bpy_struct):

    @property
    def location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """X/Y coordinates of the path point"""
        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def handle_type_1(self) -> Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']:
        """Path interpolation at this point"""
        ...
    @handle_type_1.setter
    def handle_type_1(self, value: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']) -> None:
        ...
    @property
    def handle_type_2(self) -> Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']:
        """Path interpolation at this point"""
        ...
    @handle_type_2.setter
    def handle_type_2(self, value: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']) -> None:
        ...
    @property
    def select(self) -> bool:
        """Selection state of the path point"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...