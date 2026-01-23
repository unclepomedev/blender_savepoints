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
class RigidBodyObject(bpy_struct):
    type: str
    mesh_source: str
    enabled: bool
    collision_shape: str
    kinematic: bool
    use_deform: bool
    mass: float
    use_deactivation: bool
    use_start_deactivated: bool
    deactivate_linear_velocity: float
    deactivate_angular_velocity: float
    linear_damping: float
    angular_damping: float
    friction: float
    restitution: float
    use_margin: bool
    collision_margin: float
    collision_collections: bool