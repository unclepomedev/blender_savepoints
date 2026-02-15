# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .TextureSlot import TextureSlot
from .Texture import Texture
class BrushTextureSlot(TextureSlot):
    texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Texture data-block used by this texture slot"""
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Texture slot name"""
        ...
    offset: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]
    """Fine tune of the texture mapping X, Y and Z locations"""
    scale: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]
    """Set scaling for the texture's X, Y and Z sizes"""
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Default color for textures that don't return RGB or when RGB to intensity is enabled"""
    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
    """Mode used to apply the texture"""
    default_value: Annotated[float, "step=10.0", "precision=3"]
    """Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard"""
    output_node: Literal['DEFAULT']
    """Which output node to use, for node-based textures"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Brush texture rotation"""
    map_mode: Literal['VIEW_PLANE', 'AREA_PLANE', 'TILED', '3D', 'RANDOM', 'STENCIL']
    mask_map_mode: Literal['VIEW_PLANE', 'TILED', 'RANDOM', 'STENCIL']
    use_rake: bool
    use_random: bool
    random_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Brush texture random angle"""
    @property
    def has_texture_angle_source(self) -> bool:
        ...
    @property
    def has_random_texture_angle(self) -> bool:
        ...
    @property
    def has_texture_angle(self) -> bool:
        ...