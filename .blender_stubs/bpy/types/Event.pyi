# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .NDOFMotionEventData import NDOFMotionEventData
from .XrEventData import XrEventData
class Event(bpy_struct):
    ascii: str
    unicode: str
    value: str
    value_prev: str
    type: str
    type_prev: str
    direction: str
    is_repeat: bool
    is_consecutive: bool
    mouse_x: int
    mouse_y: int
    mouse_region_x: int
    mouse_region_y: int
    mouse_prev_x: int
    mouse_prev_y: int
    mouse_prev_press_x: int
    mouse_prev_press_y: int
    pressure: float
    tilt: float
    is_tablet: bool
    is_mouse_absolute: bool
    ndof_motion: 'NDOFMotionEventData'
    xr: 'XrEventData'
    shift: bool
    ctrl: bool
    alt: bool
    oskey: bool
    hyper: bool