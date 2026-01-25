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
class StripTransform(bpy_struct):
    scale_x: float
    scale_y: float
    offset_x: float
    offset_y: float
    rotation: float
    origin: list[float]
    filter: str