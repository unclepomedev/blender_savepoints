# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .MovieTrackingObjectPlaneTracks import MovieTrackingObjectPlaneTracks
from .MovieTrackingObjectTracks import MovieTrackingObjectTracks
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingTrack import MovieTrackingTrack
class MovieTrackingObject(bpy_struct):
    name: str
    is_camera: bool
    tracks: 'MovieTrackingObjectTracks'
    plane_tracks: 'MovieTrackingObjectPlaneTracks'
    reconstruction: 'MovieTrackingReconstruction'
    scale: float
    keyframe_a: int
    keyframe_b: int