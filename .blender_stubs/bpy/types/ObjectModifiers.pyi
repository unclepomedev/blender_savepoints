# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectModifiers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Modifier import Modifier

class ObjectModifiers(bpy_struct):

    active: Annotated[Optional['Modifier'], "is_animatable=False"]
    """The active modifier in the list"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Modifier']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Modifier': ...
    def __len__(self) -> int: ...