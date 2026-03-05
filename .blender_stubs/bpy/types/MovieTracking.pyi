# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTracking.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingCamera import MovieTrackingCamera
from .MovieTrackingDopesheet import MovieTrackingDopesheet
from .MovieTrackingObject import MovieTrackingObject
from .MovieTrackingObjects import MovieTrackingObjects
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingPlaneTracks import MovieTrackingPlaneTracks
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingSettings import MovieTrackingSettings
from .MovieTrackingStabilization import MovieTrackingStabilization
from .MovieTrackingTrack import MovieTrackingTrack
from .MovieTrackingTracks import MovieTrackingTracks
from .bpy_prop_collection import bpy_prop_collection

class MovieTracking(bpy_struct):

    @property
    def settings(self) -> Annotated[Optional['MovieTrackingSettings'], "is_animatable=False"]:

        ...
    @property
    def camera(self) -> Annotated[Optional['MovieTrackingCamera'], "is_animatable=False"]:

        ...
    @property
    def tracks(self) -> Annotated['MovieTrackingTracks', "is_animatable=False"]:
        """Collection of tracks in this tracking data object. Deprecated, use objects[name].tracks"""
        ...
    @property
    def plane_tracks(self) -> Annotated['MovieTrackingPlaneTracks', "is_animatable=False"]:
        """Collection of plane tracks in this tracking data object. Deprecated, use objects[name].plane_tracks"""
        ...
    @property
    def stabilization(self) -> Annotated[Optional['MovieTrackingStabilization'], "is_animatable=False"]:

        ...
    @property
    def reconstruction(self) -> Annotated[Optional['MovieTrackingReconstruction'], "is_animatable=False"]:

        ...
    @property
    def objects(self) -> Annotated['MovieTrackingObjects', "is_animatable=False"]:
        """Collection of objects in this tracking data object"""
        ...
    @property
    def active_object_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Index of active object"""
        ...
    @active_object_index.setter
    def active_object_index(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def dopesheet(self) -> Annotated[Optional['MovieTrackingDopesheet'], "is_animatable=False"]:

        ...