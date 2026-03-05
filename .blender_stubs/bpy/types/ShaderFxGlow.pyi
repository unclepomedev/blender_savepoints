# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxGlow.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxGlow(ShaderFx):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Effect name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['FX_BLUR', 'FX_COLORIZE', 'FX_FLIP', 'FX_GLOW', 'FX_PIXEL', 'FX_RIM', 'FX_SHADOW', 'FX_SWIRL', 'FX_WAVE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display effect in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool) -> None:
        ...
    @property
    def show_render(self) -> bool:
        """Use effect during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool) -> None:
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display effect in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Set effect expansion in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def glow_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color used for generated glow"""
        ...
    @glow_color.setter
    def glow_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Effect Opacity"""
        ...
    @opacity.setter
    def opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def select_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color selected to apply glow"""
        ...
    @select_color.setter
    def select_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mode(self) -> Literal['LUMINANCE', 'COLOR']:
        """Glow mode"""
        ...
    @mode.setter
    def mode(self, value: Literal['LUMINANCE', 'COLOR']) -> None:
        ...
    @property
    def threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Limit to select color for glow effect"""
        ...
    @threshold.setter
    def threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def size(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Size of the effect"""
        ...
    @size.setter
    def size(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def samples(self) -> Annotated[int, "step=2"]:
        """Number of Blur Samples"""
        ...
    @samples.setter
    def samples(self, value: Annotated[int, "step=2"]) -> None:
        ...
    @property
    def use_glow_under(self) -> bool:
        """Glow only areas with alpha (not supported with Regular blend mode)"""
        ...
    @use_glow_under.setter
    def use_glow_under(self, value: bool) -> None:
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation of the effect"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_mode(self) -> Literal['REGULAR', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']:
        """Blend mode"""
        ...
    @blend_mode.setter
    def blend_mode(self, value: Literal['REGULAR', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']) -> None:
        ...