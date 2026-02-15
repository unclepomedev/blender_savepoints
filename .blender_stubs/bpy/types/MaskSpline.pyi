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
from .MaskSplinePoint import MaskSplinePoint
from .MaskSplinePoints import MaskSplinePoints
class MaskSpline(bpy_struct):
    offset_mode: Literal['EVEN', 'SMOOTH']
    """The method used for calculating the feather offset"""
    weight_interpolation: Literal['LINEAR', 'EASE']
    """The type of weight interpolation for spline"""
    use_cyclic: Annotated[bool, "is_animatable=False"]
    """Make this spline a closed loop"""
    use_fill: Annotated[bool, "is_animatable=False"]
    """Make this spline filled"""
    use_self_intersection_check: Annotated[bool, "is_animatable=False"]
    """Prevent feather from self-intersections"""
    @property
    def points(self) -> Annotated['MaskSplinePoints', "is_animatable=False"]:
        """Collection of points"""
        ...