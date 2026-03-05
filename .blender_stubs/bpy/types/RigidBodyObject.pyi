# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RigidBodyObject.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class RigidBodyObject(bpy_struct):

    @property
    def type(self) -> Annotated[Literal['ACTIVE', 'PASSIVE'], "is_animatable=False"]:
        """Role of object in Rigid Body Simulations"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['ACTIVE', 'PASSIVE'], "is_animatable=False"]) -> None:
        ...
    @property
    def mesh_source(self) -> Annotated[Literal['BASE', 'DEFORM', 'FINAL'], "is_animatable=False"]:
        """Source of the mesh used to create collision shape"""
        ...
    @mesh_source.setter
    def mesh_source(self, value: Annotated[Literal['BASE', 'DEFORM', 'FINAL'], "is_animatable=False"]) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """Rigid Body actively participates to the simulation"""
        ...
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def collision_shape(self) -> Annotated[Literal['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH', 'COMPOUND'], "is_animatable=False"]:
        """Collision Shape of object in Rigid Body Simulations"""
        ...
    @collision_shape.setter
    def collision_shape(self, value: Annotated[Literal['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH', 'COMPOUND'], "is_animatable=False"]) -> None:
        ...
    @property
    def kinematic(self) -> bool:
        """Allow rigid body to be controlled by the animation system"""
        ...
    @kinematic.setter
    def kinematic(self, value: bool) -> None:
        ...
    @property
    def use_deform(self) -> bool:
        """Rigid body deforms during simulation"""
        ...
    @use_deform.setter
    def use_deform(self, value: bool) -> None:
        ...
    @property
    def mass(self) -> Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]:
        """How much the object 'weighs' irrespective of gravity"""
        ...
    @mass.setter
    def mass(self, value: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_deactivation(self) -> bool:
        """Enable deactivation of resting rigid bodies (increases performance and stability but can cause glitches)"""
        ...
    @use_deactivation.setter
    def use_deactivation(self, value: bool) -> None:
        ...
    @property
    def use_start_deactivated(self) -> Annotated[bool, "is_animatable=False"]:
        """Deactivate rigid body at the start of the simulation"""
        ...
    @use_start_deactivated.setter
    def use_start_deactivated(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def deactivate_linear_velocity(self) -> Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Linear Velocity below which simulation stops simulating object"""
        ...
    @deactivate_linear_velocity.setter
    def deactivate_linear_velocity(self, value: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def deactivate_angular_velocity(self) -> Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]:
        """Angular Velocity below which simulation stops simulating object"""
        ...
    @deactivate_angular_velocity.setter
    def deactivate_angular_velocity(self, value: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def linear_damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of linear velocity that is lost over time"""
        ...
    @linear_damping.setter
    def linear_damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def angular_damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of angular velocity that is lost over time"""
        ...
    @angular_damping.setter
    def angular_damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def friction(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Resistance of object to movement"""
        ...
    @friction.setter
    def friction(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def restitution(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]:
        """Tendency of object to bounce after colliding with another (0 = stays still, 1 = perfectly elastic)"""
        ...
    @restitution.setter
    def restitution(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_margin(self) -> bool:
        """Use custom collision margin (some shapes will have a visible gap around them)"""
        ...
    @use_margin.setter
    def use_margin(self, value: bool) -> None:
        ...
    @property
    def collision_margin(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.009999999776482582", "precision=3"]:
        """Threshold of distance near surface where collisions are still considered (best results when non-zero)"""
        ...
    @collision_margin.setter
    def collision_margin(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.009999999776482582", "precision=3"]) -> None:
        ...
    @property
    def collision_collections(self) -> Annotated[list[bool], "subtype='LAYER_MEMBER'"]:
        """Collision collections rigid body belongs to"""
        ...
    @collision_collections.setter
    def collision_collections(self, value: Annotated[list[bool], "subtype='LAYER_MEMBER'"]) -> None:
        ...