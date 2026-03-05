# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WorldMistSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class WorldMistSettings(bpy_struct):

    @property
    def use_mist(self) -> bool:
        """Occlude objects with the environment color as they are further away"""
        ...
    @use_mist.setter
    def use_mist(self, value: bool):
        ...
    @property
    def intensity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Overall minimum intensity of the mist effect"""
        ...
    @intensity.setter
    def intensity(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Starting distance of the mist, measured from the camera"""
        ...
    @start.setter
    def start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]):
        ...
    @property
    def depth(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Distance over which the mist effect fades in"""
        ...
    @depth.setter
    def depth(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]):
        ...
    @property
    def height(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Control how much mist density decreases with height"""
        ...
    @height.setter
    def height(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def falloff(self) -> Literal['QUADRATIC', 'LINEAR', 'INVERSE_QUADRATIC']:
        """Type of transition used to fade mist"""
        ...
    @falloff.setter
    def falloff(self, value: Literal['QUADRATIC', 'LINEAR', 'INVERSE_QUADRATIC']):
        ...