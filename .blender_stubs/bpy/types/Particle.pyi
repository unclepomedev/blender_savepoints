# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Particle.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ParticleHairKey import ParticleHairKey
from .ParticleKey import ParticleKey
from .bpy_prop_collection import bpy_prop_collection

class Particle(bpy_struct):

    location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]

    velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]

    angular_velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]

    rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]

    prev_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]

    prev_velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]

    prev_angular_velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]

    prev_rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]

    @property
    def hair_keys(self) -> Annotated[bpy_prop_collection['ParticleHairKey'], "is_animatable=False"]:

        ...
    @property
    def particle_keys(self) -> Annotated[bpy_prop_collection['ParticleKey'], "is_animatable=False"]:

        ...
    birth_time: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]

    lifetime: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]

    die_time: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]

    size: Annotated[float, "step=10.0", "precision=3"]

    @property
    def is_exist(self) -> bool:

        ...
    @property
    def is_visible(self) -> bool:

        ...
    alive_state: Literal['DEAD', 'UNBORN', 'ALIVE', 'DYING']

    def uv_on_emitter(self, *args, **kwargs) -> Any: ...