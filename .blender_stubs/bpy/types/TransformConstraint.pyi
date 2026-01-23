# Blender Probe Generated Stub for Blender 5.1.0 Alpha
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
class TransformConstraint(Constraint):
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
    map_from: str
    map_to: str
    map_to_x_from: str
    map_to_y_from: str
    map_to_z_from: str
    use_motion_extrapolate: bool
    from_rotation_mode: str
    to_euler_order: str
    from_min_x: float
    from_min_y: float
    from_min_z: float
    from_max_x: float
    from_max_y: float
    from_max_z: float
    to_min_x: float
    to_min_y: float
    to_min_z: float
    to_max_x: float
    to_max_y: float
    to_max_z: float
    mix_mode: str
    from_min_x_rot: float
    from_min_y_rot: float
    from_min_z_rot: float
    from_max_x_rot: float
    from_max_y_rot: float
    from_max_z_rot: float
    to_min_x_rot: float
    to_min_y_rot: float
    to_min_z_rot: float
    to_max_x_rot: float
    to_max_y_rot: float
    to_max_z_rot: float
    mix_mode_rot: str
    from_min_x_scale: float
    from_min_y_scale: float
    from_min_z_scale: float
    from_max_x_scale: float
    from_max_y_scale: float
    from_max_z_scale: float
    to_min_x_scale: float
    to_min_y_scale: float
    to_min_z_scale: float
    to_max_x_scale: float
    to_max_y_scale: float
    to_max_z_scale: float
    mix_mode_scale: str