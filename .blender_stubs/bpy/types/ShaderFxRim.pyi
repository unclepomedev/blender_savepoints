# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxRim.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxRim(ShaderFx):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Effect name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['FX_BLUR', 'FX_COLORIZE', 'FX_FLIP', 'FX_GLOW', 'FX_PIXEL', 'FX_RIM', 'FX_SHADOW', 'FX_SWIRL', 'FX_WAVE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display effect in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool):
        ...
    @property
    def show_render(self) -> bool:
        """Use effect during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool):
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display effect in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Set effect expansion in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def offset(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Offset of the rim"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[int], "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def rim_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color used for Rim"""
        ...
    @rim_color.setter
    def rim_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mask_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color that must be kept"""
        ...
    @mask_color.setter
    def mask_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mode(self) -> Literal['NORMAL', 'OVERLAY', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']:
        """Blend mode"""
        ...
    @mode.setter
    def mode(self, value: Literal['NORMAL', 'OVERLAY', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']):
        ...
    @property
    def blur(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Number of pixels for blurring rim (set to 0 to disable)"""
        ...
    @blur.setter
    def blur(self, value: Annotated[list[int], "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def samples(self) -> Annotated[int, "step=2"]:
        """Number of Blur Samples (zero, disable blur)"""
        ...
    @samples.setter
    def samples(self, value: Annotated[int, "step=2"]):
        ...