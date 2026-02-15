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

    name: Annotated[str, "is_animatable=False"]
    """Unique name of track"""
    @property
    def markers(self) -> Annotated['MovieTrackingPlaneMarkers', "is_animatable=False"]:
        """Collection of markers in track"""
        ...
    select: bool
    """Plane track is selected"""
    use_auto_keying: Annotated[bool, "is_animatable=False"]
    """Automatic keyframe insertion when moving plane corners"""
    image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image displayed in the track during editing in clip editor"""
    image_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity of the image"""