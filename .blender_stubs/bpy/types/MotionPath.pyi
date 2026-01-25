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
from .MotionPathVert import MotionPathVert
class MotionPath(bpy_struct):
    points: bpy_prop_collection['MotionPathVert']
    frame_start: int
    frame_end: int
    length: int
    color: float
    color_post: float
    line_thickness: int
    use_bone_head: bool
    is_modified: bool
    use_custom_color: bool
    lines: bool