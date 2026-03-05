# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrNavigation.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class XrNavigation(bpy_struct):

    @property
    def vignette_intensity(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=1000.0", "precision=0"]:
        """Intensity of vignette that appears when moving"""
        ...
    @vignette_intensity.setter
    def vignette_intensity(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=1000.0", "precision=0"]) -> None:
        ...
    @property
    def turn_speed(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]:
        """Turn speed in degrees per second"""
        ...
    @turn_speed.setter
    def turn_speed(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]) -> None:
        ...
    @property
    def turn_amount(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]:
        """Amount in degrees per turn when using snap turn"""
        ...
    @turn_amount.setter
    def turn_amount(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]) -> None:
        ...
    @property
    def snap_turn(self) -> bool:
        """Instantly rotates the camera by a fixed angle instead of smoothly turning"""
        ...
    @snap_turn.setter
    def snap_turn(self, value: bool) -> None:
        ...
    @property
    def invert_rotation(self) -> bool:
        """Reverses the direction of rotation input"""
        ...
    @invert_rotation.setter
    def invert_rotation(self, value: bool) -> None:
        ...