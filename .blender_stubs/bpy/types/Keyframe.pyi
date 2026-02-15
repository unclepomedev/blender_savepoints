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
class Keyframe(bpy_struct):
    select_left_handle: bool
    """Left handle selection status"""
    select_right_handle: bool
    """Right handle selection status"""
    select_control_point: bool
    """Control point selection status"""
    handle_left_type: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']
    """Handle types"""
    handle_right_type: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']
    """Handle types"""
    interpolation: Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']
    """Interpolation method to use for segment of the F-Curve from this Keyframe until the next Keyframe"""
    type: Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED']
    """Type of keyframe (for visual purposes only)"""
    easing: Literal['AUTO', 'EASE_IN', 'EASE_OUT', 'EASE_IN_OUT']
    """Which ends of the segment between this and the next keyframe easing interpolation is applied to"""
    back: Annotated[float, "step=10.0", "precision=3"]
    """Amount of overshoot for 'back' easing"""
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amount to boost elastic bounces for 'elastic' easing"""
    period: Annotated[float, "step=10.0", "precision=3"]
    """Time between bounces for elastic easing"""
    handle_left: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Coordinates of the left handle (before the control point)"""
    co: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Coordinates of the control point"""
    co_ui: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Coordinates of the control point. Note: Changing this value also updates the handles similar to using the graph editor transform operator"""
    handle_right: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Coordinates of the right handle (after the control point)"""