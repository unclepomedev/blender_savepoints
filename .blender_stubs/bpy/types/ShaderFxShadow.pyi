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
class ShaderFxShadow(ShaderFx):
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
    object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to determine center of rotation"""
    offset: Annotated[list[int], "subtype='PIXEL'", "step=1"]
    """Offset of the shadow"""
    scale: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Scale of the shadow"""
    shadow_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color used for Shadow"""
    orientation: Literal['HORIZONTAL', 'VERTICAL']
    """Direction of the wave"""
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of Wave"""
    period: Annotated[float, "step=10.0", "precision=3"]
    """Period of Wave"""
    phase: Annotated[float, "step=10.0", "precision=3"]
    """Phase Shift of Wave"""
    rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=5.0", "precision=2"]
    """Rotation around center or object"""
    blur: Annotated[list[int], "subtype='PIXEL'", "step=1"]
    """Number of pixels for blurring shadow (set to 0 to disable)"""
    samples: Annotated[int, "step=2"]
    """Number of Blur Samples (zero, disable blur)"""
    use_object: bool
    """Use object as center of rotation"""
    use_wave: bool
    """Use wave effect"""