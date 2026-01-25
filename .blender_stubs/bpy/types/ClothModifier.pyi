# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
from .ClothCollisionSettings import ClothCollisionSettings
from .ClothSettings import ClothSettings
from .ClothSolverResult import ClothSolverResult
from .PointCache import PointCache
class ClothModifier(Modifier):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_on_cage: bool
    show_expanded: bool
    is_active: bool
    use_pin_to_last: bool
    is_override_data: bool
    use_apply_on_spline: bool
    execution_time: float
    persistent_uid: int
    settings: 'ClothSettings'
    collision_settings: 'ClothCollisionSettings'
    solver_result: 'ClothSolverResult'
    point_cache: 'PointCache'
    hair_grid_min: list[float]
    hair_grid_max: list[float]
    hair_grid_resolution: list[int]