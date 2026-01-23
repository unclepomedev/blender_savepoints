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
class MovieTrackingSettings(bpy_struct):
    speed: str
    use_keyframe_selection: bool
    refine_intrinsics_focal_length: bool
    refine_intrinsics_principal_point: bool
    refine_intrinsics_radial_distortion: bool
    refine_intrinsics_tangential_distortion: bool
    distance: float
    clean_frames: int
    clean_error: float
    clean_action: str
    use_tripod_solver: bool
    default_frames_limit: int
    default_pattern_match: str
    default_margin: int
    default_motion_model: str
    use_default_brute: bool
    use_default_mask: bool
    use_default_normalization: bool
    default_correlation_min: float
    default_pattern_size: int
    default_search_size: int
    use_default_red_channel: bool
    use_default_green_channel: bool
    use_default_blue_channel: bool
    default_weight: float
    object_distance: float