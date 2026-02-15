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
    interpolation: Literal['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT']
    """Set interpolation between color stops"""
    hue_interpolation: Literal['NEAR', 'FAR', 'CW', 'CCW']
    """Set color interpolation"""
    color_mode: Literal['RGB', 'HSV', 'HSL']
    """Set color mode to use for interpolation"""
    def evaluate(self, *args, **kwargs) -> Any: ...