# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingMarkers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MovieTrackingMarker import MovieTrackingMarker

class MovieTrackingMarkers(bpy_struct):

    def find_frame(self, *args, **kwargs) -> Any: ...
    def insert_frame(self, *args, **kwargs) -> Any: ...
    def delete_frame(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MovieTrackingMarker']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MovieTrackingMarker': ...
    def __len__(self) -> int: ...