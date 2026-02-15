# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ShaderFxBlur.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ShaderFx import ShaderFx

class ShaderFxBlur(ShaderFx):

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
    size: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Factor of Blur"""
    samples: Annotated[int, "step=2"]
    """Number of Blur Samples (zero, disable blur)"""
    rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation of the effect"""
    use_dof_mode: bool
    """Blur using camera depth of field"""