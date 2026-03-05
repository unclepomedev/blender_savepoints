# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneTracks.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack

class MovieTrackingPlaneTracks(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['MovieTrackingPlaneTrack'], "is_animatable=False"]:
        """Active plane track in this tracking data object. Deprecated, use objects[name].plane_tracks.active"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['MovieTrackingPlaneTrack'], "is_animatable=False"]) -> None:
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MovieTrackingPlaneTrack']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MovieTrackingPlaneTrack': ...
    def __len__(self) -> int: ...