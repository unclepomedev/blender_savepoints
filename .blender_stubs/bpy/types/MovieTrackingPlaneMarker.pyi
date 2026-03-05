# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneMarker.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieTrackingPlaneMarker(bpy_struct):

    @property
    def frame(self) -> Annotated[int, "step=1"]:
        """Frame number marker is keyframed on"""
        ...
    @frame.setter
    def frame(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def corners(self) -> Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Array of coordinates which represents UI rectangle corners in frame normalized coordinates"""
        ...
    @corners.setter
    def corners(self, value: Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Is marker muted for current frame"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...