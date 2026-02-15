# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RenderSlots.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .RenderSlot import RenderSlot

class RenderSlots(bpy_struct):

    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Active render slot of the image"""
    active: Annotated[Optional['RenderSlot'], "is_animatable=False"]
    """Active render slot of the image"""
    def new(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['RenderSlot']: ...
    def __getitem__(self, key: Union[str, int]) -> 'RenderSlot': ...
    def __len__(self) -> int: ...