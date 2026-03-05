# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequencerToolSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SequencerToolSettings(bpy_struct):

    @property
    def fit_method(self) -> Annotated[Literal['FIT', 'FILL', 'STRETCH', 'ORIGINAL'], "is_animatable=False"]:
        """Scale fit method"""
        ...
    @fit_method.setter
    def fit_method(self, value: Annotated[Literal['FIT', 'FILL', 'STRETCH', 'ORIGINAL'], "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_current_frame(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to current frame"""
        ...
    @snap_to_current_frame.setter
    def snap_to_current_frame(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_hold_offset(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to strip hold offsets"""
        ...
    @snap_to_hold_offset.setter
    def snap_to_hold_offset(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_markers(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to markers"""
        ...
    @snap_to_markers.setter
    def snap_to_markers(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_retiming_keys(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to retiming keys"""
        ...
    @snap_to_retiming_keys.setter
    def snap_to_retiming_keys(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_frame_range(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to preview or scene start and end frame"""
        ...
    @snap_to_frame_range.setter
    def snap_to_frame_range(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_borders(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to preview borders"""
        ...
    @snap_to_borders.setter
    def snap_to_borders(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_center(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to preview center"""
        ...
    @snap_to_center.setter
    def snap_to_center(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_to_strips_preview(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to borders and origins of deselected, visible strips"""
        ...
    @snap_to_strips_preview.setter
    def snap_to_strips_preview(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_ignore_muted(self) -> Annotated[bool, "is_animatable=False"]:
        """Don't snap to hidden strips"""
        ...
    @snap_ignore_muted.setter
    def snap_ignore_muted(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_ignore_sound(self) -> Annotated[bool, "is_animatable=False"]:
        """Don't snap to sound strips"""
        ...
    @snap_ignore_sound.setter
    def snap_ignore_sound(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_snap_current_frame_to_strips(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap current frame to strip start or end"""
        ...
    @use_snap_current_frame_to_strips.setter
    def use_snap_current_frame_to_strips(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def snap_distance(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Maximum distance for snapping in pixels"""
        ...
    @snap_distance.setter
    def snap_distance(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def overlap_mode(self) -> Annotated[Literal['EXPAND', 'OVERWRITE', 'SHUFFLE'], "is_animatable=False"]:
        """How to resolve overlap after transformation"""
        ...
    @overlap_mode.setter
    def overlap_mode(self, value: Annotated[Literal['EXPAND', 'OVERWRITE', 'SHUFFLE'], "is_animatable=False"]) -> None:
        ...
    @property
    def pivot_point(self) -> Annotated[Literal['CENTER', 'MEDIAN', 'CURSOR', 'INDIVIDUAL_ORIGINS'], "is_animatable=False"]:
        """Rotation or scaling pivot point"""
        ...
    @pivot_point.setter
    def pivot_point(self, value: Annotated[Literal['CENTER', 'MEDIAN', 'CURSOR', 'INDIVIDUAL_ORIGINS'], "is_animatable=False"]) -> None:
        ...