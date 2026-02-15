# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingStabilization.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingTrack import MovieTrackingTrack
from .bpy_prop_collection import bpy_prop_collection

class MovieTrackingStabilization(bpy_struct):

    use_2d_stabilization: Annotated[bool, "is_animatable=False"]
    """Use 2D stabilization for footage"""
    use_stabilize_rotation: Annotated[bool, "is_animatable=False"]
    """Stabilize detected rotation around center of frame"""
    use_stabilize_scale: Annotated[bool, "is_animatable=False"]
    """Compensate any scale changes relative to center of rotation"""
    @property
    def tracks(self) -> Annotated[bpy_prop_collection['MovieTrackingTrack'], "is_animatable=False"]:
        """Collection of tracks used for 2D stabilization (translation)"""
        ...
    active_track_index: Annotated[int, "step=1", "is_animatable=False"]
    """Index of active track in translation stabilization tracks list"""
    @property
    def rotation_tracks(self) -> Annotated[bpy_prop_collection['MovieTrackingTrack'], "is_animatable=False"]:
        """Collection of tracks used for 2D stabilization (translation)"""
        ...
    active_rotation_track_index: Annotated[int, "step=1", "is_animatable=False"]
    """Index of active track in rotation stabilization tracks list"""
    anchor_frame: Annotated[int, "step=1", "is_animatable=False"]
    """Reference point to anchor stabilization (other frames will be adjusted relative to this frame's position)"""
    target_position: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated)"""
    target_rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation present on original shot, will be compensated (e.g. for deliberate tilting)"""
    target_scale: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]
    """Explicitly scale resulting frame to compensate zoom of original shot"""
    use_autoscale: Annotated[bool, "is_animatable=False"]
    """Automatically scale footage to cover unfilled areas when stabilizing"""
    scale_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Limit the amount of automatic scaling"""
    influence_location: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of stabilization algorithm on footage location"""
    influence_scale: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of stabilization algorithm on footage scale"""
    influence_rotation: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of stabilization algorithm on footage rotation"""
    filter_type: Literal['NEAREST', 'BILINEAR', 'BICUBIC']
    """Interpolation to use for sub-pixel shifts and rotations due to stabilization"""
    show_tracks_expanded: Annotated[bool, "is_animatable=False"]
    """Show UI list of tracks participating in stabilization"""