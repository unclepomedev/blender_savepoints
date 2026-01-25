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
from .MaskParent import MaskParent
from .MaskSplinePointUW import MaskSplinePointUW
class MaskSplinePoint(bpy_struct):
    handle_left: float
    co: float
    handle_right: float
    handle_type: str
    handle_left_type: str
    handle_right_type: str
    weight: float
    select: bool
    select_left_handle: bool
    select_control_point: bool
    select_right_handle: bool
    select_single_handle: bool
    parent: 'MaskParent'
    feather_points: bpy_prop_collection['MaskSplinePointUW']