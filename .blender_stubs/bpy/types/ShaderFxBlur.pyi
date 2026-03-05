# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxBlur.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxBlur(ShaderFx):

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
    def size(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Factor of Blur"""
        ...
    @size.setter
    def size(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def samples(self) -> Annotated[int, "step=2"]:
        """Number of Blur Samples (zero, disable blur)"""
        ...
    @samples.setter
    def samples(self, value: Annotated[int, "step=2"]):
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation of the effect"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_dof_mode(self) -> bool:
        """Blur using camera depth of field"""
        ...
    @use_dof_mode.setter
    def use_dof_mode(self, value: bool):
        ...