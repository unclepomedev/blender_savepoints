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
class MetaElement(bpy_struct):
    type: str
    co: float
    rotation: float
    radius: float
    size_x: float
    size_y: float
    size_z: float
    stiffness: float
    use_negative: bool
    use_scale_stiffness: bool
    select: bool
    hide: bool