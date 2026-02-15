# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .ShaderFx import ShaderFx
from .Object import Object
class ShaderFxSwirl(ShaderFx):
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
    radius: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Radius to apply"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]
    """Angle of rotation"""
    use_transparent: bool
    """Make image transparent outside of radius"""
    object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to determine center location"""