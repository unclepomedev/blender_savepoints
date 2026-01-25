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
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingSettings import MovieTrackingSettings
from .MovieTrackingStabilization import MovieTrackingStabilization
from .MovieTrackingTrack import MovieTrackingTrack
class MovieTracking(bpy_struct):
    settings: 'MovieTrackingSettings'
    camera: 'MovieTrackingCamera'
    tracks: bpy_prop_collection['MovieTrackingTrack']
    plane_tracks: bpy_prop_collection['MovieTrackingPlaneTrack']
    stabilization: 'MovieTrackingStabilization'
    reconstruction: 'MovieTrackingReconstruction'
    objects: bpy_prop_collection['MovieTrackingObject']
    active_object_index: int
    dopesheet: 'MovieTrackingDopesheet'