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
class MovieTrackingMarker(bpy_struct):
    co: float
    frame: int
    mute: bool
    pattern_corners: float
    pattern_bound_box: float
    search_min: float
    search_max: float
    is_keyed: bool