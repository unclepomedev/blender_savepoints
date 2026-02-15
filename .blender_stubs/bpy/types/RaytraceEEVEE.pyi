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

    resolution_scale: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]
    """Determines the number of rays per pixel. Higher resolution uses more memory."""
    use_denoise: Annotated[bool, "is_animatable=False"]
    """Enable noise reduction techniques for raytraced effects"""
    denoise_spatial: Annotated[bool, "is_animatable=False"]
    """Reuse neighbor pixels' rays"""
    denoise_temporal: Annotated[bool, "is_animatable=False"]
    """Accumulate samples by reprojecting last tracing results"""
    denoise_bilateral: Annotated[bool, "is_animatable=False"]
    """Blur the resolved radiance using a bilateral filter"""
    screen_trace_thickness: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=5.0", "precision=3", "is_animatable=False"]
    """Surface thickness used to detect intersection when using screen-tracing"""
    trace_max_roughness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum roughness to use the tracing pipeline for. Higher roughness surfaces will use fast GI approximation. A value of 1 will disable fast GI approximation."""
    screen_trace_quality: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Precision of the screen space ray-tracing"""