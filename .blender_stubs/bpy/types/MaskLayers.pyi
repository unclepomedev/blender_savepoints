# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskLayers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MaskLayer import MaskLayer

class MaskLayers(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['MaskLayer'], "is_animatable=False"]:
        """Active layer in this mask"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['MaskLayer'], "is_animatable=False"]):
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MaskLayer']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MaskLayer': ...
    def __len__(self) -> int: ...