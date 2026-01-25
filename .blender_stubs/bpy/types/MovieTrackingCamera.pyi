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
class MovieTrackingCamera(bpy_struct):
    distortion_model: str
    sensor_width: float
    focal_length: float
    focal_length_pixels: float
    units: str
    principal_point: list[float]
    principal_point_pixels: list[float]
    k1: float
    k2: float
    k3: float
    division_k1: float
    division_k2: float
    nuke_k1: float
    nuke_k2: float
    brown_k1: float
    brown_k2: float
    brown_k3: float
    brown_k4: float
    brown_p1: float
    brown_p2: float
    pixel_aspect: float