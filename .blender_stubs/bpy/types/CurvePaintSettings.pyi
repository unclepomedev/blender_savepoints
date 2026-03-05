# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurvePaintSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class CurvePaintSettings(bpy_struct):

    @property
    def curve_type(self) -> Annotated[Literal['POLY', 'BEZIER'], "is_animatable=False"]:
        """Type of curve to use for new strokes"""
        ...
    @curve_type.setter
    def curve_type(self, value: Annotated[Literal['POLY', 'BEZIER'], "is_animatable=False"]):
        ...
    @property
    def use_corners_detect(self) -> Annotated[bool, "is_animatable=False"]:
        """Detect corners and use non-aligned handles"""
        ...
    @use_corners_detect.setter
    def use_corners_detect(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pressure_radius(self) -> Annotated[bool, "is_animatable=False"]:
        """Map tablet pressure to curve radius"""
        ...
    @use_pressure_radius.setter
    def use_pressure_radius(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_endpoints(self) -> Annotated[bool, "is_animatable=False"]:
        """Use the start of the stroke for the depth"""
        ...
    @use_stroke_endpoints.setter
    def use_stroke_endpoints(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_offset_absolute(self) -> Annotated[bool, "is_animatable=False"]:
        """Apply a fixed offset (don't scale by the radius)"""
        ...
    @use_offset_absolute.setter
    def use_offset_absolute(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_project_only_selected(self) -> Annotated[bool, "is_animatable=False"]:
        """Project the strokes only onto selected objects"""
        ...
    @use_project_only_selected.setter
    def use_project_only_selected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def error_threshold(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Allow deviation for a smoother, less precise line"""
        ...
    @error_threshold.setter
    def error_threshold(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def fit_method(self) -> Annotated[Literal['REFIT', 'SPLIT'], "subtype='PIXEL'", "is_animatable=False"]:
        """Curve fitting method"""
        ...
    @fit_method.setter
    def fit_method(self, value: Annotated[Literal['REFIT', 'SPLIT'], "subtype='PIXEL'", "is_animatable=False"]):
        ...
    @property
    def corner_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Angles above this are considered corners"""
        ...
    @corner_angle.setter
    def corner_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def radius_min(self) -> Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]:
        """Minimum radius when the minimum pressure is applied (also the minimum when tapering)"""
        ...
    @radius_min.setter
    def radius_min(self, value: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def radius_max(self) -> Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]:
        """Radius to use when the maximum pressure is applied (or when a tablet isn't used)"""
        ...
    @radius_max.setter
    def radius_max(self, value: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def radius_taper_start(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Taper factor for the radius of each point along the curve"""
        ...
    @radius_taper_start.setter
    def radius_taper_start(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def radius_taper_end(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Taper factor for the radius of each point along the curve"""
        ...
    @radius_taper_end.setter
    def radius_taper_end(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def surface_offset(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Offset the stroke from the surface"""
        ...
    @surface_offset.setter
    def surface_offset(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def depth_mode(self) -> Annotated[Literal['CURSOR', 'SURFACE'], "is_animatable=False"]:
        """Method of projecting depth"""
        ...
    @depth_mode.setter
    def depth_mode(self, value: Annotated[Literal['CURSOR', 'SURFACE'], "is_animatable=False"]):
        ...
    @property
    def surface_plane(self) -> Annotated[Literal['NORMAL_VIEW', 'NORMAL_SURFACE', 'VIEW'], "is_animatable=False"]:
        """Plane for projected stroke"""
        ...
    @surface_plane.setter
    def surface_plane(self, value: Annotated[Literal['NORMAL_VIEW', 'NORMAL_SURFACE', 'VIEW'], "is_animatable=False"]):
        ...