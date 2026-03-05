# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Spline.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BezierSplinePoint import BezierSplinePoint
from .SplineBezierPoints import SplineBezierPoints
from .SplinePoint import SplinePoint
from .SplinePoints import SplinePoints
from .bpy_prop_collection import bpy_prop_collection

class Spline(bpy_struct):

    @property
    def points(self) -> Annotated['SplinePoints', "is_animatable=False"]:
        """Collection of points that make up this poly or nurbs spline"""
        ...
    @property
    def bezier_points(self) -> Annotated['SplineBezierPoints', "is_animatable=False"]:
        """Collection of points for Bézier curves only"""
        ...
    @property
    def tilt_interpolation(self) -> Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']:
        """The type of tilt interpolation for 3D, Bézier curves"""
        ...
    @tilt_interpolation.setter
    def tilt_interpolation(self, value: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']):
        ...
    @property
    def radius_interpolation(self) -> Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']:
        """The type of radius interpolation for Bézier curves"""
        ...
    @radius_interpolation.setter
    def radius_interpolation(self, value: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']):
        ...
    @property
    def type(self) -> Literal['POLY', 'BEZIER', 'NURBS']:
        """The interpolation type for this curve element"""
        ...
    @type.setter
    def type(self, value: Literal['POLY', 'BEZIER', 'NURBS']):
        ...
    @property
    def point_count_u(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Total number points for the curve or surface in the U direction"""
        ...
    @property
    def point_count_v(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Total number points for the surface on the V direction"""
        ...
    @property
    def order_u(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """NURBS order in the U direction. Higher values make each point influence a greater area, but have worse performance."""
        ...
    @order_u.setter
    def order_u(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def order_v(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """NURBS order in the V direction. Higher values make each point influence a greater area, but have worse performance."""
        ...
    @order_v.setter
    def order_v(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def resolution_u(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Curve or Surface subdivisions per segment"""
        ...
    @resolution_u.setter
    def resolution_u(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def resolution_v(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Surface subdivisions per segment"""
        ...
    @resolution_v.setter
    def resolution_v(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_cyclic_u(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this curve or surface a closed loop in the U direction"""
        ...
    @use_cyclic_u.setter
    def use_cyclic_u(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_cyclic_v(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this surface a closed loop in the V direction"""
        ...
    @use_cyclic_v.setter
    def use_cyclic_v(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_endpoint_u(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this nurbs curve or surface meet the endpoints in the U direction"""
        ...
    @use_endpoint_u.setter
    def use_endpoint_u(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_endpoint_v(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this nurbs surface meet the endpoints in the V direction"""
        ...
    @use_endpoint_v.setter
    def use_endpoint_v(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_bezier_u(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this nurbs curve or surface act like a Bézier spline in the U direction"""
        ...
    @use_bezier_u.setter
    def use_bezier_u(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_bezier_v(self) -> Annotated[bool, "is_animatable=False"]:
        """Make this nurbs surface act like a Bézier spline in the V direction"""
        ...
    @use_bezier_v.setter
    def use_bezier_v(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_smooth(self) -> bool:
        """Smooth the normals of the surface or beveled curve"""
        ...
    @use_smooth.setter
    def use_smooth(self, value: bool):
        ...
    @property
    def hide(self) -> bool:
        """Hide this curve in Edit mode"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def material_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Material slot index of this curve"""
        ...
    @material_index.setter
    def material_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def character_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Location of this character in the text data (only for text curves)"""
        ...
    def calc_length(self, *args, **kwargs) -> Any: ...
    def valid_message(self, *args, **kwargs) -> Any: ...