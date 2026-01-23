# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ParticleSystem import ParticleSystem
from .Texture import Texture
class FluidFlowSettings(bpy_struct):
    density: float
    smoke_color: float
    fuel_amount: float
    temperature: float
    particle_system: 'ParticleSystem'
    flow_type: str
    flow_behavior: str
    flow_source: str
    use_absolute: bool
    use_initial_velocity: bool
    velocity_factor: float
    velocity_normal: float
    velocity_random: float
    velocity_coord: float
    volume_density: float
    surface_distance: float
    use_plane_init: bool
    particle_size: float
    use_particle_size: bool
    use_inflow: bool
    subframes: int
    density_vertex_group: str
    use_texture: bool
    texture_map_type: str
    uv_layer: str
    noise_texture: 'Texture'
    texture_size: float
    texture_offset: float