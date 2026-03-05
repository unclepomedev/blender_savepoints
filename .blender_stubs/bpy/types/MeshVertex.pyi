# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshVertex.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .VertexGroupElement import VertexGroupElement
from .bpy_prop_collection import bpy_prop_collection

class MeshVertex(bpy_struct):

    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def normal(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Vertex Normal"""
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
    def groups(self) -> Annotated[bpy_prop_collection['VertexGroupElement'], "is_animatable=False"]:
        """Weights for the vertex groups this vertex is member of"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this vertex"""
        ...
    @property
    def undeformed_co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """For meshes with modifiers applied, the coordinate of the vertex with no deforming modifiers applied, as used for generated texture coordinates"""
        ...