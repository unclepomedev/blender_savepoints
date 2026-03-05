# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WalkNavigation.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class WalkNavigation(bpy_struct):

    @property
    def mouse_speed(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Speed factor for when looking around, high values mean faster mouse movement"""
        ...
    @mouse_speed.setter
    def mouse_speed(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def walk_speed(self) -> Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Base speed for walking and flying"""
        ...
    @walk_speed.setter
    def walk_speed(self, value: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]):
        ...
    @property
    def walk_speed_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Multiplication factor when using the fast or slow modifiers"""
        ...
    @walk_speed_factor.setter
    def walk_speed_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def view_height(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]:
        """View distance from the floor when walking"""
        ...
    @view_height.setter
    def view_height(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def jump_height(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]:
        """Maximum height of a jump"""
        ...
    @jump_height.setter
    def jump_height(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def teleport_time(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Interval of time warp when teleporting in navigation mode"""
        ...
    @teleport_time.setter
    def teleport_time(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_gravity(self) -> bool:
        """Walk with gravity, or free navigate"""
        ...
    @use_gravity.setter
    def use_gravity(self, value: bool):
        ...
    @property
    def use_mouse_reverse(self) -> bool:
        """Reverse the vertical movement of the mouse"""
        ...
    @use_mouse_reverse.setter
    def use_mouse_reverse(self, value: bool):
        ...