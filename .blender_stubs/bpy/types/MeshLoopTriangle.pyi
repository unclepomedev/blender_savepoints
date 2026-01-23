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
class MeshLoopTriangle(bpy_struct):
    vertices: list[int]
    loops: list[int]
    polygon_index: int
    normal: list[float]
    split_normals: list[float]
    area: float
    index: int
    material_index: int
    use_smooth: bool