# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Object import Object
class RigidBodyConstraint(bpy_struct):
    type: Annotated[Literal['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], "is_animatable=False"]
    """Type of Rigid Body Constraint"""
    spring_type: Annotated[Literal['SPRING1', 'SPRING2'], "is_animatable=False"]
    """Which implementation of spring to use"""
    enabled: bool
    """Enable this constraint"""
    disable_collisions: bool
    """Disable collisions between constrained rigid bodies"""
    object1: Annotated[Optional['Object'], "is_animatable=False"]
    """First Rigid Body Object to be constrained"""
    object2: Annotated[Optional['Object'], "is_animatable=False"]
    """Second Rigid Body Object to be constrained"""
    use_breaking: bool
    """Constraint can be broken if it receives an impulse above the threshold"""
    breaking_threshold: Annotated[float, "step=100.0", "precision=2"]
    """Impulse threshold that must be reached for the constraint to break"""
    use_override_solver_iterations: bool
    """Override the number of solver iterations for this constraint"""
    solver_iterations: Annotated[int, "step=1"]
    """Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)"""
    use_limit_lin_x: bool
    """Limit translation on X axis"""
    use_limit_lin_y: bool
    """Limit translation on Y axis"""
    use_limit_lin_z: bool
    """Limit translation on Z axis"""
    use_limit_ang_x: bool
    """Limit rotation around X axis"""
    use_limit_ang_y: bool
    """Limit rotation around Y axis"""
    use_limit_ang_z: bool
    """Limit rotation around Z axis"""
    use_spring_x: bool
    """Enable spring on X axis"""
    use_spring_y: bool
    """Enable spring on Y axis"""
    use_spring_z: bool
    """Enable spring on Z axis"""
    use_spring_ang_x: bool
    """Enable spring on X rotational axis"""
    use_spring_ang_y: bool
    """Enable spring on Y rotational axis"""
    use_spring_ang_z: bool
    """Enable spring on Z rotational axis"""
    use_motor_lin: bool
    """Enable linear motor"""
    use_motor_ang: bool
    """Enable angular motor"""
    limit_lin_x_lower: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Lower limit of X axis translation"""
    limit_lin_x_upper: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Upper limit of X axis translation"""
    limit_lin_y_lower: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Lower limit of Y axis translation"""
    limit_lin_y_upper: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Upper limit of Y axis translation"""
    limit_lin_z_lower: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Lower limit of Z axis translation"""
    limit_lin_z_upper: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Upper limit of Z axis translation"""
    limit_ang_x_lower: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Lower limit of X axis rotation"""
    limit_ang_x_upper: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Upper limit of X axis rotation"""
    limit_ang_y_lower: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Lower limit of Y axis rotation"""
    limit_ang_y_upper: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Upper limit of Y axis rotation"""
    limit_ang_z_lower: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Lower limit of Z axis rotation"""
    limit_ang_z_upper: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Upper limit of Z axis rotation"""
    spring_stiffness_x: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the X axis"""
    spring_stiffness_y: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the Y axis"""
    spring_stiffness_z: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the Z axis"""
    spring_stiffness_ang_x: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the X rotational axis"""
    spring_stiffness_ang_y: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the Y rotational axis"""
    spring_stiffness_ang_z: Annotated[float, "step=1.0", "precision=3"]
    """Stiffness on the Z rotational axis"""
    spring_damping_x: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the X axis"""
    spring_damping_y: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the Y axis"""
    spring_damping_z: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the Z axis"""
    spring_damping_ang_x: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the X rotational axis"""
    spring_damping_ang_y: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the Y rotational axis"""
    spring_damping_ang_z: Annotated[float, "step=10.0", "precision=3"]
    """Damping on the Z rotational axis"""
    motor_lin_target_velocity: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=1.0", "precision=3"]
    """Target linear motor velocity"""
    motor_lin_max_impulse: Annotated[float, "step=1.0", "precision=3"]
    """Maximum linear motor impulse"""
    motor_ang_target_velocity: Annotated[float, "step=1.0", "precision=3"]
    """Target angular motor velocity"""
    motor_ang_max_impulse: Annotated[float, "step=1.0", "precision=3"]
    """Maximum angular motor impulse"""