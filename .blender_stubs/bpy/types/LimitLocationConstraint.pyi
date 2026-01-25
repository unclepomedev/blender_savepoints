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
class LimitLocationConstraint(Constraint):
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
    use_min_x: bool
    use_min_y: bool
    use_min_z: bool
    use_max_x: bool
    use_max_y: bool
    use_max_z: bool
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float
    use_transform_limit: bool