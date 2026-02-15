# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class ImageUser(bpy_struct):
    use_auto_refresh: Annotated[bool, "is_animatable=False"]
    """Always refresh image on frame changes"""
    frame_current: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Current frame number in image sequence or movie"""
    use_cyclic: Annotated[bool, "is_animatable=False"]
    """Cycle the images in the movie"""
    frame_duration: Annotated[int, "step=1", "is_animatable=False"]
    """Number of images of a movie to use"""
    frame_offset: Annotated[int, "step=1"]
    """Offset the number of the frame to use in the animation"""
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Global starting frame of the movie/sequence, assuming first picture has a #1"""
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
    tile: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Tile in tiled image"""