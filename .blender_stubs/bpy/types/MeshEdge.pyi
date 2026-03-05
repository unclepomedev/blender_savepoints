# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshEdge.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshEdge(bpy_struct):

    @property
    def vertices(self) -> Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Vertex indices"""
        ...
    @vertices.setter
    def vertices(self, value: Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def hide(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @hide.setter
    def hide(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_seam(self) -> bool:
        """Seam edge for UV unwrapping"""
        ...
    @use_seam.setter
    def use_seam(self, value: bool) -> None:
        ...
    @property
    def use_edge_sharp(self) -> bool:
        """Sharp edge for shading"""
        ...
    @use_edge_sharp.setter
    def use_edge_sharp(self, value: bool) -> None:
        ...
    @property
    def is_loose(self) -> bool:
        """Edge is not connected to any faces"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this edge"""
        ...