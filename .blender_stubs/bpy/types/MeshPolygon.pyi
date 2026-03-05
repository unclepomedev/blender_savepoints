# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshPolygon.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshPolygon(bpy_struct):

    @property
    def vertices(self) -> Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Vertex indices"""
        ...
    @vertices.setter
    def vertices(self, value: Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def loop_start(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Index of the first loop of this face"""
        ...
    @loop_start.setter
    def loop_start(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def loop_total(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of loops used by this face"""
        ...
    @property
    def material_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Material slot index of this face"""
        ...
    @material_index.setter
    def material_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def hide(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @hide.setter
    def hide(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_smooth(self) -> bool:

        ...
    @use_smooth.setter
    def use_smooth(self, value: bool):
        ...
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