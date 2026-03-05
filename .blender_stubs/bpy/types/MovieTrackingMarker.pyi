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

    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Marker position at frame in normalized coordinates"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def frame(self) -> Annotated[int, "step=1"]:
        """Frame number marker is keyframed on"""
        ...
    @frame.setter
    def frame(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Is marker muted for current frame"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def pattern_corners(self) -> Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Array of coordinates which represents pattern's corners in normalized coordinates relative to marker position"""
        ...
    @pattern_corners.setter
    def pattern_corners(self, value: Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def pattern_bound_box(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Pattern area bounding box in normalized coordinates"""
        ...
    @property
    def search_min(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Left-bottom corner of search area in normalized coordinates relative to marker position"""
        ...
    @search_min.setter
    def search_min(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def search_max(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Right-bottom corner of search area in normalized coordinates relative to marker position"""
        ...
    @search_max.setter
    def search_max(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def is_keyed(self) -> Annotated[bool, "is_animatable=False"]:
        """Whether the position of the marker is keyframed or tracked"""
        ...
    @is_keyed.setter
    def is_keyed(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...