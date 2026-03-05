# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieTrackingSettings(bpy_struct):

    @property
    def speed(self) -> Annotated[Literal['FASTEST', 'DOUBLE', 'REALTIME', 'HALF', 'QUARTER'], "is_animatable=False"]:
        """Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality)"""
        ...
    @speed.setter
    def speed(self, value: Annotated[Literal['FASTEST', 'DOUBLE', 'REALTIME', 'HALF', 'QUARTER'], "is_animatable=False"]):
        ...
    @property
    def use_keyframe_selection(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically select keyframes when solving camera/object motion"""
        ...
    @use_keyframe_selection.setter
    def use_keyframe_selection(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def refine_intrinsics_focal_length(self) -> Annotated[bool, "is_animatable=False"]:
        """Refine focal length during camera solving"""
        ...
    @refine_intrinsics_focal_length.setter
    def refine_intrinsics_focal_length(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def refine_intrinsics_principal_point(self) -> Annotated[bool, "is_animatable=False"]:
        """Refine principal point during camera solving"""
        ...
    @refine_intrinsics_principal_point.setter
    def refine_intrinsics_principal_point(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def refine_intrinsics_radial_distortion(self) -> Annotated[bool, "is_animatable=False"]:
        """Refine radial coefficients of distortion model during camera solving"""
        ...
    @refine_intrinsics_radial_distortion.setter
    def refine_intrinsics_radial_distortion(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def refine_intrinsics_tangential_distortion(self) -> Annotated[bool, "is_animatable=False"]:
        """Refine tangential coefficients of distortion model during camera solving"""
        ...
    @refine_intrinsics_tangential_distortion.setter
    def refine_intrinsics_tangential_distortion(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def distance(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Distance between two bundles used for scene scaling"""
        ...
    @distance.setter
    def distance(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def clean_frames(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Effect on tracks which are tracked less than the specified amount of frames"""
        ...
    @clean_frames.setter
    def clean_frames(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def clean_error(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Effect on tracks which have a larger re-projection error"""
        ...
    @clean_error.setter
    def clean_error(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def clean_action(self) -> Annotated[Literal['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], "is_animatable=False"]:
        """Cleanup action to execute"""
        ...
    @clean_action.setter
    def clean_action(self, value: Annotated[Literal['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], "is_animatable=False"]):
        ...
    @property
    def use_tripod_solver(self) -> Annotated[bool, "is_animatable=False"]:
        """Use special solver to track a stable camera position, such as a tripod"""
        ...
    @use_tripod_solver.setter
    def use_tripod_solver(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def default_frames_limit(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Every tracking cycle, this number of frames are tracked"""
        ...
    @default_frames_limit.setter
    def default_frames_limit(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def default_pattern_match(self) -> Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]:
        """Track pattern from given frame when tracking marker to next frame"""
        ...
    @default_pattern_match.setter
    def default_pattern_match(self, value: Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]):
        ...
    @property
    def default_margin(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Default distance from image boundary at which marker stops tracking"""
        ...
    @default_margin.setter
    def default_margin(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def default_motion_model(self) -> Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]:
        """Default motion model to use for tracking"""
        ...
    @default_motion_model.setter
    def default_motion_model(self, value: Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]):
        ...
    @property
    def use_default_brute(self) -> bool:
        """Use a brute-force translation-only initialization when tracking"""
        ...
    @use_default_brute.setter
    def use_default_brute(self, value: bool):
        ...
    @property
    def use_default_mask(self) -> bool:
        """Use a Grease Pencil data-block as a mask to use only specified areas of pattern when tracking"""
        ...
    @use_default_mask.setter
    def use_default_mask(self, value: bool):
        ...
    @property
    def use_default_normalization(self) -> bool:
        """Normalize light intensities while tracking (slower)"""
        ...
    @use_default_normalization.setter
    def use_default_normalization(self, value: bool):
        ...
    @property
    def default_correlation_min(self) -> Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]:
        """Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking"""
        ...
    @default_correlation_min.setter
    def default_correlation_min(self, value: Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]):
        ...
    @property
    def default_pattern_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of pattern area for newly created tracks"""
        ...
    @default_pattern_size.setter
    def default_pattern_size(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def default_search_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of search area for newly created tracks"""
        ...
    @default_search_size.setter
    def default_search_size(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_default_red_channel(self) -> bool:
        """Use red channel from footage for tracking"""
        ...
    @use_default_red_channel.setter
    def use_default_red_channel(self, value: bool):
        ...
    @property
    def use_default_green_channel(self) -> bool:
        """Use green channel from footage for tracking"""
        ...
    @use_default_green_channel.setter
    def use_default_green_channel(self, value: bool):
        ...
    @property
    def use_default_blue_channel(self) -> bool:
        """Use blue channel from footage for tracking"""
        ...
    @use_default_blue_channel.setter
    def use_default_blue_channel(self, value: bool):
        ...
    @property
    def default_weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence of newly created track on a final solution"""
        ...
    @default_weight.setter
    def default_weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def object_distance(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Distance between two bundles used for object scaling"""
        ...
    @object_distance.setter
    def object_distance(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]):
        ...