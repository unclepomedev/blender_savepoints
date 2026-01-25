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
from .MovieTrackingTrack import MovieTrackingTrack
class MovieTrackingStabilization(bpy_struct):
    use_2d_stabilization: bool
    use_stabilize_rotation: bool
    use_stabilize_scale: bool
    tracks: bpy_prop_collection['MovieTrackingTrack']
    active_track_index: int
    rotation_tracks: bpy_prop_collection['MovieTrackingTrack']
    active_rotation_track_index: int
    anchor_frame: int
    target_position: float
    target_rotation: float
    target_scale: float
    use_autoscale: bool
    scale_max: float
    influence_location: float
    influence_scale: float
    influence_rotation: float
    filter_type: str
    show_tracks_expanded: bool