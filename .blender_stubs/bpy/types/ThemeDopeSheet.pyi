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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeDopeSheet(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: float
    keyframe_border: float
    keyframe_border_selected: float
    keyframe_scale_factor: float
    summary: float
    interpolation_line: float
    simulated_frames: float