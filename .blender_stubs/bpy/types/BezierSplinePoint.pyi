# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BezierSplinePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class BezierSplinePoint(bpy_struct):

    select_left_handle: bool
    """Handle 1 selection status"""
    select_right_handle: bool
    """Handle 2 selection status"""
    select_control_point: bool
    """Control point selection status"""
    hide: bool
    """Visibility status"""
    handle_left_type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
    """Handle types"""
    handle_right_type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
    """Handle types"""
    handle_left: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Coordinates of the first handle"""
    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Coordinates of the control point"""
    handle_right: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Coordinates of the second handle"""
    tilt: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Tilt in 3D View"""
    weight_softbody: Annotated[float, "step=10.0", "precision=3"]
    """Softbody goal weight"""
    radius: Annotated[float, "step=10.0", "precision=3"]
    """Radius for beveling"""