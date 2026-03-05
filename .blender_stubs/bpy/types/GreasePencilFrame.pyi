# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilFrame.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .GreasePencilDrawing import GreasePencilDrawing

class GreasePencilFrame(bpy_struct):

    @property
    def drawing(self) -> Annotated[Optional['GreasePencilDrawing'], "is_animatable=False"]:
        """A Grease Pencil drawing"""
        ...
    @drawing.setter
    def drawing(self, value: Annotated[Optional['GreasePencilDrawing'], "is_animatable=False"]):
        ...
    @property
    def frame_number(self) -> Annotated[int, "step=1"]:
        """The frame number in the scene"""
        ...
    @property
    def select(self) -> bool:
        """Frame Selection in the Dope Sheet"""
        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def keyframe_type(self) -> Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]:
        """Type of keyframe"""
        ...
    @keyframe_type.setter
    def keyframe_type(self, value: Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]):
        ...