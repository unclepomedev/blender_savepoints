# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FCurveModifiers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .FModifier import FModifier

class FCurveModifiers(bpy_struct):

    active: Annotated[Optional['FModifier'], "is_animatable=False"]
    """Active F-Curve Modifier"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['FModifier']: ...
    def __getitem__(self, key: Union[str, int]) -> 'FModifier': ...
    def __len__(self) -> int: ...