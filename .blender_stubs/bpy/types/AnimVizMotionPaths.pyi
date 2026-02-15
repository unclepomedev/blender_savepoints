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

    type: Literal['CURRENT_FRAME', 'RANGE']
    """Type of range to show for Motion Paths"""
    range: Literal['KEYS_ALL', 'KEYS_SELECTED', 'SCENE', 'MANUAL']
    """Type of range to calculate for Motion Paths"""
    bake_location: Literal['HEADS', 'TAILS']
    """When calculating Bone Paths, use Head or Tips"""
    show_frame_numbers: bool
    """Show frame numbers on Motion Paths"""
    show_keyframe_highlight: bool
    """Emphasize position of keyframes on Motion Paths"""
    show_keyframe_numbers: bool
    """Show frame numbers of Keyframes on Motion Paths"""
    show_keyframe_action_all: bool
    """For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower)"""
    frame_step: Annotated[int, "step=1"]
    """Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method)"""
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Starting frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """End frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)"""
    frame_before: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Number of frames to show before the current frame (only for 'Around Frame' Onion-skinning method)"""
    frame_after: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Number of frames to show after the current frame (only for 'Around Frame' Onion-skinning method)"""
    @property
    def has_motion_paths(self) -> bool:
        """Are there any bone paths that will need updating (read-only)"""
        ...
    use_camera_space_bake: bool
    """Motion path points will be baked into the camera space of the active camera. This means they will only look right when looking through that camera. Switching cameras using markers is not supported."""