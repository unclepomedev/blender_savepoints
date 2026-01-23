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
    vertices: int
    loops: int
    polygon_index: int
    normal: float
    split_normals: float
    area: float
    index: int
    material_index: int
    use_smooth: bool