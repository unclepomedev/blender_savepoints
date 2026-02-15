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
class MeshPolygon(bpy_struct):
    vertices: Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Vertex indices"""
    loop_start: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Index of the first loop of this face"""
    @property
    def loop_total(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of loops used by this face"""
        ...
    material_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Material slot index of this face"""
    select: Annotated[bool, "is_animatable=False"]
    hide: Annotated[bool, "is_animatable=False"]
    use_smooth: bool
    @property
    def normal(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Local space unit length normal vector for this face"""
        ...
    @property
    def center(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Center of this face"""
        ...
    @property
    def area(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Read only area of this face"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this face"""
        ...
    def flip(self, *args, **kwargs) -> Any: ...