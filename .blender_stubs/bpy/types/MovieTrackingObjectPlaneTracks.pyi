# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingObjectPlaneTracks.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingTrack import MovieTrackingTrack

class MovieTrackingObjectPlaneTracks(bpy_struct):

    active: Annotated[Optional['MovieTrackingTrack'], "is_animatable=False"]
    """Active track in this tracking data object"""
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MovieTrackingPlaneTrack']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MovieTrackingPlaneTrack': ...
    def __len__(self) -> int: ...