# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxRim.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxRim(ShaderFx):

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
    offset: Annotated[list[int], "subtype='PIXEL'", "step=1"]
    """Offset of the rim"""
    rim_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color used for Rim"""
    mask_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color that must be kept"""
    mode: Literal['NORMAL', 'OVERLAY', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']
    """Blend mode"""
    blur: Annotated[list[int], "subtype='PIXEL'", "step=1"]
    """Number of pixels for blurring rim (set to 0 to disable)"""
    samples: Annotated[int, "step=2"]
    """Number of Blur Samples (zero, disable blur)"""