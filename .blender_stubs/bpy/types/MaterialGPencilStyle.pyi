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

    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:

        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def fill_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for filling region bounded by each stroke"""
        ...
    @fill_color.setter
    def fill_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mix_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for mixing with primary filling color"""
        ...
    @mix_color.setter
    def mix_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mix_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Mix Factor"""
        ...
    @mix_factor.setter
    def mix_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def mix_stroke_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Mix Stroke Factor"""
        ...
    @mix_stroke_factor.setter
    def mix_stroke_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def texture_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Texture Orientation Angle"""
        ...
    @texture_angle.setter
    def texture_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def texture_scale(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Scale Factor for Texture"""
        ...
    @texture_scale.setter
    def texture_scale(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]):
        ...
    @property
    def texture_offset(self) -> Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]:
        """Shift Texture in 2d Space"""
        ...
    @texture_offset.setter
    def texture_offset(self, value: Annotated[list[float], "subtype='COORDINATES'", "step=10.0", "precision=3"]):
        ...
    @property
    def pixel_size(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Texture Pixel Size factor along the stroke"""
        ...
    @pixel_size.setter
    def pixel_size(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def hide(self) -> bool:
        """Set color Visibility"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def lock(self) -> bool:
        """Protect color from further editing and/or frame changes"""
        ...
    @lock.setter
    def lock(self, value: bool):
        ...
    @property
    def ghost(self) -> bool:
        """Display strokes using this color when showing onion skins"""
        ...
    @ghost.setter
    def ghost(self, value: bool):
        ...
    @property
    def texture_clamp(self) -> bool:
        """Do not repeat texture and clamp to one instance only"""
        ...
    @texture_clamp.setter
    def texture_clamp(self, value: bool):
        ...
    @property
    def flip(self) -> bool:
        """Flip filling colors"""
        ...
    @flip.setter
    def flip(self, value: bool):
        ...
    @property
    def use_overlap_strokes(self) -> bool:
        """Disable stencil and overlap self intersections with alpha materials"""
        ...
    @use_overlap_strokes.setter
    def use_overlap_strokes(self, value: bool):
        ...
    @property
    def use_stroke_holdout(self) -> bool:
        """Remove the color from underneath this stroke by using it as a mask"""
        ...
    @use_stroke_holdout.setter
    def use_stroke_holdout(self, value: bool):
        ...
    @property
    def use_fill_holdout(self) -> bool:
        """Remove the color from underneath this stroke by using it as a mask"""
        ...
    @use_fill_holdout.setter
    def use_fill_holdout(self, value: bool):
        ...
    @property
    def show_stroke(self) -> bool:
        """Show stroke lines of this material"""
        ...
    @show_stroke.setter
    def show_stroke(self, value: bool):
        ...
    @property
    def show_fill(self) -> bool:
        """Show stroke fills of this material"""
        ...
    @show_fill.setter
    def show_fill(self, value: bool):
        ...
    @property
    def alignment_mode(self) -> Literal['PATH', 'OBJECT', 'FIXED']:
        """Defines how align Dots and Boxes with drawing path and object rotation"""
        ...
    @alignment_mode.setter
    def alignment_mode(self, value: Literal['PATH', 'OBJECT', 'FIXED']):
        ...
    @property
    def alignment_rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Additional rotation applied to dots and square texture of strokes. Only applies in texture shading mode."""
        ...
    @alignment_rotation.setter
    def alignment_rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def pass_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index number for the "Color Index" pass"""
        ...
    @pass_index.setter
    def pass_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def mode(self) -> Literal['LINE', 'DOTS', 'BOX']:
        """Select line type for strokes"""
        ...
    @mode.setter
    def mode(self, value: Literal['LINE', 'DOTS', 'BOX']):
        ...
    @property
    def stroke_style(self) -> Literal['SOLID', 'TEXTURE']:
        """Select style used to draw strokes"""
        ...
    @stroke_style.setter
    def stroke_style(self, value: Literal['SOLID', 'TEXTURE']):
        ...
    @property
    def stroke_image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:

        ...
    @stroke_image.setter
    def stroke_image(self, value: Annotated[Optional['Image'], "is_animatable=False"]):
        ...
    @property
    def fill_style(self) -> Literal['SOLID', 'GRADIENT', 'TEXTURE']:
        """Select style used to fill strokes"""
        ...
    @fill_style.setter
    def fill_style(self, value: Literal['SOLID', 'GRADIENT', 'TEXTURE']):
        ...
    @property
    def gradient_type(self) -> Literal['LINEAR', 'RADIAL']:
        """Select type of gradient used to fill strokes"""
        ...
    @gradient_type.setter
    def gradient_type(self, value: Literal['LINEAR', 'RADIAL']):
        ...
    @property
    def fill_image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:

        ...
    @fill_image.setter
    def fill_image(self, value: Annotated[Optional['Image'], "is_animatable=False"]):
        ...
    @property
    def is_stroke_visible(self) -> bool:
        """True when opacity of stroke is set high enough to be visible"""
        ...
    @property
    def is_fill_visible(self) -> bool:
        """True when opacity of fill is set high enough to be visible"""
        ...