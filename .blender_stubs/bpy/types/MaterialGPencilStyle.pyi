# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaterialGPencilStyle.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Image import Image

class MaterialGPencilStyle(bpy_struct):

    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]

    fill_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for filling region bounded by each stroke"""
    mix_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for mixing with primary filling color"""
    mix_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Mix Factor"""
    mix_stroke_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Mix Stroke Factor"""
    texture_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Texture Orientation Angle"""
    texture_scale: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Scale Factor for Texture"""
    texture_offset: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]
    """Shift Texture in 2d Space"""
    pixel_size: Annotated[float, "step=10.0", "precision=3"]
    """Texture Pixel Size factor along the stroke"""
    hide: bool
    """Set color Visibility"""
    lock: bool
    """Protect color from further editing and/or frame changes"""
    ghost: bool
    """Display strokes using this color when showing onion skins"""
    texture_clamp: bool
    """Do not repeat texture and clamp to one instance only"""
    flip: bool
    """Flip filling colors"""
    use_overlap_strokes: bool
    """Disable stencil and overlap self intersections with alpha materials"""
    use_stroke_holdout: bool
    """Remove the color from underneath this stroke by using it as a mask"""
    use_fill_holdout: bool
    """Remove the color from underneath this stroke by using it as a mask"""
    show_stroke: bool
    """Show stroke lines of this material"""
    show_fill: bool
    """Show stroke fills of this material"""
    alignment_mode: Literal['PATH', 'OBJECT', 'FIXED']
    """Defines how align Dots and Boxes with drawing path and object rotation"""
    alignment_rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Additional rotation applied to dots and square texture of strokes. Only applies in texture shading mode."""
    pass_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index number for the "Color Index" pass"""
    mode: Literal['LINE', 'DOTS', 'BOX']
    """Select line type for strokes"""
    stroke_style: Literal['SOLID', 'TEXTURE']
    """Select style used to draw strokes"""
    stroke_image: Annotated[Optional['Image'], "is_animatable=False"]

    fill_style: Literal['SOLID', 'GRADIENT', 'TEXTURE']
    """Select style used to fill strokes"""
    gradient_type: Literal['LINEAR', 'RADIAL']
    """Select type of gradient used to fill strokes"""
    fill_image: Annotated[Optional['Image'], "is_animatable=False"]

    @property
    def is_stroke_visible(self) -> bool:
        """True when opacity of stroke is set high enough to be visible"""
        ...
    @property
    def is_fill_visible(self) -> bool:
        """True when opacity of fill is set high enough to be visible"""
        ...