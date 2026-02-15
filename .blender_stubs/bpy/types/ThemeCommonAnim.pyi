# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeCommonAnim.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeCommonAnim(bpy_struct):

    playhead: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    preview_range: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of preview range overlay"""
    scene_strip_range: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of scene strip range overlay"""
    channels: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    channels_sub: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    channel_group: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    channel_group_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    channel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    channel_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    keyframe: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of regular keyframe"""
    keyframe_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected keyframe"""
    keyframe_extreme: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of extreme keyframe"""
    keyframe_extreme_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected extreme keyframe"""
    keyframe_breakdown: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of breakdown keyframe"""
    keyframe_breakdown_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected breakdown keyframe"""
    keyframe_jitter: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of jitter keyframe"""
    keyframe_jitter_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected jitter keyframe"""
    keyframe_moving_hold: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of moving hold keyframe"""
    keyframe_moving_hold_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected moving hold keyframe"""
    keyframe_generated: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of generated keyframe"""
    keyframe_generated_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected generated keyframe"""
    long_key: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    long_key_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
