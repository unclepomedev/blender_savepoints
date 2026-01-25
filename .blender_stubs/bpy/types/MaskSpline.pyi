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
from .MaskSplinePoint import MaskSplinePoint
class MaskSpline(bpy_struct):
    offset_mode: str
    weight_interpolation: str
    use_cyclic: bool
    use_fill: bool
    use_self_intersection_check: bool
    points: bpy_prop_collection['MaskSplinePoint']