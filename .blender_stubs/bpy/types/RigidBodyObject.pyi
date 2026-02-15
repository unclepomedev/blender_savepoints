# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class RigidBodyObject(bpy_struct):
    type: Annotated[Literal['ACTIVE', 'PASSIVE'], "is_animatable=False"]
    """Role of object in Rigid Body Simulations"""
    mesh_source: Annotated[Literal['BASE', 'DEFORM', 'FINAL'], "is_animatable=False"]
    """Source of the mesh used to create collision shape"""
    enabled: bool
    """Rigid Body actively participates to the simulation"""
    collision_shape: Annotated[Literal['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH', 'COMPOUND'], "is_animatable=False"]
    """Collision Shape of object in Rigid Body Simulations"""
    kinematic: bool
    """Allow rigid body to be controlled by the animation system"""
    use_deform: bool
    """Rigid body deforms during simulation"""
    mass: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]
    """How much the object 'weighs' irrespective of gravity"""
    use_deactivation: bool
    """Enable deactivation of resting rigid bodies (increases performance and stability but can cause glitches)"""
    use_start_deactivated: Annotated[bool, "is_animatable=False"]
    """Deactivate rigid body at the start of the simulation"""
    deactivate_linear_velocity: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Linear Velocity below which simulation stops simulating object"""
    deactivate_angular_velocity: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Angular Velocity below which simulation stops simulating object"""
    linear_damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of linear velocity that is lost over time"""
    angular_damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of angular velocity that is lost over time"""
    friction: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Resistance of object to movement"""
    restitution: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3"]
    """Tendency of object to bounce after colliding with another (0 = stays still, 1 = perfectly elastic)"""
    use_margin: bool
    """Use custom collision margin (some shapes will have a visible gap around them)"""
    collision_margin: Annotated[float, "subtype=''", "unit='LENGTH'", "step=0.009999999776482582", "precision=3"]
    """Threshold of distance near surface where collisions are still considered (best results when non-zero)"""
    collision_collections: Annotated[list[bool], "subtype='LAYER_MEMBER'"]
    """Collision collections rigid body belongs to"""