# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MotionPath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MotionPathVert import MotionPathVert
from .bpy_prop_collection import bpy_prop_collection

class MotionPath(bpy_struct):

    @property
    def points(self) -> Annotated[bpy_prop_collection['MotionPathVert'], "is_animatable=False"]:
        """Cached positions per frame"""
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Starting frame of the stored range"""
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """End frame of the stored range"""
        ...
    @property
    def length(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Number of frames cached"""
        ...
    color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Custom color for motion path before the current frame"""
    color_post: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Custom color for motion path after the current frame"""
    line_thickness: Annotated[int, "step=1"]
    """Line thickness for motion path"""
    @property
    def use_bone_head(self) -> bool:
        """For PoseBone paths, use the bone head location when calculating this path"""
        ...
    is_modified: bool
    """Path is being edited"""
    use_custom_color: bool
    """Use custom color for this motion path"""
    lines: bool
    """Use straight lines between keyframe points"""