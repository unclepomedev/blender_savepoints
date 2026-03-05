# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SceneGpencil.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SceneGpencil(bpy_struct):

    @property
    def antialias_threshold(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Threshold for edge detection algorithm (higher values might over-blur some part of the image)"""
        ...
    @antialias_threshold.setter
    def antialias_threshold(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def antialias_threshold_render(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Threshold for edge detection algorithm (higher values might over-blur some part of the image). Only applies to final render"""
        ...
    @antialias_threshold_render.setter
    def antialias_threshold_render(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def aa_samples(self) -> Annotated[int, "step=1"]:
        """Number of supersampling anti-aliasing samples per pixel for final render"""
        ...
    @aa_samples.setter
    def aa_samples(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def motion_blur_steps(self) -> Annotated[int, "step=1"]:
        """Controls accuracy of motion blur, more steps result in longer render time. Only used when Motion Blur is enabled. Set to 0 to disable motion blur for Grease Pencil"""
        ...
    @motion_blur_steps.setter
    def motion_blur_steps(self, value: Annotated[int, "step=1"]):
        ...