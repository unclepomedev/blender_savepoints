# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Constraint import Constraint
from .Object import Object
class KinematicConstraint(Constraint):
    name: str
    type: str
    is_override_data: bool
    owner_space: str
    target_space: str
    space_object: 'Object'
    space_subtarget: str
    mute: bool
    enabled: bool
    show_expanded: bool
    is_valid: bool
    active: bool
    influence: float
    error_location: float
    error_rotation: float
    target: 'Object'
    subtarget: str
    iterations: int
    pole_target: 'Object'
    pole_subtarget: str
    pole_angle: float
    weight: float
    orient_weight: float
    chain_count: int
    use_tail: bool
    reference_axis: str
    use_location: bool
    lock_location_x: bool
    lock_location_y: bool
    lock_location_z: bool
    use_rotation: bool
    lock_rotation_x: bool
    lock_rotation_y: bool
    lock_rotation_z: bool
    use_stretch: bool
    ik_type: str
    limit_mode: str
    distance: float