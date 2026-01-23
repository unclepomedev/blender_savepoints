# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .IKParam import IKParam
class Itasc(IKParam):
    ik_solver: str
    precision: float
    iterations: int
    step_count: int
    translate_root_bones: bool
    mode: str
    reiteration_method: str
    use_auto_step: bool
    step_min: float
    step_max: float
    feedback: float
    velocity_max: float
    solver: str
    damping_max: float
    damping_epsilon: float