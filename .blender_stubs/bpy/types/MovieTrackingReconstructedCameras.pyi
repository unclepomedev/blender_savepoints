# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingReconstructedCameras.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieReconstructedCamera import MovieReconstructedCamera

class MovieTrackingReconstructedCameras(bpy_struct):

    def find_frame(self, *args, **kwargs) -> Any: ...
    def matrix_from_frame(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MovieReconstructedCamera']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MovieReconstructedCamera': ...
    def __len__(self) -> int: ...