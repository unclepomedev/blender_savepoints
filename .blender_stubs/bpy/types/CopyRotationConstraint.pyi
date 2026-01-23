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
class CopyRotationConstraint(Constraint):
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
    use_x: bool
    use_y: bool
    use_z: bool
    invert_x: bool
    invert_y: bool
    invert_z: bool
    euler_order: str
    mix_mode: str
    use_offset: bool