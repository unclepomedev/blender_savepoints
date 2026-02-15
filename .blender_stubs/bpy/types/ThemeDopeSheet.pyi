# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeDopeSheet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeDopeSheet(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    keyframe_border: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of keyframe border"""
    keyframe_border_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected keyframe border"""
    keyframe_scale_factor: Annotated[float, "step=10.0", "precision=3"]
    """Scale factor for adjusting the height of keyframes"""
    summary: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of summary channel"""
    interpolation_line: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of lines showing non-Bézier interpolation modes"""
    simulated_frames: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
