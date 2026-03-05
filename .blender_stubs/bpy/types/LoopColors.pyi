# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LoopColors.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MeshLoopColorLayer import MeshLoopColorLayer

class LoopColors(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['MeshLoopColorLayer'], "is_animatable=False"]:
        """Active vertex color layer"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['MeshLoopColorLayer'], "is_animatable=False"]):
        ...
    @property
    def active_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Active vertex color index"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MeshLoopColorLayer']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MeshLoopColorLayer': ...
    def __len__(self) -> int: ...