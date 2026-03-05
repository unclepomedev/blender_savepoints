# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShapeKey.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ShapeKeyPoint import ShapeKeyPoint
from .UnknownType import UnknownType
from .bpy_prop_collection import bpy_prop_collection

class ShapeKey(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of Shape Key"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def frame(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Frame for absolute keys"""
        ...
    @property
    def value(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Value of shape key at the current frame"""
        ...
    @value.setter
    def value(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def interpolation(self) -> Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']:
        """Interpolation type for absolute shape keys"""
        ...
    @interpolation.setter
    def interpolation(self, value: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']) -> None:
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex weight group, to blend with basis shape"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def relative_key(self) -> Annotated['ShapeKey', "is_animatable=False"]:
        """Shape used as a relative key"""
        ...
    @relative_key.setter
    def relative_key(self, value: Annotated['ShapeKey', "is_animatable=False"]) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Toggle this shape key"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def lock_shape(self) -> bool:
        """Protect the shape key from accidental sculpting and editing"""
        ...
    @lock_shape.setter
    def lock_shape(self, value: bool) -> None:
        ...
    @property
    def slider_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum for slider"""
        ...
    @slider_min.setter
    def slider_min(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def slider_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum for slider"""
        ...
    @slider_max.setter
    def slider_max(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
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