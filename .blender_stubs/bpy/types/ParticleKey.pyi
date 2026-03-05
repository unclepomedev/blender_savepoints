# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleKey.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ParticleKey(bpy_struct):

    @property
    def location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Key location"""
        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Key velocity"""
        ...
    @velocity.setter
    def velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]):
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:
        """Key rotation quaternion"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]):
        ...
    @property
    def angular_velocity(self) -> Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Key angular velocity"""
        ...
    @angular_velocity.setter
    def angular_velocity(self, value: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]):
        ...
    @property
    def time(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Time of key over the simulation"""
        ...
    @time.setter
    def time(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...