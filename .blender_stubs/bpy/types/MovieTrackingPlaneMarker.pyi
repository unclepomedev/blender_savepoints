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

    frame: Annotated[int, "step=1"]
    """Frame number marker is keyframed on"""
    corners: Annotated[list[float], "subtype='MATRIX'", "step=1.0", "precision=5", "is_animatable=False"]
    """Array of coordinates which represents UI rectangle corners in frame normalized coordinates"""
    mute: bool
    """Is marker muted for current frame"""