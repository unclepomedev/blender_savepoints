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
from .ColorRamp import ColorRamp
class ColorMapping(bpy_struct):
    use_color_ramp: bool
    color_ramp: 'ColorRamp'
    brightness: float
    contrast: float
    saturation: float
    blend_type: str
    blend_color: float
    blend_factor: float