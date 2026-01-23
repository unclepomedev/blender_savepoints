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
from .Object import Object
class RigidBodyConstraint(bpy_struct):
    type: str
    spring_type: str
    enabled: bool
    disable_collisions: bool
    object1: 'Object'
    object2: 'Object'
    use_breaking: bool
    breaking_threshold: float
    use_override_solver_iterations: bool
    solver_iterations: int
    use_limit_lin_x: bool
    use_limit_lin_y: bool
    use_limit_lin_z: bool
    use_limit_ang_x: bool
    use_limit_ang_y: bool
    use_limit_ang_z: bool
    use_spring_x: bool
    use_spring_y: bool
    use_spring_z: bool
    use_spring_ang_x: bool
    use_spring_ang_y: bool
    use_spring_ang_z: bool
    use_motor_lin: bool
    use_motor_ang: bool
    limit_lin_x_lower: float
    limit_lin_x_upper: float
    limit_lin_y_lower: float
    limit_lin_y_upper: float
    limit_lin_z_lower: float
    limit_lin_z_upper: float
    limit_ang_x_lower: float
    limit_ang_x_upper: float
    limit_ang_y_lower: float
    limit_ang_y_upper: float
    limit_ang_z_lower: float
    limit_ang_z_upper: float
    spring_stiffness_x: float
    spring_stiffness_y: float
    spring_stiffness_z: float
    spring_stiffness_ang_x: float
    spring_stiffness_ang_y: float
    spring_stiffness_ang_z: float
    spring_damping_x: float
    spring_damping_y: float
    spring_damping_z: float
    spring_damping_ang_x: float
    spring_damping_ang_y: float
    spring_damping_ang_z: float
    motor_lin_target_velocity: float
    motor_lin_max_impulse: float
    motor_ang_target_velocity: float
    motor_ang_max_impulse: float