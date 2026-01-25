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
class MeshLoop(bpy_struct):
    vertex_index: int
    edge_index: int
    index: int
    normal: list[float]
    tangent: list[float]
    bitangent_sign: float
    bitangent: list[float]