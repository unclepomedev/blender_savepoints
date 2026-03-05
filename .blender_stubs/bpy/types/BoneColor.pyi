# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoneColor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeBoneColorSet import ThemeBoneColorSet

class BoneColor(bpy_struct):

    @property
    def palette(self) -> Annotated[Literal['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM'], "is_animatable=False"]:
        """Color palette to use"""
        ...
    @palette.setter
    def palette(self, value: Annotated[Literal['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM'], "is_animatable=False"]) -> None:
        ...
    @property
    def is_custom(self) -> bool:
        """A color palette is user-defined, instead of using a theme-defined one"""
        ...
    @property
    def custom(self) -> Annotated['ThemeBoneColorSet', "is_animatable=False"]:
        """The custom bone colors, used when palette is 'CUSTOM'"""
        ...