# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskSpline.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MaskSplinePoint import MaskSplinePoint
from .MaskSplinePoints import MaskSplinePoints
from .bpy_prop_collection import bpy_prop_collection

class MaskSpline(bpy_struct):

    @property
    def offset_mode(self) -> Literal['EVEN', 'SMOOTH']:
        """The method used for calculating the feather offset"""
        ...
    @offset_mode.setter
    def offset_mode(self, value: Literal['EVEN', 'SMOOTH']):
        ...
    @property
    def weight_interpolation(self) -> Literal['LINEAR', 'EASE']:
        """The type of weight interpolation for spline"""
        ...
    @weight_interpolation.setter
    def weight_interpolation(self, value: Literal['LINEAR', 'EASE']):
        ...
    @property
    def use_cyclic(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this spline a closed loop"""
        ...
    @use_cyclic.setter
    def use_cyclic(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_fill(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this spline filled"""
        ...
    @use_fill.setter
    def use_fill(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_self_intersection_check(self) -> Annotated[bool, "is_animatable=False"]:
        """Prevent feather from self-intersections"""
        ...
    @use_self_intersection_check.setter
    def use_self_intersection_check(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def points(self) -> Annotated['MaskSplinePoints', "is_animatable=False"]:
        """Collection of points"""
        ...