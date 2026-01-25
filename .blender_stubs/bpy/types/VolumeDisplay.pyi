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
class VolumeDisplay(bpy_struct):
    density: float
    wireframe_type: str
    wireframe_detail: str
    interpolation_method: str
    use_slice: bool
    slice_axis: str
    slice_depth: float