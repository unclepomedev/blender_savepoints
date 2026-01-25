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
from .Object import Object
class GPencilSculptGuide(bpy_struct):
    use_guide: bool
    use_snapping: bool
    reference_object: 'Object'
    reference_point: str
    type: str
    angle: float
    angle_snap: float
    spacing: float
    location: list[float]