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
class RaytraceEEVEE(bpy_struct):
    resolution_scale: str
    use_denoise: bool
    denoise_spatial: bool
    denoise_temporal: bool
    denoise_bilateral: bool
    screen_trace_thickness: float
    trace_max_roughness: float
    screen_trace_quality: float