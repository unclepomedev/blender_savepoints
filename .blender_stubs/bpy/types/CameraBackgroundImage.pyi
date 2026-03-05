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
    @property
    def source(self) -> Literal['IMAGE', 'MOVIE_CLIP']:
        """Data source used for background"""
        ...
    @source.setter
    def source(self, value: Literal['IMAGE', 'MOVIE_CLIP']) -> None:
        ...
    @property
    def image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image displayed and edited in this space"""
        ...
    @image.setter
    def image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def clip(self) -> Annotated[Optional['MovieClip'], "is_animatable=False"]:
        """Movie clip displayed and edited in this space"""
        ...
    @clip.setter
    def clip(self, value: Annotated[Optional['MovieClip'], "is_animatable=False"]) -> None:
        ...
    @property
    def image_user(self) -> Annotated['ImageUser', "is_animatable=False"]:
        """Parameters defining which layer, pass and frame of the image is displayed"""
        ...
    @property
    def clip_user(self) -> Annotated['MovieClipUser', "is_animatable=False"]:
        """Parameters defining which frame of the movie clip is displayed"""
        ...
    @property
    def offset(self) -> Annotated[list[float], "subtype='XYZ'", "step=0.10000000149011612", "precision=5"]:

        ...
    @offset.setter
    def offset(self, value: Annotated[list[float], "subtype='XYZ'", "step=0.10000000149011612", "precision=5"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[float, "step=0.10000000149011612", "precision=5"]:
        """Scale the background image"""
        ...
    @scale.setter
    def scale(self, value: Annotated[float, "step=0.10000000149011612", "precision=5"]) -> None:
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation for the background image (ortho view only)"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_flip_x(self) -> bool:
        """Flip the background image horizontally"""
        ...
    @use_flip_x.setter
    def use_flip_x(self, value: bool) -> None:
        ...
    @property
    def use_flip_y(self) -> bool:
        """Flip the background image vertically"""
        ...
    @use_flip_y.setter
    def use_flip_y(self, value: bool) -> None:
        ...
    @property
    def alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Image opacity to blend the image against the background color"""
        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Show the details in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def use_camera_clip(self) -> bool:
        """Use movie clip from active scene camera"""
        ...
    @use_camera_clip.setter
    def use_camera_clip(self, value: bool) -> None:
        ...
    @property
    def show_background_image(self) -> bool:
        """Show this image as background"""
        ...
    @show_background_image.setter
    def show_background_image(self, value: bool) -> None:
        ...
    @property
    def show_on_foreground(self) -> bool:
        """Show this image in front of objects in viewport"""
        ...
    @show_on_foreground.setter
    def show_on_foreground(self, value: bool) -> None:
        ...
    @property
    def display_depth(self) -> Literal['BACK', 'FRONT']:
        """Display under or over everything"""
        ...
    @display_depth.setter
    def display_depth(self, value: Literal['BACK', 'FRONT']) -> None:
        ...
    @property
    def frame_method(self) -> Literal['STRETCH', 'FIT', 'CROP']:
        """How the image fits in the camera frame"""
        ...
    @frame_method.setter
    def frame_method(self, value: Literal['STRETCH', 'FIT', 'CROP']) -> None:
        ...