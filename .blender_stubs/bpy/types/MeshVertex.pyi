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
from .VertexGroupElement import VertexGroupElement
class MeshVertex(bpy_struct):
    co: float
    normal: float
    select: bool
    hide: bool
    groups: bpy_prop_collection['VertexGroupElement']
    index: int
    undeformed_co: float