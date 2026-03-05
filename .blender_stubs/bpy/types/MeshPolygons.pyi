# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshPolygons.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MeshPolygon import MeshPolygon

class MeshPolygons(bpy_struct):

    @property
    def active(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The active face for this mesh"""
        ...
    @active.setter
    def active(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    def add(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MeshPolygon']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MeshPolygon': ...
    def __len__(self) -> int: ...