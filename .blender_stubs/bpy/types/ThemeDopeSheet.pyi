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
    @property
    def grid(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @grid.setter
    def grid(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def keyframe_border(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of keyframe border"""
        ...
    @keyframe_border.setter
    def keyframe_border(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def keyframe_border_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of selected keyframe border"""
        ...
    @keyframe_border_selected.setter
    def keyframe_border_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def keyframe_scale_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scale factor for adjusting the height of keyframes"""
        ...
    @keyframe_scale_factor.setter
    def keyframe_scale_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def summary(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of summary channel"""
        ...
    @summary.setter
    def summary(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def interpolation_line(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of lines showing non-Bézier interpolation modes"""
        ...
    @interpolation_line.setter
    def interpolation_line(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def simulated_frames(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @simulated_frames.setter
    def simulated_frames(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...