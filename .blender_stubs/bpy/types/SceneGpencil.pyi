# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class SceneGpencil(bpy_struct):
    antialias_threshold: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Threshold for edge detection algorithm (higher values might over-blur some part of the image)"""
    antialias_threshold_render: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Threshold for edge detection algorithm (higher values might over-blur some part of the image). Only applies to final render"""
    aa_samples: Annotated[int, "step=1"]
    """Number of supersampling anti-aliasing samples per pixel for final render"""
    motion_blur_steps: Annotated[int, "step=1"]
    """Controls accuracy of motion blur, more steps result in longer render time. Only used when Motion Blur is enabled. Set to 0 to disable motion blur for Grease Pencil"""