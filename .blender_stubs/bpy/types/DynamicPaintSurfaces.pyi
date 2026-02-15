# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .DynamicPaintSurface import DynamicPaintSurface
class DynamicPaintSurfaces(bpy_struct):
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    @property
    def active(self) -> Annotated[Optional['DynamicPaintSurface'], "is_animatable=False"]:
        """Active Dynamic Paint surface being displayed"""
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['DynamicPaintSurface']: ...
    def __getitem__(self, key: Union[str, int]) -> 'DynamicPaintSurface': ...
    def __len__(self) -> int: ...