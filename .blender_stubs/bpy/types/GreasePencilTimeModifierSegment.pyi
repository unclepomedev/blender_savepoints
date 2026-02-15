# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class GreasePencilTimeModifierSegment(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name of the dash segment"""
    segment_start: Annotated[int, "step=1"]
    """First frame of the segment"""
    segment_end: Annotated[int, "step=1"]
    """Last frame of the segment"""
    segment_repeat: Annotated[int, "step=1"]
    """Number of cycle repeats"""
    segment_mode: Literal['NORMAL', 'REVERSE', 'PINGPONG']