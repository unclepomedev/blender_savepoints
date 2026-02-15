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
class MeshLoop(bpy_struct):
    vertex_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Vertex index"""
    edge_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Edge index"""
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this loop"""
        ...
    @property
    def normal(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """The normal direction of the face corner, taking into account sharp faces, sharp edges, and custom normal data"""
        ...
    @property
    def tangent(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Local space unit length tangent vector of this vertex for this face (must be computed beforehand using calc_tangents)"""
        ...
    @property
    def bitangent_sign(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Sign of the bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent))"""
        ...
    @property
    def bitangent(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, use it only if really needed, slower access than bitangent_sign)"""
        ...