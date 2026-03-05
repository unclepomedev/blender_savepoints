# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingPlaneTrack.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Image import Image
from .MovieTrackingPlaneMarker import MovieTrackingPlaneMarker
from .MovieTrackingPlaneMarkers import MovieTrackingPlaneMarkers
from .bpy_prop_collection import bpy_prop_collection

class MovieTrackingPlaneTrack(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name of track"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def markers(self) -> Annotated['MovieTrackingPlaneMarkers', "is_animatable=False"]:
        """Collection of markers in track"""
        ...
    @property
    def select(self) -> bool:
        """Plane track is selected"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def use_auto_keying(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatic keyframe insertion when moving plane corners"""
        ...
    @use_auto_keying.setter
    def use_auto_keying(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image displayed in the track during editing in clip editor"""
        ...
    @image.setter
    def image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def image_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity of the image"""
        ...
    @image_opacity.setter
    def image_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...