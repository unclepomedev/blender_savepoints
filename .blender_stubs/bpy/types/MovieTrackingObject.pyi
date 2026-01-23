# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .MovieTrackingPlaneTrack import MovieTrackingPlaneTrack
from .MovieTrackingReconstruction import MovieTrackingReconstruction
from .MovieTrackingTrack import MovieTrackingTrack
class MovieTrackingObject(bpy_struct):
    name: str
    is_camera: bool
    tracks: bpy_prop_collection['MovieTrackingTrack']
    plane_tracks: bpy_prop_collection['MovieTrackingPlaneTrack']
    reconstruction: 'MovieTrackingReconstruction'
    scale: float
    keyframe_a: int
    keyframe_b: int