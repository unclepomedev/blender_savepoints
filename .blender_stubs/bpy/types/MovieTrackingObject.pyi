# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingObject.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingObjectPlaneTracks import MovieTrackingObjectPlaneTracks
from .MovieTrackingObjectTracks import MovieTrackingObjectTracks
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingTrack import MovieTrackingTrack
from .bpy_prop_collection import bpy_prop_collection

class MovieTrackingObject(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name of object"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def is_camera(self) -> bool:
        """Object is used for camera tracking"""
        ...
    @property
    def tracks(self) -> Annotated['MovieTrackingObjectTracks', "is_animatable=False"]:
        """Collection of tracks in this tracking data object"""
        ...
    @property
    def plane_tracks(self) -> Annotated['MovieTrackingObjectPlaneTracks', "is_animatable=False"]:
        """Collection of plane tracks in this tracking data object"""
        ...
    @property
    def reconstruction(self) -> Annotated[Optional['MovieTrackingReconstruction'], "is_animatable=False"]:

        ...
    @property
    def scale(self) -> Annotated[float, "step=1.0", "precision=4", "is_animatable=False"]:
        """Scale of object solution in camera space"""
        ...
    @scale.setter
    def scale(self, value: Annotated[float, "step=1.0", "precision=4", "is_animatable=False"]) -> None:
        ...
    @property
    def keyframe_a(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """First keyframe used for reconstruction initialization"""
        ...
    @keyframe_a.setter
    def keyframe_a(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def keyframe_b(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Second keyframe used for reconstruction initialization"""
        ...
    @keyframe_b.setter
    def keyframe_b(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...