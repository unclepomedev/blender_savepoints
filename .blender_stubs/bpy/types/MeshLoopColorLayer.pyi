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
from .MeshLoopColor import MeshLoopColor
class MeshLoopColorLayer(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name of Vertex color layer"""
    active: Annotated[bool, "is_animatable=False"]
    """Sets the layer as active for display and editing"""
    active_render: Annotated[bool, "is_animatable=False"]
    """Sets the layer as active for rendering"""
    @property
    def data(self) -> Annotated[bpy_prop_collection['MeshLoopColor'], "is_animatable=False"]:
        ...