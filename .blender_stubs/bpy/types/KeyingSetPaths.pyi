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

    active: Annotated[Optional['KeyingSetPath'], "is_animatable=False"]
    """Active Keying Set used to insert/delete keyframes"""
    active_index: Annotated[int, "step=1"]
    """Current Keying Set index"""
    def add(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['KeyingSetPath']: ...
    def __getitem__(self, key: Union[str, int]) -> 'KeyingSetPath': ...
    def __len__(self) -> int: ...