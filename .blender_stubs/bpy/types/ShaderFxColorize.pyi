# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxColorize.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxColorize(ShaderFx):

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
    factor: Annotated[float, "step=10.0", "precision=3"]
    """Mix factor"""
    low_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """First color used for effect"""
    high_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Second color used for effect"""
    mode: Literal['GRAYSCALE', 'SEPIA', 'DUOTONE', 'TRANSPARENT', 'CUSTOM']
    """Effect mode"""