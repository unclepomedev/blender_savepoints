# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PointCaches.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .PointCacheItem import PointCacheItem

class PointCaches(bpy_struct):

    @property
    def active_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['PointCacheItem']: ...
    def __getitem__(self, key: Union[str, int]) -> 'PointCacheItem': ...
    def __len__(self) -> int: ...