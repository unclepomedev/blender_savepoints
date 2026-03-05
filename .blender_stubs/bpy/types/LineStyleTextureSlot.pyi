# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleTextureSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .TextureSlot import TextureSlot
from .Texture import Texture

class LineStyleTextureSlot(TextureSlot):

    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Texture data-block used by this texture slot"""
        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Texture slot name"""
        ...
    @property
    def offset(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]:
        """Fine tune of the texture mapping X, Y and Z locations"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]:
        """Set scaling for the texture's X, Y and Z sizes"""
        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Default color for textures that don't return RGB or when RGB to intensity is enabled"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_type(self) -> Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']:
        """Mode used to apply the texture"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']) -> None:
        ...
    @property
    def default_value(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard"""
        ...
    @default_value.setter
    def default_value(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def output_node(self) -> Literal['DEFAULT']:
        """Which output node to use, for node-based textures"""
        ...
    @output_node.setter
    def output_node(self, value: Literal['DEFAULT']) -> None:
        ...
    @property
    def mapping_x(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_x.setter
    def mapping_x(self, value: Literal['NONE', 'X', 'Y', 'Z']) -> None:
        ...
    @property
    def mapping_y(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_y.setter
    def mapping_y(self, value: Literal['NONE', 'X', 'Y', 'Z']) -> None:
        ...
    @property
    def mapping_z(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_z.setter
    def mapping_z(self, value: Literal['NONE', 'X', 'Y', 'Z']) -> None:
        ...
    @property
    def mapping(self) -> Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']:

        ...
    @mapping.setter
    def mapping(self, value: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']) -> None:
        ...
    @property
    def use_map_color_diffuse(self) -> bool:
        """The texture affects basic color of the stroke"""
        ...
    @use_map_color_diffuse.setter
    def use_map_color_diffuse(self, value: bool) -> None:
        ...
    @property
    def use_map_alpha(self) -> bool:
        """The texture affects the alpha value"""
        ...
    @use_map_alpha.setter
    def use_map_alpha(self, value: bool) -> None:
        ...
    @property
    def texture_coords(self) -> Literal['WINDOW', 'GLOBAL', 'ALONG_STROKE', 'ORCO']:
        """Texture coordinates used to map the texture onto the background"""
        ...
    @texture_coords.setter
    def texture_coords(self, value: Literal['WINDOW', 'GLOBAL', 'ALONG_STROKE', 'ORCO']) -> None:
        ...
    @property
    def alpha_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects alpha"""
        ...
    @alpha_factor.setter
    def alpha_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def diffuse_color_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects diffuse color"""
        ...
    @diffuse_color_factor.setter
    def diffuse_color_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...