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
class ThemeCommonAnim(bpy_struct):
    playhead: list[float]
    preview_range: list[float]
    scene_strip_range: list[float]
    channels: list[float]
    channels_sub: list[float]
    channel_group: list[float]
    channel_group_active: list[float]
    channel: list[float]
    channel_selected: list[float]
    keyframe: list[float]
    keyframe_selected: list[float]
    keyframe_extreme: list[float]
    keyframe_extreme_selected: list[float]
    keyframe_breakdown: list[float]
    keyframe_breakdown_selected: list[float]
    keyframe_jitter: list[float]
    keyframe_jitter_selected: list[float]
    keyframe_moving_hold: list[float]
    keyframe_moving_hold_selected: list[float]
    keyframe_generated: list[float]
    keyframe_generated_selected: list[float]
    long_key: list[float]
    long_key_selected: list[float]