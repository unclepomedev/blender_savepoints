# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeFontStyle.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeFontStyle(bpy_struct):

    @property
    def points(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=1"]:
        """Font size in points"""
        ...
    @points.setter
    def points(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=1"]) -> None:
        ...
    @property
    def character_weight(self) -> Annotated[int, "step=50"]:
        """Weight of the characters. 100-900, 400 is normal."""
        ...
    @character_weight.setter
    def character_weight(self, value: Annotated[int, "step=50"]) -> None:
        ...
    @property
    def shadow(self) -> Annotated[int, "step=1"]:
        """Shadow type (0 none, 3, 5 blur, 6 outline)"""
        ...
    @shadow.setter
    def shadow(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def shadow_offset_x(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Shadow offset in pixels"""
        ...
    @shadow_offset_x.setter
    def shadow_offset_x(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def shadow_offset_y(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Shadow offset in pixels"""
        ...
    @shadow_offset_y.setter
    def shadow_offset_y(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def shadow_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:

        ...
    @shadow_alpha.setter
    def shadow_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def shadow_value(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Shadow color in gray value"""
        ...
    @shadow_value.setter
    def shadow_value(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...