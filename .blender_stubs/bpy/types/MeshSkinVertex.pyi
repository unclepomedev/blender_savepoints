# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshSkinVertex.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshSkinVertex(bpy_struct):

    @property
    def radius(self) -> Annotated[list[float], "subtype='UNSIGNED'", "step=1.0", "precision=3"]:
        """Radius of the skin"""
        ...
    @radius.setter
    def radius(self, value: Annotated[list[float], "subtype='UNSIGNED'", "step=1.0", "precision=3"]):
        ...
    @property
    def use_root(self) -> bool:
        """Vertex is a root for rotation calculations and armature generation, setting this flag does not clear other roots in the same mesh island"""
        ...
    @use_root.setter
    def use_root(self, value: bool):
        ...
    @property
    def use_loose(self) -> bool:
        """If vertex has multiple adjacent edges, it is hulled to them directly"""
        ...
    @use_loose.setter
    def use_loose(self, value: bool):
        ...