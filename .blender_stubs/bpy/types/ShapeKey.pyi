# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ShapeKeyPoint import ShapeKeyPoint
from .UnknownType import UnknownType
class ShapeKey(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name of Shape Key"""
    @property
    def frame(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Frame for absolute keys"""
        ...
    value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Value of shape key at the current frame"""
    interpolation: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']
    """Interpolation type for absolute shape keys"""
    vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex weight group, to blend with basis shape"""
    relative_key: Annotated['ShapeKey', "is_animatable=False"]
    """Shape used as a relative key"""
    mute: bool
    """Toggle this shape key"""
    lock_shape: bool
    """Protect the shape key from accidental sculpting and editing"""
    slider_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum for slider"""
    slider_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum for slider"""
    @property
    def data(self) -> Annotated[bpy_prop_collection['UnknownType'], "is_animatable=False"]:
        ...
    @property
    def points(self) -> Annotated[bpy_prop_collection['ShapeKeyPoint'], "is_animatable=False"]:
        """Optimized access to shape keys point data, when using foreach_get/foreach_set accessors. Warning: Does not support legacy Curve shape keys."""
        ...
    def normals_vertex_get(self, *args, **kwargs) -> Any: ...
    def normals_polygon_get(self, *args, **kwargs) -> Any: ...
    def normals_split_get(self, *args, **kwargs) -> Any: ...