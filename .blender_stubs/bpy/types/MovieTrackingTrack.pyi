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
from .Annotation import Annotation
from .MovieTrackingMarker import MovieTrackingMarker
class MovieTrackingTrack(bpy_struct):
    name: str
    frames_limit: int
    pattern_match: str
    margin: int
    motion_model: str
    correlation_min: float
    use_brute: bool
    use_mask: bool
    use_normalization: bool
    markers: bpy_prop_collection['MovieTrackingMarker']
    use_red_channel: bool
    use_green_channel: bool
    use_blue_channel: bool
    use_grayscale_preview: bool
    use_alpha_preview: bool
    has_bundle: bool
    bundle: list[float]
    hide: bool
    select: bool
    select_anchor: bool
    select_pattern: bool
    select_search: bool
    lock: bool
    use_custom_color: bool
    color: list[float]
    average_error: float
    annotation: 'Annotation'
    weight: float
    weight_stab: float
    offset: list[float]