# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BrushCurvesSculptSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class BrushCurvesSculptSettings(bpy_struct):

    @property
    def add_amount(self) -> Annotated[int, "step=1"]:
        """Number of curves added by the Add brush"""
        ...
    @add_amount.setter
    def add_amount(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def points_per_curve(self) -> Annotated[int, "step=1"]:
        """Number of control points in a newly added curve"""
        ...
    @points_per_curve.setter
    def points_per_curve(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_uniform_scale(self) -> bool:
        """Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation"""
        ...
    @use_uniform_scale.setter
    def use_uniform_scale(self, value: bool):
        ...
    @property
    def minimum_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Avoid shrinking curves shorter than this length"""
        ...
    @minimum_length.setter
    def minimum_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_length_interpolate(self) -> bool:
        """Use length of the curves in close proximity"""
        ...
    @use_length_interpolate.setter
    def use_length_interpolate(self, value: bool):
        ...
    @property
    def use_radius_interpolate(self) -> bool:
        """Use radius of the curves in close proximity"""
        ...
    @use_radius_interpolate.setter
    def use_radius_interpolate(self, value: bool):
        ...
    @property
    def use_point_count_interpolate(self) -> bool:
        """Use the number of points from the curves in close proximity"""
        ...
    @use_point_count_interpolate.setter
    def use_point_count_interpolate(self, value: bool):
        ...
    @property
    def use_shape_interpolate(self) -> bool:
        """Use shape of the curves in close proximity"""
        ...
    @use_shape_interpolate.setter
    def use_shape_interpolate(self, value: bool):
        ...
    @property
    def curve_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Length of newly added curves when it is not interpolated from other curves"""
        ...
    @curve_length.setter
    def curve_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def minimum_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]:
        """Goal distance between curve roots for the Density brush"""
        ...
    @minimum_distance.setter
    def minimum_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]):
        ...
    @property
    def curve_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]:
        """Radius of newly added curves when it is not interpolated from other curves"""
        ...
    @curve_radius.setter
    def curve_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]):
        ...
    @property
    def density_add_attempts(self) -> Annotated[int, "step=1"]:
        """How many times the Density brush tries to add a new curve"""
        ...
    @density_add_attempts.setter
    def density_add_attempts(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def density_mode(self) -> Literal['AUTO', 'ADD', 'REMOVE']:
        """Determines whether the brush adds or removes curves"""
        ...
    @density_mode.setter
    def density_mode(self, value: Literal['AUTO', 'ADD', 'REMOVE']):
        ...
    @property
    def curve_parameter_falloff(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Falloff that is applied from the tip to the root of each curve"""
        ...