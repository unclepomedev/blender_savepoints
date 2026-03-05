# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ColorMapping.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ColorRamp import ColorRamp

class ColorMapping(bpy_struct):

    @property
    def use_color_ramp(self) -> bool:
        """Toggle color ramp operations"""
        ...
    @use_color_ramp.setter
    def use_color_ramp(self, value: bool) -> None:
        ...
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:

        ...
    @property
    def brightness(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the brightness of the texture"""
        ...
    @brightness.setter
    def brightness(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def contrast(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the contrast of the texture"""
        ...
    @contrast.setter
    def contrast(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def saturation(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Adjust the saturation of colors in the texture"""
        ...
    @saturation.setter
    def saturation(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def blend_type(self) -> Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']:
        """Mode used to mix with texture output color"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']) -> None:
        ...
    @property
    def blend_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Blend color to mix with texture output color"""
        ...
    @blend_color.setter
    def blend_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @blend_factor.setter
    def blend_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...