# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CameraBackgroundImage.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Image import Image
from .ImageUser import ImageUser
from .MovieClip import MovieClip
from .MovieClipUser import MovieClipUser

class CameraBackgroundImage(bpy_struct):

    @property
    def is_override_data(self) -> bool:
        """In a local override camera, whether this background image comes from the linked reference camera, or is local to the override"""
        ...
    source: Literal['IMAGE', 'MOVIE_CLIP']
    """Data source used for background"""
    image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image displayed and edited in this space"""
    clip: Annotated[Optional['MovieClip'], "is_animatable=False"]
    """Movie clip displayed and edited in this space"""
    @property
    def image_user(self) -> Annotated['ImageUser', "is_animatable=False"]:
        """Parameters defining which layer, pass and frame of the image is displayed"""
        ...
    @property
    def clip_user(self) -> Annotated['MovieClipUser', "is_animatable=False"]:
        """Parameters defining which frame of the movie clip is displayed"""
        ...
    offset: Annotated[list[float], "subtype='XYZ'", "step=0.10000000149011612", "precision=5"]

    scale: Annotated[float, "step=0.10000000149011612", "precision=5"]
    """Scale the background image"""
    rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation for the background image (ortho view only)"""
    use_flip_x: bool
    """Flip the background image horizontally"""
    use_flip_y: bool
    """Flip the background image vertically"""
    alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Image opacity to blend the image against the background color"""
    show_expanded: bool
    """Show the details in the user interface"""
    use_camera_clip: bool
    """Use movie clip from active scene camera"""
    show_background_image: bool
    """Show this image as background"""
    show_on_foreground: bool
    """Show this image in front of objects in viewport"""
    display_depth: Literal['BACK', 'FRONT']
    """Display under or over everything"""
    frame_method: Literal['STRETCH', 'FIT', 'CROP']
    """How the image fits in the camera frame"""