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
class SplineIKConstraint(Constraint):
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
    chain_count: int
    joint_bindings: float
    use_chain_offset: bool
    use_even_divisions: bool
    use_curve_radius: bool
    xz_scale_mode: str
    y_scale_mode: str
    use_original_scale: bool
    bulge: float
    use_bulge_min: bool
    use_bulge_max: bool
    bulge_min: float
    bulge_max: float
    bulge_smooth: float