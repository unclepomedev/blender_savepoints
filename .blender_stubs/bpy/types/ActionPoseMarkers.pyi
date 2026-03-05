# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionPoseMarkers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .TimelineMarker import TimelineMarker

class ActionPoseMarkers(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['TimelineMarker'], "is_animatable=False"]:
        """Active pose marker for this action"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['TimelineMarker'], "is_animatable=False"]) -> None:
        ...
    @property
    def active_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active pose marker"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['TimelineMarker']: ...
    def __getitem__(self, key: Union[str, int]) -> 'TimelineMarker': ...
    def __len__(self) -> int: ...