# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Nodes.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Node import Node

class Nodes(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        """Active node in this tree"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['Node'], "is_animatable=False"]) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Node']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Node': ...
    def __len__(self) -> int: ...