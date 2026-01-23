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
from .MovieClip import MovieClip
from .Object import Object
class ObjectSolverConstraint(Constraint):
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
    clip: 'MovieClip'
    use_active_clip: bool
    set_inverse_pending: bool
    object: str
    camera: 'Object'