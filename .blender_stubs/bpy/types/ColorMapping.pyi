# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ColorRamp import ColorRamp
class ColorMapping(bpy_struct):
    use_color_ramp: bool
    """Toggle color ramp operations"""
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "subtype=''", "unit='MASS'", "is_animatable=False"]:
        ...
    brightness: Annotated[float, "step=1.0", "precision=3"]
    """Adjust the brightness of the texture"""
    contrast: Annotated[float, "step=1.0", "precision=3"]
    """Adjust the contrast of the texture"""
    saturation: Annotated[float, "step=1.0", "precision=3"]
    """Adjust the saturation of colors in the texture"""
    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
    """Mode used to mix with texture output color"""
    blend_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Blend color to mix with texture output color"""
    blend_factor: Annotated[float, "step=10.0", "precision=3"]