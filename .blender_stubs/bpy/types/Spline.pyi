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
from .BezierSplinePoint import BezierSplinePoint
from .SplineBezierPoints import SplineBezierPoints
from .SplinePoint import SplinePoint
from .SplinePoints import SplinePoints
class Spline(bpy_struct):
    @property
    def points(self) -> Annotated['SplinePoints', "is_animatable=False"]:
        """Collection of points that make up this poly or nurbs spline"""
        ...
    @property
    def bezier_points(self) -> Annotated['SplineBezierPoints', "is_animatable=False"]:
        """Collection of points for Bézier curves only"""
        ...
    tilt_interpolation: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']
    """The type of tilt interpolation for 3D, Bézier curves"""
    radius_interpolation: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']
    """The type of radius interpolation for Bézier curves"""
    type: Literal['POLY', 'BEZIER', 'NURBS']
    """The interpolation type for this curve element"""
    @property
    def point_count_u(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Total number points for the curve or surface in the U direction"""
        ...
    @property
    def point_count_v(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Total number points for the surface on the V direction"""
        ...
    order_u: Annotated[int, "step=1", "is_animatable=False"]
    """NURBS order in the U direction. Higher values make each point influence a greater area, but have worse performance."""
    order_v: Annotated[int, "step=1", "is_animatable=False"]
    """NURBS order in the V direction. Higher values make each point influence a greater area, but have worse performance."""
    resolution_u: Annotated[int, "step=1", "is_animatable=False"]
    """Curve or Surface subdivisions per segment"""
    resolution_v: Annotated[int, "step=1", "is_animatable=False"]
    """Surface subdivisions per segment"""
    use_cyclic_u: Annotated[bool, "is_animatable=False"]
    """Make this curve or surface a closed loop in the U direction"""
    use_cyclic_v: Annotated[bool, "is_animatable=False"]
    """Make this surface a closed loop in the V direction"""
    use_endpoint_u: Annotated[bool, "is_animatable=False"]
    """Make this nurbs curve or surface meet the endpoints in the U direction"""
    use_endpoint_v: Annotated[bool, "is_animatable=False"]
    """Make this nurbs surface meet the endpoints in the V direction"""
    use_bezier_u: Annotated[bool, "is_animatable=False"]
    """Make this nurbs curve or surface act like a Bézier spline in the U direction"""
    use_bezier_v: Annotated[bool, "is_animatable=False"]
    """Make this nurbs surface act like a Bézier spline in the V direction"""
    use_smooth: bool
    """Smooth the normals of the surface or beveled curve"""
    hide: bool
    """Hide this curve in Edit mode"""
    material_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Material slot index of this curve"""
    @property
    def character_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Location of this character in the text data (only for text curves)"""
        ...
    def calc_length(self, *args, **kwargs) -> Any: ...
    def valid_message(self, *args, **kwargs) -> Any: ...