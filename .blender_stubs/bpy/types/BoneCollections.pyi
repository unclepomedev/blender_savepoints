# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoneCollections.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BoneCollection import BoneCollection

class BoneCollections(bpy_struct):

    active: Annotated[Optional['BoneCollection'], "is_animatable=False"]
    """Armature's active bone collection"""
    active_index: Annotated[int, "step=1"]
    """The index of the Armature's active bone collection; -1 when there is no active collection. Note that this is indexing the underlying array of bone collections, which may not be in the order you expect. Root collections are listed first, and siblings are always sequential. Apart from that, bone collections can be in any order, and thus incrementing or decrementing this index can make the active bone collection jump around in unexpected ways. For a more predictable interface, use ``active`` or ``active_name``."""
    active_name: Annotated[str, "is_animatable=False"]
    """The name of the Armature's active bone collection; empty when there is no active collection"""
    @property
    def is_solo_active(self) -> bool:
        """Read-only flag that indicates there is at least one bone collection marked as 'solo'"""
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['BoneCollection']: ...
    def __getitem__(self, key: Union[str, int]) -> 'BoneCollection': ...
    def __len__(self) -> int: ...