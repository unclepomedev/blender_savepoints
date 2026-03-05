# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RaytraceEEVEE.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class RaytraceEEVEE(bpy_struct):

    @property
    def resolution_scale(self) -> Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]:
        """Determines the number of rays per pixel. Higher resolution uses more memory."""
        ...
    @resolution_scale.setter
    def resolution_scale(self, value: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]):
        ...
    @property
    def use_denoise(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable noise reduction techniques for raytraced effects"""
        ...
    @use_denoise.setter
    def use_denoise(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def denoise_spatial(self) -> Annotated[bool, "is_animatable=False"]:
        """Reuse neighbor pixels' rays"""
        ...
    @denoise_spatial.setter
    def denoise_spatial(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def denoise_temporal(self) -> Annotated[bool, "is_animatable=False"]:
        """Accumulate samples by reprojecting last tracing results"""
        ...
    @denoise_temporal.setter
    def denoise_temporal(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def denoise_bilateral(self) -> Annotated[bool, "is_animatable=False"]:
        """Blur the resolved radiance using a bilateral filter"""
        ...
    @denoise_bilateral.setter
    def denoise_bilateral(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def screen_trace_thickness(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=5.0", "precision=3", "is_animatable=False"]:
        """Surface thickness used to detect intersection when using screen-tracing"""
        ...
    @screen_trace_thickness.setter
    def screen_trace_thickness(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=5.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def trace_max_roughness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum roughness to use the tracing pipeline for. Higher roughness surfaces will use fast GI approximation. A value of 1 will disable fast GI approximation."""
        ...
    @trace_max_roughness.setter
    def trace_max_roughness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def screen_trace_quality(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Precision of the screen space ray-tracing"""
        ...
    @screen_trace_quality.setter
    def screen_trace_quality(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...