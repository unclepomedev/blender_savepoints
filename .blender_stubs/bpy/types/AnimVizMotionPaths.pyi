# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnimVizMotionPaths.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class AnimVizMotionPaths(bpy_struct):

    @property
    def type(self) -> Literal['CURRENT_FRAME', 'RANGE']:
        """Type of range to show for Motion Paths"""
        ...
    @type.setter
    def type(self, value: Literal['CURRENT_FRAME', 'RANGE']) -> None:
        ...
    @property
    def range(self) -> Literal['KEYS_ALL', 'KEYS_SELECTED', 'SCENE', 'MANUAL']:
        """Type of range to calculate for Motion Paths"""
        ...
    @range.setter
    def range(self, value: Literal['KEYS_ALL', 'KEYS_SELECTED', 'SCENE', 'MANUAL']) -> None:
        ...
    @property
    def bake_location(self) -> Literal['HEADS', 'TAILS']:
        """When calculating Bone Paths, use Head or Tips"""
        ...
    @bake_location.setter
    def bake_location(self, value: Literal['HEADS', 'TAILS']) -> None:
        ...
    @property
    def show_frame_numbers(self) -> bool:
        """Show frame numbers on Motion Paths"""
        ...
    @show_frame_numbers.setter
    def show_frame_numbers(self, value: bool) -> None:
        ...
    @property
    def show_keyframe_highlight(self) -> bool:
        """Emphasize position of keyframes on Motion Paths"""
        ...
    @show_keyframe_highlight.setter
    def show_keyframe_highlight(self, value: bool) -> None:
        ...
    @property
    def show_keyframe_numbers(self) -> bool:
        """Show frame numbers of Keyframes on Motion Paths"""
        ...
    @show_keyframe_numbers.setter
    def show_keyframe_numbers(self, value: bool) -> None:
        ...
    @property
    def show_keyframe_action_all(self) -> bool:
        """For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower)"""
        ...
    @show_keyframe_action_all.setter
    def show_keyframe_action_all(self, value: bool) -> None:
        ...
    @property
    def frame_step(self) -> Annotated[int, "step=1"]:
        """Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method)"""
        ...
    @frame_step.setter
    def frame_step(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Starting frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """End frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def frame_before(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Number of frames to show before the current frame (only for 'Around Frame' Onion-skinning method)"""
        ...
    @frame_before.setter
    def frame_before(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def frame_after(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Number of frames to show after the current frame (only for 'Around Frame' Onion-skinning method)"""
        ...
    @frame_after.setter
    def frame_after(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]) -> None:
        ...
    @property
    def has_motion_paths(self) -> bool:
        """Are there any bone paths that will need updating (read-only)"""
        ...
    @property
    def use_camera_space_bake(self) -> bool:
        """Motion path points will be baked into the camera space of the active camera. This means they will only look right when looking through that camera. Switching cameras using markers is not supported."""
        ...
    @use_camera_space_bake.setter
    def use_camera_space_bake(self, value: bool) -> None:
        ...