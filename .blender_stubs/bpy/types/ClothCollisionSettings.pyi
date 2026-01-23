# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Collection import Collection
class ClothCollisionSettings(bpy_struct):
    use_collision: bool
    distance_min: float
    friction: float
    damping: float
    collision_quality: int
    impulse_clamp: float
    use_self_collision: bool
    self_distance_min: float
    self_friction: float
    collection: 'Collection'
    vertex_group_self_collisions: str
    vertex_group_object_collisions: str
    self_impulse_clamp: float