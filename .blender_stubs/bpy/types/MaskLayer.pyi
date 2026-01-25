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
from .MaskSpline import MaskSpline
class MaskLayer(bpy_struct):
    name: str
    splines: bpy_prop_collection['MaskSpline']
    hide: bool
    hide_select: bool
    hide_render: bool
    select: bool
    alpha: float
    blend: str
    invert: bool
    falloff: str
    use_fill_holes: bool
    use_fill_overlap: bool