# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxGlow.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxGlow(ShaderFx):

    name: Annotated[str, "is_animatable=False"]
    """Effect name"""
    @property
    def type(self) -> Literal['FX_BLUR', 'FX_COLORIZE', 'FX_FLIP', 'FX_GLOW', 'FX_PIXEL', 'FX_RIM', 'FX_SHADOW', 'FX_SWIRL', 'FX_WAVE']:

        ...
    show_viewport: bool
    """Display effect in viewport"""
    show_render: bool
    """Use effect during render"""
    show_in_editmode: bool
    """Display effect in Edit mode"""
    show_expanded: bool
    """Set effect expansion in the user interface"""
    glow_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color used for generated glow"""
    opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Effect Opacity"""
    select_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color selected to apply glow"""
    mode: Literal['LUMINANCE', 'COLOR']
    """Glow mode"""
    threshold: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Limit to select color for glow effect"""
    size: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Size of the effect"""
    samples: Annotated[int, "step=2"]
    """Number of Blur Samples"""
    use_glow_under: bool
    """Glow only areas with alpha (not supported with Regular blend mode)"""
    rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation of the effect"""
    blend_mode: Literal['REGULAR', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']
    """Blend mode"""