# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ColorRamp.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ColorRampElement import ColorRampElement
from .ColorRampElements import ColorRampElements
from .bpy_prop_collection import bpy_prop_collection

class ColorRamp(bpy_struct):

    @property
    def elements(self) -> Annotated['ColorRampElements', "subtype='COLOR'", "is_animatable=False"]:

        ...
    @property
    def interpolation(self) -> Literal['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT']:
        """Set interpolation between color stops"""
        ...
    @interpolation.setter
    def interpolation(self, value: Literal['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT']) -> None:
        ...
    @property
    def hue_interpolation(self) -> Literal['NEAR', 'FAR', 'CW', 'CCW']:
        """Set color interpolation"""
        ...
    @hue_interpolation.setter
    def hue_interpolation(self, value: Literal['NEAR', 'FAR', 'CW', 'CCW']) -> None:
        ...
    @property
    def color_mode(self) -> Literal['RGB', 'HSV', 'HSL']:
        """Set color mode to use for interpolation"""
        ...
    @color_mode.setter
    def color_mode(self, value: Literal['RGB', 'HSV', 'HSL']) -> None:
        ...
    def evaluate(self, *args, **kwargs) -> Any: ...