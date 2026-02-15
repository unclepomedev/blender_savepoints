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
class CollisionSettings(bpy_struct):
    use: bool
    """Enable this object as a collider for physics systems"""
    damping_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of damping during particle collision"""
    damping_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random variation of damping"""
    friction_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of friction during particle collision"""
    friction_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Random variation of friction"""
    permeability: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Chance that the particle will pass through the mesh"""
    use_particle_kill: bool
    """Kill collided particles"""
    stickiness: Annotated[float, "step=10.0", "precision=3"]
    """Amount of stickiness to surface collision"""
    thickness_inner: Annotated[float, "step=10.0", "precision=3"]
    """Inner face thickness (only used by softbodies)"""
    thickness_outer: Annotated[float, "step=10.0", "precision=3"]
    """Outer face thickness"""
    damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of damping during collision"""
    absorption: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """How much of effector force gets lost during collision with this object (in percent)"""
    cloth_friction: Annotated[float, "step=10.0", "precision=3"]
    """Friction for cloth collisions"""
    use_culling: bool
    """Cloth collision acts with respect to the collider normals (improves penetration recovery)"""
    use_normal: bool
    """Cloth collision impulses act in the direction of the collider normals (more reliable in some cases)"""