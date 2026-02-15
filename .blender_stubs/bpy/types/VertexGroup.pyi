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
class VertexGroup(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Vertex group name"""
    lock_weight: Annotated[bool, "is_animatable=False"]
    """Maintain the relative weights for the group"""
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Index number of the vertex group"""
        ...
    def add(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def weight(self, *args, **kwargs) -> Any: ...