# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ColorManagedViewSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class ColorManagedViewSettings(bpy_struct):

    @property
    def look(self) -> Literal['NONE']:
        """Additional transform applied before view transform for artistic needs"""
        ...
    @look.setter
    def look(self, value: Literal['NONE']) -> None:
        ...
    @property
    def view_transform(self) -> Literal['NONE']:
        """View used when converting image to a display space"""
        ...
    @view_transform.setter
    def view_transform(self, value: Literal['NONE']) -> None:
        ...
    @property
    def exposure(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Exposure (stops) applied before display transform, multiplying by 2^exposure"""
        ...
    @exposure.setter
    def exposure(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def gamma(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Additional gamma encoding after display transform, for output with custom gamma"""
        ...
    @gamma.setter
    def gamma(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def curve_mapping(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Color curve mapping applied before display transform"""
        ...
    @property
    def use_curve_mapping(self) -> bool:
        """Use RGB curved for pre-display transformation"""
        ...
    @use_curve_mapping.setter
    def use_curve_mapping(self, value: bool) -> None:
        ...
    @property
    def use_white_balance(self) -> bool:
        """Perform chromatic adaption from a different white point"""
        ...
    @use_white_balance.setter
    def use_white_balance(self, value: bool) -> None:
        ...
    @property
    def white_balance_temperature(self) -> Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=100.0", "precision=0"]:
        """Color temperature of the scene's white point"""
        ...
    @white_balance_temperature.setter
    def white_balance_temperature(self, value: Annotated[float, "subtype='COLOR_TEMPERATURE'", "unit='COLOR_TEMPERATURE'", "step=100.0", "precision=0"]) -> None:
        ...
    @property
    def white_balance_tint(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=1"]:
        """Color tint of the scene's white point (the default of 10 matches daylight)"""
        ...
    @white_balance_tint.setter
    def white_balance_tint(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=1"]) -> None:
        ...
    @property
    def white_balance_whitepoint(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """The color which gets mapped to white (automatically converted to/from temperature and tint)"""
        ...
    @white_balance_whitepoint.setter
    def white_balance_whitepoint(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def is_hdr(self) -> bool:
        """The display and view transform supports high dynamic range colors"""
        ...
    @property
    def support_emulation(self) -> bool:
        """The display and view transform supports automatic emulation for another display device, using the display color spaces mechanism in OpenColorIO v2 configurations"""
        ...