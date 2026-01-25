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
from .ParticleHairKey import ParticleHairKey
from .ParticleKey import ParticleKey
class Particle(bpy_struct):
    location: list[float]
    velocity: list[float]
    angular_velocity: list[float]
    rotation: list[float]
    prev_location: list[float]
    prev_velocity: list[float]
    prev_angular_velocity: list[float]
    prev_rotation: list[float]
    hair_keys: bpy_prop_collection['ParticleHairKey']
    particle_keys: bpy_prop_collection['ParticleKey']
    birth_time: float
    lifetime: float
    die_time: float
    size: float
    is_exist: bool
    is_visible: bool
    alive_state: str
    def uv_on_emitter(self, *args, **kwargs) -> Any: ...