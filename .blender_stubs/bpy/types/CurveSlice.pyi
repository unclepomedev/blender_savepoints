# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurveSlice.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurvePoint import CurvePoint
from .bpy_prop_collection import bpy_prop_collection

class CurveSlice(bpy_struct):

    @property
    def points(self) -> Annotated[bpy_prop_collection['CurvePoint'], "is_animatable=False"]:
        """Control points of the curve"""
        ...
    @property
    def first_point_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """The index of this curve's first control point"""
        ...
    @property
    def points_length(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of control points in the curve"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this curve"""
        ...