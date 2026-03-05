# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectConstraints.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Constraint import Constraint

class ObjectConstraints(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['Constraint'], "is_animatable=False"]:
        """Active Object constraint"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['Constraint'], "is_animatable=False"]):
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Constraint']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Constraint': ...
    def __len__(self) -> int: ...