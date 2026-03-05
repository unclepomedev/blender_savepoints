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

    @property
    def location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:

        ...
    @velocity.setter
    def velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def angular_velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:

        ...
    @angular_velocity.setter
    def angular_velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:

        ...
    @rotation.setter
    def rotation(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def prev_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @prev_location.setter
    def prev_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def prev_velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:

        ...
    @prev_velocity.setter
    def prev_velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def prev_angular_velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:

        ...
    @prev_angular_velocity.setter
    def prev_angular_velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def prev_rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:

        ...
    @prev_rotation.setter
    def prev_rotation(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def hair_keys(self) -> Annotated[bpy_prop_collection['ParticleHairKey'], "is_animatable=False"]:

        ...
    @property
    def particle_keys(self) -> Annotated[bpy_prop_collection['ParticleKey'], "is_animatable=False"]:

        ...
    @property
    def birth_time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @birth_time.setter
    def birth_time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lifetime(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @lifetime.setter
    def lifetime(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def die_time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @die_time.setter
    def die_time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @size.setter
    def size(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def is_exist(self) -> bool:

        ...
    @property
    def is_visible(self) -> bool:

        ...
    @property
    def alive_state(self) -> Literal['DEAD', 'UNBORN', 'ALIVE', 'DYING']:

        ...
    @alive_state.setter
    def alive_state(self, value: Literal['DEAD', 'UNBORN', 'ALIVE', 'DYING']) -> None:
        ...
    def uv_on_emitter(self, *args, **kwargs) -> Any: ...