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

    drawing: Annotated[Optional['GreasePencilDrawing'], "is_animatable=False"]
    """A Grease Pencil drawing"""
    @property
    def frame_number(self) -> Annotated[int, "step=1"]:
        """The frame number in the scene"""
        ...
    select: bool
    """Frame Selection in the Dope Sheet"""
    keyframe_type: Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]
    """Type of keyframe"""