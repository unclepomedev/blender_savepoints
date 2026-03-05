# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleSettingsTextureSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .TextureSlot import TextureSlot
from .Object import Object
from .Texture import Texture

class ParticleSettingsTextureSlot(TextureSlot):

    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Texture data-block used by this texture slot"""
        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
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
    def offset(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]):
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]:
        """Set scaling for the texture's X, Y and Z sizes"""
        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Default color for textures that don't return RGB or when RGB to intensity is enabled"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def blend_type(self) -> Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']:
        """Mode used to apply the texture"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']):
        ...
    @property
    def default_value(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard"""
        ...
    @default_value.setter
    def default_value(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def output_node(self) -> Literal['DEFAULT']:
        """Which output node to use, for node-based textures"""
        ...
    @output_node.setter
    def output_node(self, value: Literal['DEFAULT']):
        ...
    @property
    def texture_coords(self) -> Literal['GLOBAL', 'OBJECT', 'UV', 'ORCO', 'STRAND']:
        """Texture coordinates used to map the texture onto the background"""
        ...
    @texture_coords.setter
    def texture_coords(self, value: Literal['GLOBAL', 'OBJECT', 'UV', 'ORCO', 'STRAND']):
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to use for mapping with Object texture coordinates"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map to use for mapping with UV texture coordinates"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def mapping_x(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_x.setter
    def mapping_x(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping_y(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_y.setter
    def mapping_y(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping_z(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_z.setter
    def mapping_z(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping(self) -> Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']:

        ...
    @mapping.setter
    def mapping(self, value: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']):
        ...
    @property
    def use_map_time(self) -> bool:
        """Affect the emission time of the particles"""
        ...
    @use_map_time.setter
    def use_map_time(self, value: bool):
        ...
    @property
    def use_map_life(self) -> bool:
        """Affect the life time of the particles"""
        ...
    @use_map_life.setter
    def use_map_life(self, value: bool):
        ...
    @property
    def use_map_density(self) -> bool:
        """Affect the density of the particles"""
        ...
    @use_map_density.setter
    def use_map_density(self, value: bool):
        ...
    @property
    def use_map_size(self) -> bool:
        """Affect the particle size"""
        ...
    @use_map_size.setter
    def use_map_size(self, value: bool):
        ...
    @property
    def use_map_velocity(self) -> bool:
        """Affect the particle initial velocity"""
        ...
    @use_map_velocity.setter
    def use_map_velocity(self, value: bool):
        ...
    @property
    def use_map_field(self) -> bool:
        """Affect the particle force fields"""
        ...
    @use_map_field.setter
    def use_map_field(self, value: bool):
        ...
    @property
    def use_map_gravity(self) -> bool:
        """Affect the particle gravity"""
        ...
    @use_map_gravity.setter
    def use_map_gravity(self, value: bool):
        ...
    @property
    def use_map_damp(self) -> bool:
        """Affect the particle velocity damping"""
        ...
    @use_map_damp.setter
    def use_map_damp(self, value: bool):
        ...
    @property
    def use_map_clump(self) -> bool:
        """Affect the child clumping"""
        ...
    @use_map_clump.setter
    def use_map_clump(self, value: bool):
        ...
    @property
    def use_map_kink_amp(self) -> bool:
        """Affect the child kink amplitude"""
        ...
    @use_map_kink_amp.setter
    def use_map_kink_amp(self, value: bool):
        ...
    @property
    def use_map_kink_freq(self) -> bool:
        """Affect the child kink frequency"""
        ...
    @use_map_kink_freq.setter
    def use_map_kink_freq(self, value: bool):
        ...
    @property
    def use_map_rough(self) -> bool:
        """Affect the child rough"""
        ...
    @use_map_rough.setter
    def use_map_rough(self, value: bool):
        ...
    @property
    def use_map_length(self) -> bool:
        """Affect the child hair length"""
        ...
    @use_map_length.setter
    def use_map_length(self, value: bool):
        ...
    @property
    def use_map_twist(self) -> bool:
        """Affect the child twist"""
        ...
    @use_map_twist.setter
    def use_map_twist(self, value: bool):
        ...
    @property
    def time_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle emission time"""
        ...
    @time_factor.setter
    def time_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def life_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle life time"""
        ...
    @life_factor.setter
    def life_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def density_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle density"""
        ...
    @density_factor.setter
    def density_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def size_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects physical particle size"""
        ...
    @size_factor.setter
    def size_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def velocity_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle initial velocity"""
        ...
    @velocity_factor.setter
    def velocity_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def field_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle force fields"""
        ...
    @field_factor.setter
    def field_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def gravity_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle gravity"""
        ...
    @gravity_factor.setter
    def gravity_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def damp_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects particle damping"""
        ...
    @damp_factor.setter
    def damp_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def length_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child hair length"""
        ...
    @length_factor.setter
    def length_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def clump_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child clump"""
        ...
    @clump_factor.setter
    def clump_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def kink_amp_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child kink amplitude"""
        ...
    @kink_amp_factor.setter
    def kink_amp_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def kink_freq_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child kink frequency"""
        ...
    @kink_freq_factor.setter
    def kink_freq_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def rough_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child roughness"""
        ...
    @rough_factor.setter
    def rough_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def twist_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount texture affects child twist"""
        ...
    @twist_factor.setter
    def twist_factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...