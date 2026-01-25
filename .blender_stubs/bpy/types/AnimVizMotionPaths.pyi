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
class AnimVizMotionPaths(bpy_struct):
    type: str
    range: str
    bake_location: str
    show_frame_numbers: bool
    show_keyframe_highlight: bool
    show_keyframe_numbers: bool
    show_keyframe_action_all: bool
    frame_step: int
    frame_start: int
    frame_end: int
    frame_before: int
    frame_after: int
    has_motion_paths: bool
    use_camera_space_bake: bool