# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieClipProxy.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieClipProxy(bpy_struct):

    build_25: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 25% of the original footage dimension"""
    build_50: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 50% of the original footage dimension"""
    build_75: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 75% of the original footage dimension"""
    build_100: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 100% of the original footage dimension"""
    build_undistorted_25: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 25% of the original undistorted footage dimension"""
    build_undistorted_50: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 50% of the original undistorted footage dimension"""
    build_undistorted_75: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 75% of the original undistorted footage dimension"""
    build_undistorted_100: Annotated[bool, "is_animatable=False"]
    """Build proxy resolution 100% of the original undistorted footage dimension"""
    build_record_run: Annotated[bool, "is_animatable=False"]
    """Build record run time code index"""
    quality: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """JPEG quality of proxy images"""
    timecode: Annotated[Literal['NONE', 'RECORD_RUN', 'FREE_RUN_NO_GAPS'], "is_animatable=False"]

    directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Location to store the proxy files"""