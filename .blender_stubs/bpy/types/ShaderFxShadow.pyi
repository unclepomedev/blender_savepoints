# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxShadow.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx
from .Object import Object

class ShaderFxShadow(ShaderFx):

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
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to determine center of rotation"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def offset(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Offset of the shadow"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[int], "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Scale of the shadow"""
        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def shadow_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color used for Shadow"""
        ...
    @shadow_color.setter
    def shadow_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def orientation(self) -> Literal['HORIZONTAL', 'VERTICAL']:
        """Direction of the wave"""
        ...
    @orientation.setter
    def orientation(self, value: Literal['HORIZONTAL', 'VERTICAL']) -> None:
        ...
    @property
    def amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amplitude of Wave"""
        ...
    @amplitude.setter
    def amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def period(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Period of Wave"""
        ...
    @period.setter
    def period(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def phase(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Phase Shift of Wave"""
        ...
    @phase.setter
    def phase(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]:
        """Rotation around center or object"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]) -> None:
        ...
    @property
    def blur(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1"]:
        """Number of pixels for blurring shadow (set to 0 to disable)"""
        ...
    @blur.setter
    def blur(self, value: Annotated[list[int], "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def samples(self) -> Annotated[int, "step=2"]:
        """Number of Blur Samples (zero, disable blur)"""
        ...
    @samples.setter
    def samples(self, value: Annotated[int, "step=2"]) -> None:
        ...
    @property
    def use_object(self) -> bool:
        """Use object as center of rotation"""
        ...
    @use_object.setter
    def use_object(self, value: bool) -> None:
        ...
    @property
    def use_wave(self) -> bool:
        """Use wave effect"""
        ...
    @use_wave.setter
    def use_wave(self, value: bool) -> None:
        ...