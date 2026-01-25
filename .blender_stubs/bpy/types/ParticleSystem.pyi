# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ChildParticle import ChildParticle
from .ClothModifier import ClothModifier
from .Object import Object
from .Particle import Particle
from .ParticleSettings import ParticleSettings
from .ParticleTarget import ParticleTarget
from .PointCache import PointCache
class ParticleSystem(bpy_struct):
    name: str
    settings: 'ParticleSettings'
    particles: bpy_prop_collection['Particle']
    child_particles: bpy_prop_collection['ChildParticle']
    seed: int
    child_seed: int
    is_global_hair: bool
    use_hair_dynamics: bool
    cloth: 'ClothModifier'
    reactor_target_object: 'Object'
    reactor_target_particle_system: int
    use_keyed_timing: bool
    targets: bpy_prop_collection['ParticleTarget']
    active_particle_target: 'ParticleTarget'
    active_particle_target_index: int
    vertex_group_density: str
    invert_vertex_group_density: bool
    vertex_group_velocity: str
    invert_vertex_group_velocity: bool
    vertex_group_length: str
    invert_vertex_group_length: bool
    vertex_group_clump: str
    invert_vertex_group_clump: bool
    vertex_group_kink: str
    invert_vertex_group_kink: bool
    vertex_group_roughness_1: str
    invert_vertex_group_roughness_1: bool
    vertex_group_roughness_2: str
    invert_vertex_group_roughness_2: bool
    vertex_group_roughness_end: str
    invert_vertex_group_roughness_end: bool
    vertex_group_size: str
    invert_vertex_group_size: bool
    vertex_group_tangent: str
    invert_vertex_group_tangent: bool
    vertex_group_rotation: str
    invert_vertex_group_rotation: bool
    vertex_group_field: str
    invert_vertex_group_field: bool
    vertex_group_twist: str
    invert_vertex_group_twist: bool
    point_cache: 'PointCache'
    has_multiple_caches: bool
    parent: 'Object'
    is_editable: bool
    is_edited: bool
    dt_frac: float
    def co_hair(self, *args, **kwargs) -> Any: ...
    def uv_on_emitter(self, *args, **kwargs) -> Any: ...
    def mcol_on_emitter(self, *args, **kwargs) -> Any: ...