# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyingSetPaths.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .KeyingSetPath import KeyingSetPath

class KeyingSetPaths(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['KeyingSetPath'], "is_animatable=False"]:
        """Active Keying Set used to insert/delete keyframes"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['KeyingSetPath'], "is_animatable=False"]):
        ...
    @property
    def active_index(self) -> Annotated[int, "step=1"]:
        """Current Keying Set index"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "step=1"]):
        ...
    def add(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['KeyingSetPath']: ...
    def __getitem__(self, key: Union[str, int]) -> 'KeyingSetPath': ...
    def __len__(self) -> int: ...