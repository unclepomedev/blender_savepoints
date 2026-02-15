# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrActionMaps.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .XrActionMap import XrActionMap

class XrActionMaps(bpy_struct):

    def new(self, *args, **kwargs) -> Any: ...
    def new_from_actionmap(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def find(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['XrActionMap']: ...
    def __getitem__(self, key: Union[str, int]) -> 'XrActionMap': ...
    def __len__(self) -> int: ...