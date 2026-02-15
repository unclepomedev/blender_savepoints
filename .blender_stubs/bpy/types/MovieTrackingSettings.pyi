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

    speed: Annotated[Literal['FASTEST', 'DOUBLE', 'REALTIME', 'HALF', 'QUARTER'], "is_animatable=False"]
    """Limit speed of tracking to make visual feedback easier (this does not affect the tracking quality)"""
    use_keyframe_selection: Annotated[bool, "is_animatable=False"]
    """Automatically select keyframes when solving camera/object motion"""
    refine_intrinsics_focal_length: Annotated[bool, "is_animatable=False"]
    """Refine focal length during camera solving"""
    refine_intrinsics_principal_point: Annotated[bool, "is_animatable=False"]
    """Refine principal point during camera solving"""
    refine_intrinsics_radial_distortion: Annotated[bool, "is_animatable=False"]
    """Refine radial coefficients of distortion model during camera solving"""
    refine_intrinsics_tangential_distortion: Annotated[bool, "is_animatable=False"]
    """Refine tangential coefficients of distortion model during camera solving"""
    distance: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Distance between two bundles used for scene scaling"""
    clean_frames: Annotated[int, "step=1", "is_animatable=False"]
    """Effect on tracks which are tracked less than the specified amount of frames"""
    clean_error: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Effect on tracks which have a larger re-projection error"""
    clean_action: Annotated[Literal['SELECT', 'DELETE_TRACK', 'DELETE_SEGMENTS'], "is_animatable=False"]
    """Cleanup action to execute"""
    use_tripod_solver: Annotated[bool, "is_animatable=False"]
    """Use special solver to track a stable camera position, such as a tripod"""
    default_frames_limit: Annotated[int, "step=1", "is_animatable=False"]
    """Every tracking cycle, this number of frames are tracked"""
    default_pattern_match: Annotated[Literal['KEYFRAME', 'PREV_FRAME'], "is_animatable=False"]
    """Track pattern from given frame when tracking marker to next frame"""
    default_margin: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Default distance from image boundary at which marker stops tracking"""
    default_motion_model: Annotated[Literal['Perspective', 'Affine', 'LocRotScale', 'LocScale', 'LocRot', 'Loc'], "is_animatable=False"]
    """Default motion model to use for tracking"""
    use_default_brute: bool
    """Use a brute-force translation-only initialization when tracking"""
    use_default_mask: bool
    """Use a Grease Pencil data-block as a mask to use only specified areas of pattern when tracking"""
    use_default_normalization: bool
    """Normalize light intensities while tracking (slower)"""
    default_correlation_min: Annotated[float, "step=0.05000000074505806", "precision=3", "is_animatable=False"]
    """Default minimum value of correlation between matched pattern and reference that is still treated as successful tracking"""
    default_pattern_size: Annotated[int, "step=1", "is_animatable=False"]
    """Size of pattern area for newly created tracks"""
    default_search_size: Annotated[int, "step=1", "is_animatable=False"]
    """Size of search area for newly created tracks"""
    use_default_red_channel: bool
    """Use red channel from footage for tracking"""
    use_default_green_channel: bool
    """Use green channel from footage for tracking"""
    use_default_blue_channel: bool
    """Use blue channel from footage for tracking"""
    default_weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence of newly created track on a final solution"""
    object_distance: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Distance between two bundles used for object scaling"""