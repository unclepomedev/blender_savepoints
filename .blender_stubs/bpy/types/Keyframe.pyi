# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Keyframe.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Keyframe(bpy_struct):

    @property
    def select_left_handle(self) -> bool:
        """Left handle selection status"""
        ...
    @select_left_handle.setter
    def select_left_handle(self, value: bool) -> None:
        ...
    @property
    def select_right_handle(self) -> bool:
        """Right handle selection status"""
        ...
    @select_right_handle.setter
    def select_right_handle(self, value: bool) -> None:
        ...
    @property
    def select_control_point(self) -> bool:
        """Control point selection status"""
        ...
    @select_control_point.setter
    def select_control_point(self, value: bool) -> None:
        ...
    @property
    def handle_left_type(self) -> Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']:
        """Handle types"""
        ...
    @handle_left_type.setter
    def handle_left_type(self, value: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']) -> None:
        ...
    @property
    def handle_right_type(self) -> Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']:
        """Handle types"""
        ...
    @handle_right_type.setter
    def handle_right_type(self, value: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']) -> None:
        ...
    @property
    def interpolation(self) -> Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']:
        """Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe"""
        ...
    @interpolation.setter
    def interpolation(self, value: Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']) -> None:
        ...
    @property
    def type(self) -> Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED']:
        """Type of keyframe (for visual purposes only)"""
        ...
    @type.setter
    def type(self, value: Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED']) -> None:
        ...
    @property
    def easing(self) -> Literal['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT']:
        """Which ends of the segment between this and the next keyframe easing interpolation is applied to"""
        ...
    @easing.setter
    def easing(self, value: Literal['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT']) -> None:
        ...
    @property
    def back(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of overshoot for 'back' easing"""
        ...
    @back.setter
    def back(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount to boost elastic bounces for 'elastic' easing"""
        ...
    @amplitude.setter
    def amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def period(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time between bounces for elastic easing"""
        ...
    @period.setter
    def period(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def handle_left(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Coordinates of the left handle (before the control point)"""
        ...
    @handle_left.setter
    def handle_left(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Coordinates of the control point"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def co_ui(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Coordinates of the control point. Note: Changing this value also updates the handles similar to using the graph editor transform operator"""
        ...
    @co_ui.setter
    def co_ui(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def handle_right(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Coordinates of the right handle (after the control point)"""
        ...
    @handle_right.setter
    def handle_right(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]) -> None:
        ...