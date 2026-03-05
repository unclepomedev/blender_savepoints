# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CollisionSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class CollisionSettings(bpy_struct):

    @property
    def use(self) -> bool:
        """Enable this object as a collider for physics systems"""
        ...
    @use.setter
    def use(self, value: bool):
        ...
    @property
    def damping_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of damping during particle collision"""
        ...
    @damping_factor.setter
    def damping_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def damping_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random variation of damping"""
        ...
    @damping_random.setter
    def damping_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def friction_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of friction during particle collision"""
        ...
    @friction_factor.setter
    def friction_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def friction_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Random variation of friction"""
        ...
    @friction_random.setter
    def friction_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def permeability(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Chance that the particle will pass through the mesh"""
        ...
    @permeability.setter
    def permeability(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_particle_kill(self) -> bool:
        """Kill collided particles"""
        ...
    @use_particle_kill.setter
    def use_particle_kill(self, value: bool):
        ...
    @property
    def stickiness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of stickiness to surface collision"""
        ...
    @stickiness.setter
    def stickiness(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_inner(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Inner face thickness (only used by softbodies)"""
        ...
    @thickness_inner.setter
    def thickness_inner(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_outer(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Outer face thickness"""
        ...
    @thickness_outer.setter
    def thickness_outer(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of damping during collision"""
        ...
    @damping.setter
    def damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def absorption(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """How much of effector force gets lost during collision with this object (in percent)"""
        ...
    @absorption.setter
    def absorption(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]):
        ...
    @property
    def cloth_friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Friction for cloth collisions"""
        ...
    @cloth_friction.setter
    def cloth_friction(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_culling(self) -> bool:
        """Cloth collision acts with respect to the collider normals (improves penetration recovery)"""
        ...
    @use_culling.setter
    def use_culling(self, value: bool):
        ...
    @property
    def use_normal(self) -> bool:
        """Cloth collision impulses act in the direction of the collider normals (more reliable in some cases)"""
        ...
    @use_normal.setter
    def use_normal(self, value: bool):
        ...