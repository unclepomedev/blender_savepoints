# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleTarget.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class ParticleTarget(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Particle target name"""
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """The object that has the target particle system (empty if same object)"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def system(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """The index of particle system on the target object"""
        ...
    @system.setter
    def system(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:

        ...
    @time.setter
    def time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def duration(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @duration.setter
    def duration(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def is_valid(self) -> Annotated[bool, "is_animatable=False"]:
        """Keyed particles target is valid"""
        ...
    @is_valid.setter
    def is_valid(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def alliance(self) -> Annotated[Literal['FRIEND', 'NEUTRAL', 'ENEMY'], "is_animatable=False"]:

        ...
    @alliance.setter
    def alliance(self, value: Annotated[Literal['FRIEND', 'NEUTRAL', 'ENEMY'], "is_animatable=False"]):
        ...