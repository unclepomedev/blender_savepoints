# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieReconstructedCamera.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieReconstructedCamera(bpy_struct):

    @property
    def frame(self) -> Annotated[int, "step=1"]:
        """Frame number marker is keyframed on"""
        ...
    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Worldspace transformation matrix"""
        ...
    @property
    def average_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average error of reconstruction"""
        ...