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
from .Object import Object
from .Texture import Texture
class ParticleSettingsTextureSlot(TextureSlot):
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
    texture_coords: Literal['GLOBAL', 'OBJECT', 'UV', 'ORCO', 'STRAND']
    """Texture coordinates used to map the texture onto the background"""
    object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to use for mapping with Object texture coordinates"""
    uv_layer: Annotated[str, "is_animatable=False"]
    """UV map to use for mapping with UV texture coordinates"""
    mapping_x: Literal['NONE', 'X', 'Y', 'Z']
    mapping_y: Literal['NONE', 'X', 'Y', 'Z']
    mapping_z: Literal['NONE', 'X', 'Y', 'Z']
    mapping: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']
    use_map_time: bool
    """Affect the emission time of the particles"""
    use_map_life: bool
    """Affect the life time of the particles"""
    use_map_density: bool
    """Affect the density of the particles"""
    use_map_size: bool
    """Affect the particle size"""
    use_map_velocity: bool
    """Affect the particle initial velocity"""
    use_map_field: bool
    """Affect the particle force fields"""
    use_map_gravity: bool
    """Affect the particle gravity"""
    use_map_damp: bool
    """Affect the particle velocity damping"""
    use_map_clump: bool
    """Affect the child clumping"""
    use_map_kink_amp: bool
    """Affect the child kink amplitude"""
    use_map_kink_freq: bool
    """Affect the child kink frequency"""
    use_map_rough: bool
    """Affect the child rough"""
    use_map_length: bool
    """Affect the child hair length"""
    use_map_twist: bool
    """Affect the child twist"""
    time_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle emission time"""
    life_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle life time"""
    density_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle density"""
    size_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects physical particle size"""
    velocity_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle initial velocity"""
    field_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle force fields"""
    gravity_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle gravity"""
    damp_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects particle damping"""
    length_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child hair length"""
    clump_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child clump"""
    kink_amp_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child kink amplitude"""
    kink_freq_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child kink frequency"""
    rough_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child roughness"""
    twist_factor: Annotated[float, "step=10.0", "precision=3"]
    """Amount texture affects child twist"""