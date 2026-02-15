# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BlendDataGreasePencilsV3.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .GreasePencil import GreasePencil

class BlendDataGreasePencilsV3(bpy_struct):

    def tag(self, *args, **kwargs) -> Any: ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['GreasePencil']: ...
    def __getitem__(self, key: Union[str, int]) -> 'GreasePencil': ...
    def __len__(self) -> int: ...