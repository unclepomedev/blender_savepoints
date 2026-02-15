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
from .MovieTrackingObjectPlaneTracks import MovieTrackingObjectPlaneTracks
from .MovieTrackingObjectTracks import MovieTrackingObjectTracks
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingTrack import MovieTrackingTrack
class MovieTrackingObject(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Unique name of object"""
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
    scale: Annotated[float, "step=1.0", "precision=4", "is_animatable=False"]
    """Scale of object solution in camera space"""
    keyframe_a: Annotated[int, "step=1", "is_animatable=False"]
    """First keyframe used for reconstruction initialization"""
    keyframe_b: Annotated[int, "step=1", "is_animatable=False"]
    """Second keyframe used for reconstruction initialization"""