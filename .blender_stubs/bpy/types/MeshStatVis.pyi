# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshStatVis.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshStatVis(bpy_struct):

    type: Annotated[Literal['OVERHANG', 'THICKNESS', 'INTERSECT', 'DISTORT', 'SHARP'], "is_animatable=False"]
    """Type of data to visualize/check"""
    overhang_min: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Minimum angle to display"""
    overhang_max: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum angle to display"""
    overhang_axis: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]

    thickness_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """Minimum for measuring thickness"""
    thickness_max: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """Maximum for measuring thickness"""
    thickness_samples: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Number of samples to test per face"""
    distort_min: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Minimum angle to display"""
    distort_max: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum angle to display"""
    sharp_min: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Minimum angle to display"""
    sharp_max: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum angle to display"""