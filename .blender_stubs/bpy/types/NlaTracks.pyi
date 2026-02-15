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
from .NlaTrack import NlaTrack
class NlaTracks(bpy_struct):
    active: Annotated[Optional['NlaTrack'], "is_animatable=False"]
    """Active NLA Track"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['NlaTrack']: ...
    def __getitem__(self, key: Union[str, int]) -> 'NlaTrack': ...
    def __len__(self) -> int: ...