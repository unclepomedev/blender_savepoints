# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshSkinVertexLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MeshSkinVertex import MeshSkinVertex
from .bpy_prop_collection import bpy_prop_collection

class MeshSkinVertexLayer(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of skin layer"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def data(self) -> Annotated[bpy_prop_collection['MeshSkinVertex'], "is_animatable=False"]:

        ...