# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VertexGroups.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .VertexGroup import VertexGroup

class VertexGroups(bpy_struct):

    active: Annotated[Optional['VertexGroup'], "is_animatable=False"]
    """Vertex groups of the object"""
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Active index in vertex group array"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['VertexGroup']: ...
    def __getitem__(self, key: Union[str, int]) -> 'VertexGroup': ...
    def __len__(self) -> int: ...