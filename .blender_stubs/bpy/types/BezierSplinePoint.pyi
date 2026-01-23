# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class BezierSplinePoint(bpy_struct):
    select_left_handle: bool
    select_right_handle: bool
    select_control_point: bool
    hide: bool
    handle_left_type: str
    handle_right_type: str
    handle_left: float
    co: float
    handle_right: float
    tilt: float
    weight_softbody: float
    radius: float