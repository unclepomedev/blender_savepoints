# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingMarker.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieTrackingMarker(bpy_struct):

    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Marker position at frame in normalized coordinates"""
    frame: Annotated[int, "step=1"]
    """Frame number marker is keyframed on"""
    mute: bool
    """Is marker muted for current frame"""
    pattern_corners: Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]
    """Array of coordinates which represents pattern's corners in normalized coordinates relative to marker position"""
    @property
    def pattern_bound_box(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Pattern area bounding box in normalized coordinates"""
        ...
    search_min: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]
    """Left-bottom corner of search area in normalized coordinates relative to marker position"""
    search_max: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]
    """Right-bottom corner of search area in normalized coordinates relative to marker position"""
    is_keyed: Annotated[bool, "is_animatable=False"]
    """Whether the position of the marker is keyframed or tracked"""