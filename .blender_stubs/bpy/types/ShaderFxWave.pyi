# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxWave.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxWave(ShaderFx):

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
    def orientation(self) -> Literal['HORIZONTAL', 'VERTICAL']:
        """Direction of the wave"""
        ...
    @orientation.setter
    def orientation(self, value: Literal['HORIZONTAL', 'VERTICAL']):
        ...
    @property
    def amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amplitude of Wave"""
        ...
    @amplitude.setter
    def amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def period(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Period of Wave"""
        ...
    @period.setter
    def period(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def phase(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Phase Shift of Wave"""
        ...
    @phase.setter
    def phase(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...