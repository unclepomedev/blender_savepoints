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
class CollisionSettings(bpy_struct):
    use: bool
    damping_factor: float
    damping_random: float
    friction_factor: float
    friction_random: float
    permeability: float
    use_particle_kill: bool
    stickiness: float
    thickness_inner: float
    thickness_outer: float
    damping: float
    absorption: float
    cloth_friction: float
    use_culling: bool
    use_normal: bool