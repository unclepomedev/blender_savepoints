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
class MeshPolygon(bpy_struct):
    vertices: list[int]
    loop_start: int
    loop_total: int
    material_index: int
    select: bool
    hide: bool
    use_smooth: bool
    normal: list[float]
    center: list[float]
    area: float
    index: int
    def flip(self, *args, **kwargs) -> Any: ...