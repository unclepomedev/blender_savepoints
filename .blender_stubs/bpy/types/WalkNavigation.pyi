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
class WalkNavigation(bpy_struct):
    mouse_speed: Annotated[float, "step=10.0", "precision=3"]
    """Speed factor for when looking around, high values mean faster mouse movement"""
    walk_speed: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Base speed for walking and flying"""
    walk_speed_factor: Annotated[float, "step=10.0", "precision=3"]
    """Multiplication factor when using the fast or slow modifiers"""
    view_height: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]
    """View distance from the floor when walking"""
    jump_height: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]
    """Maximum height of a jump"""
    teleport_time: Annotated[float, "step=10.0", "precision=3"]
    """Interval of time warp when teleporting in navigation mode"""
    use_gravity: bool
    """Walk with gravity, or free navigate"""
    use_mouse_reverse: bool
    """Reverse the vertical movement of the mouse"""