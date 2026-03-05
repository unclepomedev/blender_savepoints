# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxSwirl.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx
from .Object import Object

class ShaderFxSwirl(ShaderFx):

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
    def radius(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Radius to apply"""
        ...
    @radius.setter
    def radius(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]):
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]:
        """Angle of rotation"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]):
        ...
    @property
    def use_transparent(self) -> bool:
        """Make image transparent outside of radius"""
        ...
    @use_transparent.setter
    def use_transparent(self, value: bool):
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to determine center location"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...