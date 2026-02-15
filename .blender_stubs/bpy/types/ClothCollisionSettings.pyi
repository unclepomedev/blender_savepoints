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
from .Collection import Collection
class ClothCollisionSettings(bpy_struct):
    use_collision: bool
    """Enable collisions with other objects"""
    distance_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Minimum distance between collision objects before collision response takes effect"""
    friction: Annotated[float, "step=10.0", "precision=3"]
    """Friction force if a collision happened (higher = less movement)"""
    damping: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of velocity lost on collision"""
    collision_quality: Annotated[int, "step=1"]
    """How many collision iterations should be done (higher is better quality but slower)"""
    impulse_clamp: Annotated[float, "step=10.0", "precision=3"]
    """Clamp collision impulses to avoid instability (0.0 to disable clamping)"""
    use_self_collision: bool
    """Enable self collisions"""
    self_distance_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Minimum distance between cloth faces before collision response takes effect"""
    self_friction: Annotated[float, "step=10.0", "precision=3"]
    """Friction with self contact"""
    collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Limit colliders to this Collection"""
    vertex_group_self_collisions: Annotated[str, "is_animatable=False"]
    """Triangles with all vertices in this group are not used during self collisions"""
    vertex_group_object_collisions: Annotated[str, "is_animatable=False"]
    """Triangles with all vertices in this group are not used during object collisions"""
    self_impulse_clamp: Annotated[float, "step=10.0", "precision=3"]
    """Clamp collision impulses to avoid instability (0.0 to disable clamping)"""