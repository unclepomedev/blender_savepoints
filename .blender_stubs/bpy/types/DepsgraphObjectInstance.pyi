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
from .Object import Object
from .ParticleSystem import ParticleSystem
class DepsgraphObjectInstance(bpy_struct):
    object: 'Object'
    show_self: bool
    show_particles: bool
    is_instance: bool
    instance_object: 'Object'
    parent: 'Object'
    particle_system: 'ParticleSystem'
    persistent_id: list[int]
    random_id: int
    matrix_world: list[float]
    orco: list[float]
    uv: list[float]