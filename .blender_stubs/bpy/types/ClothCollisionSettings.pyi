# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ClothCollisionSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection

class ClothCollisionSettings(bpy_struct):

    @property
    def use_collision(self) -> bool:
        """Enable collisions with other objects"""
        ...
    @use_collision.setter
    def use_collision(self, value: bool):
        ...
    @property
    def distance_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Minimum distance between collision objects before collision response takes effect"""
        ...
    @distance_min.setter
    def distance_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Friction force if a collision happened (higher = less movement)"""
        ...
    @friction.setter
    def friction(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of velocity lost on collision"""
        ...
    @damping.setter
    def damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def collision_quality(self) -> Annotated[int, "step=1"]:
        """How many collision iterations should be done (higher is better quality but slower)"""
        ...
    @collision_quality.setter
    def collision_quality(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def impulse_clamp(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Clamp collision impulses to avoid instability (0.0 to disable clamping)"""
        ...
    @impulse_clamp.setter
    def impulse_clamp(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_self_collision(self) -> bool:
        """Enable self collisions"""
        ...
    @use_self_collision.setter
    def use_self_collision(self, value: bool):
        ...
    @property
    def self_distance_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Minimum distance between cloth faces before collision response takes effect"""
        ...
    @self_distance_min.setter
    def self_distance_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def self_friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Friction with self contact"""
        ...
    @self_friction.setter
    def self_friction(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit colliders to this Collection"""
        ...
    @collection.setter
    def collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]):
        ...
    @property
    def vertex_group_self_collisions(self) -> Annotated[str, "is_animatable=False"]:
        """Triangles with all vertices in this group are not used during self collisions"""
        ...
    @vertex_group_self_collisions.setter
    def vertex_group_self_collisions(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def vertex_group_object_collisions(self) -> Annotated[str, "is_animatable=False"]:
        """Triangles with all vertices in this group are not used during object collisions"""
        ...
    @vertex_group_object_collisions.setter
    def vertex_group_object_collisions(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def self_impulse_clamp(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Clamp collision impulses to avoid instability (0.0 to disable clamping)"""
        ...
    @self_impulse_clamp.setter
    def self_impulse_clamp(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...