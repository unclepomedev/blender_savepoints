# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UVLoopLayers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MeshUVLoopLayer import MeshUVLoopLayer

class UVLoopLayers(bpy_struct):

    active: Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]
    """Active UV Map layer"""
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Active UV map index"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MeshUVLoopLayer']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MeshUVLoopLayer': ...
    def __len__(self) -> int: ...