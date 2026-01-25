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
from .ShapeKeyPoint import ShapeKeyPoint
from .UnknownType import UnknownType
class ShapeKey(bpy_struct):
    name: str
    frame: float
    value: float
    interpolation: str
    vertex_group: str
    relative_key: 'ShapeKey'
    mute: bool
    lock_shape: bool
    slider_min: float
    slider_max: float
    data: bpy_prop_collection['UnknownType']
    points: bpy_prop_collection['ShapeKeyPoint']
    def normals_vertex_get(self, *args, **kwargs) -> Any: ...
    def normals_polygon_get(self, *args, **kwargs) -> Any: ...
    def normals_split_get(self, *args, **kwargs) -> Any: ...