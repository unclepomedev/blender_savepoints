# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .TextureSlot import TextureSlot
from .Object import Object
from .Texture import Texture
class ParticleSettingsTextureSlot(TextureSlot):
    texture: 'Texture'
    name: str
    offset: float
    scale: float
    color: float
    blend_type: str
    default_value: float
    output_node: str
    texture_coords: str
    object: 'Object'
    uv_layer: str
    mapping_x: str
    mapping_y: str
    mapping_z: str
    mapping: str
    use_map_time: bool
    use_map_life: bool
    use_map_density: bool
    use_map_size: bool
    use_map_velocity: bool
    use_map_field: bool
    use_map_gravity: bool
    use_map_damp: bool
    use_map_clump: bool
    use_map_kink_amp: bool
    use_map_kink_freq: bool
    use_map_rough: bool
    use_map_length: bool
    use_map_twist: bool
    time_factor: float
    life_factor: float
    density_factor: float
    size_factor: float
    velocity_factor: float
    field_factor: float
    gravity_factor: float
    damp_factor: float
    length_factor: float
    clump_factor: float
    kink_amp_factor: float
    kink_freq_factor: float
    rough_factor: float
    twist_factor: float