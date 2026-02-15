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
class MeshLoopTriangle(bpy_struct):
    @property
    def vertices(self) -> Annotated[list[int], "subtype='UNSIGNED'", "step=1"]:
        """Indices of triangle vertices"""
        ...
    @property
    def loops(self) -> Annotated[list[int], "subtype='UNSIGNED'", "step=1"]:
        """Indices of mesh loops that make up the triangle"""
        ...
    @property
    def polygon_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of mesh face that the triangle is a part of"""
        ...
    @property
    def normal(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Local space unit length normal vector for this triangle"""
        ...
    @property
    def split_normals(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Local space unit length custom normal vectors of the face corners of this triangle"""
        ...
    @property
    def area(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Area of this triangle"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this loop triangle"""
        ...
    @property
    def material_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Material slot index of this triangle"""
        ...
    @property
    def use_smooth(self) -> bool:
        ...