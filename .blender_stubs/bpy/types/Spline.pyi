# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .BezierSplinePoint import BezierSplinePoint
from .SplinePoint import SplinePoint
class Spline(bpy_struct):
    points: bpy_prop_collection['SplinePoint']
    bezier_points: bpy_prop_collection['BezierSplinePoint']
    tilt_interpolation: str
    radius_interpolation: str
    type: str
    point_count_u: int
    point_count_v: int
    order_u: int
    order_v: int
    resolution_u: int
    resolution_v: int
    use_cyclic_u: bool
    use_cyclic_v: bool
    use_endpoint_u: bool
    use_endpoint_v: bool
    use_bezier_u: bool
    use_bezier_v: bool
    use_smooth: bool
    hide: bool
    material_index: int
    character_index: int
    def calc_length(self, *args, **kwargs) -> Any: ...
    def valid_message(self, *args, **kwargs) -> Any: ...