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
from .KeyingSet import KeyingSet
class KeyingSetsAll(bpy_struct):
    active: Annotated[Optional['KeyingSet'], "is_animatable=False"]
    """Active Keying Set used to insert/delete keyframes"""
    active_index: Annotated[int, "step=1"]
    """Current Keying Set index (negative for 'builtin' and positive for 'absolute')"""
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['KeyingSet']: ...
    def __getitem__(self, key: Union[str, int]) -> 'KeyingSet': ...
    def __len__(self) -> int: ...