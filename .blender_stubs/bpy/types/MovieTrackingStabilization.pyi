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

    @property
    def use_2d_stabilization(self) -> Annotated[bool, "is_animatable=False"]:
        """Use 2D stabilization for footage"""
        ...
    @use_2d_stabilization.setter
    def use_2d_stabilization(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stabilize_rotation(self) -> Annotated[bool, "is_animatable=False"]:
        """Stabilize detected rotation around center of frame"""
        ...
    @use_stabilize_rotation.setter
    def use_stabilize_rotation(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stabilize_scale(self) -> Annotated[bool, "is_animatable=False"]:
        """Compensate any scale changes relative to center of rotation"""
        ...
    @use_stabilize_scale.setter
    def use_stabilize_scale(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def tracks(self) -> Annotated[bpy_prop_collection['MovieTrackingTrack'], "is_animatable=False"]:
        """Collection of tracks used for 2D stabilization (translation)"""
        ...
    @property
    def active_track_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Index of active track in translation stabilization tracks list"""
        ...
    @active_track_index.setter
    def active_track_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def rotation_tracks(self) -> Annotated[bpy_prop_collection['MovieTrackingTrack'], "is_animatable=False"]:
        """Collection of tracks used for 2D stabilization (translation)"""
        ...
    @property
    def active_rotation_track_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Index of active track in rotation stabilization tracks list"""
        ...
    @active_rotation_track_index.setter
    def active_rotation_track_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def anchor_frame(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Reference point to anchor stabilization (other frames will be adjusted relative to this frame's position)"""
        ...
    @anchor_frame.setter
    def anchor_frame(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def target_position(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Known relative offset of original shot, will be subtracted (e.g. for panning shot, can be animated)"""
        ...
    @target_position.setter
    def target_position(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def target_rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation present on original shot, will be compensated (e.g. for deliberate tilting)"""
        ...
    @target_rotation.setter
    def target_rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def target_scale(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]:
        """Explicitly scale resulting frame to compensate zoom of original shot"""
        ...
    @target_scale.setter
    def target_scale(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3"]) -> None:
        ...
    @property
    def use_autoscale(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically scale footage to cover unfilled areas when stabilizing"""
        ...
    @use_autoscale.setter
    def use_autoscale(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def scale_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Limit the amount of automatic scaling"""
        ...
    @scale_max.setter
    def scale_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def influence_location(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of stabilization algorithm on footage location"""
        ...
    @influence_location.setter
    def influence_location(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def influence_scale(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of stabilization algorithm on footage scale"""
        ...
    @influence_scale.setter
    def influence_scale(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def influence_rotation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of stabilization algorithm on footage rotation"""
        ...
    @influence_rotation.setter
    def influence_rotation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def filter_type(self) -> Literal['NEAREST', 'BILINEAR', 'BICUBIC']:
        """Interpolation to use for sub-pixel shifts and rotations due to stabilization"""
        ...
    @filter_type.setter
    def filter_type(self, value: Literal['NEAREST', 'BILINEAR', 'BICUBIC']) -> None:
        ...
    @property
    def show_tracks_expanded(self) -> Annotated[bool, "is_animatable=False"]:
        """Show UI list of tracks participating in stabilization"""
        ...
    @show_tracks_expanded.setter
    def show_tracks_expanded(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...