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
class ChildOfConstraint(Constraint):
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
    use_location_x: bool
    use_location_y: bool
    use_location_z: bool
    use_rotation_x: bool
    use_rotation_y: bool
    use_rotation_z: bool
    use_scale_x: bool
    use_scale_y: bool
    use_scale_z: bool
    set_inverse_pending: bool
    inverse_matrix: list[float]