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
class MovieTracking(bpy_struct):
    settings: 'MovieTrackingSettings'
    camera: 'MovieTrackingCamera'
    tracks: 'MovieTrackingTracks'
    plane_tracks: 'MovieTrackingPlaneTracks'
    stabilization: 'MovieTrackingStabilization'
    reconstruction: 'MovieTrackingReconstruction'
    objects: 'MovieTrackingObjects'
    active_object_index: int
    dopesheet: 'MovieTrackingDopesheet'