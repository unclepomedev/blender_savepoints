# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripColorBalance.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .StripColorBalanceData import StripColorBalanceData

class StripColorBalance(StripColorBalanceData):

    @property
    def correction_method(self) -> Literal['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE']:

        ...
    @correction_method.setter
    def correction_method(self, value: Literal['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE']):
        ...
    @property
    def lift(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Color balance lift (shadows)"""
        ...
    @lift.setter
    def lift(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def gamma(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Color balance gamma (midtones)"""
        ...
    @gamma.setter
    def gamma(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def gain(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Color balance gain (highlights)"""
        ...
    @gain.setter
    def gain(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def slope(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Correction for highlights"""
        ...
    @slope.setter
    def slope(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def offset(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Correction for entire tonal range"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def power(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]:
        """Correction for midtones"""
        ...
    @power.setter
    def power(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def invert_lift(self) -> bool:
        """Invert the lift color"""
        ...
    @invert_lift.setter
    def invert_lift(self, value: bool):
        ...
    @property
    def invert_gamma(self) -> bool:
        """Invert the gamma color"""
        ...
    @invert_gamma.setter
    def invert_gamma(self, value: bool):
        ...
    @property
    def invert_gain(self) -> bool:
        """Invert the gain color"""
        ...
    @invert_gain.setter
    def invert_gain(self, value: bool):
        ...
    @property
    def invert_slope(self) -> bool:
        """Invert the slope color"""
        ...
    @invert_slope.setter
    def invert_slope(self, value: bool):
        ...
    @property
    def invert_offset(self) -> bool:
        """Invert the offset color"""
        ...
    @invert_offset.setter
    def invert_offset(self, value: bool):
        ...
    @property
    def invert_power(self) -> bool:
        """Invert the power color"""
        ...
    @invert_power.setter
    def invert_power(self, value: bool):
        ...