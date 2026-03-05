# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ImageUser.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ImageUser(bpy_struct):

    @property
    def use_auto_refresh(self) -> Annotated[bool, "is_animatable=False"]:
        """Always refresh image on frame changes"""
        ...
    @use_auto_refresh.setter
    def use_auto_refresh(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def frame_current(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Current frame number in image sequence or movie"""
        ...
    @frame_current.setter
    def frame_current(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def use_cyclic(self) -> Annotated[bool, "is_animatable=False"]:
        """Cycle the images in the movie"""
        ...
    @use_cyclic.setter
    def use_cyclic(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def frame_duration(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of images of a movie to use"""
        ...
    @frame_duration.setter
    def frame_duration(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_offset(self) -> Annotated[int, "step=1"]:
        """Offset the number of the frame to use in the animation"""
        ...
    @frame_offset.setter
    def frame_offset(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Global starting frame of the movie/sequence, assuming first picture has a #1"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def multilayer_layer(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Layer in multilayer image"""
        ...
    @property
    def multilayer_pass(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Pass in multilayer image"""
        ...
    @property
    def multilayer_view(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """View in multilayer image"""
        ...
    @property
    def tile(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Tile in tiled image"""
        ...
    @tile.setter
    def tile(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...