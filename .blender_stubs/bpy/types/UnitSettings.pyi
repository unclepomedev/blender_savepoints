# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UnitSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UnitSettings(bpy_struct):

    @property
    def system(self) -> Annotated[Literal['NONE', 'METRIC', 'IMPERIAL'], "is_animatable=False"]:
        """The unit system to use for user interface controls"""
        ...
    @system.setter
    def system(self, value: Annotated[Literal['NONE', 'METRIC', 'IMPERIAL'], "is_animatable=False"]) -> None:
        ...
    @property
    def system_rotation(self) -> Annotated[Literal['DEGREES', 'RADIANS'], "is_animatable=False"]:
        """Unit to use for displaying/editing rotation values"""
        ...
    @system_rotation.setter
    def system_rotation(self, value: Annotated[Literal['DEGREES', 'RADIANS'], "is_animatable=False"]) -> None:
        ...
    @property
    def scale_length(self) -> Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=6", "is_animatable=False"]:
        """Scale to use when converting between Blender units and dimensions. When working at microscopic or astronomical scale, a small or large unit scale respectively can be used to avoid numerical precision problems"""
        ...
    @scale_length.setter
    def scale_length(self, value: Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=6", "is_animatable=False"]) -> None:
        ...
    @property
    def use_separate(self) -> Annotated[bool, "is_animatable=False"]:
        """Display units in pairs (e.g. 1m 0cm)"""
        ...
    @use_separate.setter
    def use_separate(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def length_unit(self) -> Annotated[Literal['DEFAULT'], "is_animatable=False"]:
        """Unit that will be used to display length values"""
        ...
    @length_unit.setter
    def length_unit(self, value: Annotated[Literal['DEFAULT'], "is_animatable=False"]) -> None:
        ...
    @property
    def mass_unit(self) -> Annotated[Literal['DEFAULT'], "is_animatable=False"]:
        """Unit that will be used to display mass values"""
        ...
    @mass_unit.setter
    def mass_unit(self, value: Annotated[Literal['DEFAULT'], "is_animatable=False"]) -> None:
        ...
    @property
    def time_unit(self) -> Annotated[Literal['DEFAULT'], "is_animatable=False"]:
        """Unit that will be used to display time values"""
        ...
    @time_unit.setter
    def time_unit(self, value: Annotated[Literal['DEFAULT'], "is_animatable=False"]) -> None:
        ...
    @property
    def temperature_unit(self) -> Annotated[Literal['DEFAULT'], "is_animatable=False"]:
        """Unit that will be used to display temperature values"""
        ...
    @temperature_unit.setter
    def temperature_unit(self, value: Annotated[Literal['DEFAULT'], "is_animatable=False"]) -> None:
        ...