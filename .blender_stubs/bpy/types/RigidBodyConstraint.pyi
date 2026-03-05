# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RigidBodyConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class RigidBodyConstraint(bpy_struct):

    @property
    def type(self) -> Annotated[Literal['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], "is_animatable=False"]:
        """Type of Rigid Body Constraint"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], "is_animatable=False"]) -> None:
        ...
    @property
    def spring_type(self) -> Annotated[Literal['SPRING1', 'SPRING2'], "is_animatable=False"]:
        """Which implementation of spring to use"""
        ...
    @spring_type.setter
    def spring_type(self, value: Annotated[Literal['SPRING1', 'SPRING2'], "is_animatable=False"]) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """Enable this constraint"""
        ...
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def disable_collisions(self) -> bool:
        """Disable collisions between constrained rigid bodies"""
        ...
    @disable_collisions.setter
    def disable_collisions(self, value: bool) -> None:
        ...
    @property
    def object1(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """First Rigid Body Object to be constrained"""
        ...
    @object1.setter
    def object1(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def object2(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Second Rigid Body Object to be constrained"""
        ...
    @object2.setter
    def object2(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_breaking(self) -> bool:
        """Constraint can be broken if it receives an impulse above the threshold"""
        ...
    @use_breaking.setter
    def use_breaking(self, value: bool) -> None:
        ...
    @property
    def breaking_threshold(self) -> Annotated[float, "step=100.0", "precision=2"]:
        """Impulse threshold that must be reached for the constraint to break"""
        ...
    @breaking_threshold.setter
    def breaking_threshold(self, value: Annotated[float, "step=100.0", "precision=2"]) -> None:
        ...
    @property
    def use_override_solver_iterations(self) -> bool:
        """Override the number of solver iterations for this constraint"""
        ...
    @use_override_solver_iterations.setter
    def use_override_solver_iterations(self, value: bool) -> None:
        ...
    @property
    def solver_iterations(self) -> Annotated[int, "step=1"]:
        """Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)"""
        ...
    @solver_iterations.setter
    def solver_iterations(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_limit_lin_x(self) -> bool:
        """Limit translation on X axis"""
        ...
    @use_limit_lin_x.setter
    def use_limit_lin_x(self, value: bool) -> None:
        ...
    @property
    def use_limit_lin_y(self) -> bool:
        """Limit translation on Y axis"""
        ...
    @use_limit_lin_y.setter
    def use_limit_lin_y(self, value: bool) -> None:
        ...
    @property
    def use_limit_lin_z(self) -> bool:
        """Limit translation on Z axis"""
        ...
    @use_limit_lin_z.setter
    def use_limit_lin_z(self, value: bool) -> None:
        ...
    @property
    def use_limit_ang_x(self) -> bool:
        """Limit rotation around X axis"""
        ...
    @use_limit_ang_x.setter
    def use_limit_ang_x(self, value: bool) -> None:
        ...
    @property
    def use_limit_ang_y(self) -> bool:
        """Limit rotation around Y axis"""
        ...
    @use_limit_ang_y.setter
    def use_limit_ang_y(self, value: bool) -> None:
        ...
    @property
    def use_limit_ang_z(self) -> bool:
        """Limit rotation around Z axis"""
        ...
    @use_limit_ang_z.setter
    def use_limit_ang_z(self, value: bool) -> None:
        ...
    @property
    def use_spring_x(self) -> bool:
        """Enable spring on X axis"""
        ...
    @use_spring_x.setter
    def use_spring_x(self, value: bool) -> None:
        ...
    @property
    def use_spring_y(self) -> bool:
        """Enable spring on Y axis"""
        ...
    @use_spring_y.setter
    def use_spring_y(self, value: bool) -> None:
        ...
    @property
    def use_spring_z(self) -> bool:
        """Enable spring on Z axis"""
        ...
    @use_spring_z.setter
    def use_spring_z(self, value: bool) -> None:
        ...
    @property
    def use_spring_ang_x(self) -> bool:
        """Enable spring on X rotational axis"""
        ...
    @use_spring_ang_x.setter
    def use_spring_ang_x(self, value: bool) -> None:
        ...
    @property
    def use_spring_ang_y(self) -> bool:
        """Enable spring on Y rotational axis"""
        ...
    @use_spring_ang_y.setter
    def use_spring_ang_y(self, value: bool) -> None:
        ...
    @property
    def use_spring_ang_z(self) -> bool:
        """Enable spring on Z rotational axis"""
        ...
    @use_spring_ang_z.setter
    def use_spring_ang_z(self, value: bool) -> None:
        ...
    @property
    def use_motor_lin(self) -> bool:
        """Enable linear motor"""
        ...
    @use_motor_lin.setter
    def use_motor_lin(self, value: bool) -> None:
        ...
    @property
    def use_motor_ang(self) -> bool:
        """Enable angular motor"""
        ...
    @use_motor_ang.setter
    def use_motor_ang(self, value: bool) -> None:
        ...
    @property
    def limit_lin_x_lower(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Lower limit of X axis translation"""
        ...
    @limit_lin_x_lower.setter
    def limit_lin_x_lower(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_lin_x_upper(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Upper limit of X axis translation"""
        ...
    @limit_lin_x_upper.setter
    def limit_lin_x_upper(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_lin_y_lower(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Lower limit of Y axis translation"""
        ...
    @limit_lin_y_lower.setter
    def limit_lin_y_lower(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_lin_y_upper(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Upper limit of Y axis translation"""
        ...
    @limit_lin_y_upper.setter
    def limit_lin_y_upper(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_lin_z_lower(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Lower limit of Z axis translation"""
        ...
    @limit_lin_z_lower.setter
    def limit_lin_z_lower(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_lin_z_upper(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Upper limit of Z axis translation"""
        ...
    @limit_lin_z_upper.setter
    def limit_lin_z_upper(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_x_lower(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Lower limit of X axis rotation"""
        ...
    @limit_ang_x_lower.setter
    def limit_ang_x_lower(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_x_upper(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Upper limit of X axis rotation"""
        ...
    @limit_ang_x_upper.setter
    def limit_ang_x_upper(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_y_lower(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Lower limit of Y axis rotation"""
        ...
    @limit_ang_y_lower.setter
    def limit_ang_y_lower(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_y_upper(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Upper limit of Y axis rotation"""
        ...
    @limit_ang_y_upper.setter
    def limit_ang_y_upper(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_z_lower(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Lower limit of Z axis rotation"""
        ...
    @limit_ang_z_lower.setter
    def limit_ang_z_lower(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def limit_ang_z_upper(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Upper limit of Z axis rotation"""
        ...
    @limit_ang_z_upper.setter
    def limit_ang_z_upper(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_x(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the X axis"""
        ...
    @spring_stiffness_x.setter
    def spring_stiffness_x(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_y(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the Y axis"""
        ...
    @spring_stiffness_y.setter
    def spring_stiffness_y(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_z(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the Z axis"""
        ...
    @spring_stiffness_z.setter
    def spring_stiffness_z(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_ang_x(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the X rotational axis"""
        ...
    @spring_stiffness_ang_x.setter
    def spring_stiffness_ang_x(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_ang_y(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the Y rotational axis"""
        ...
    @spring_stiffness_ang_y.setter
    def spring_stiffness_ang_y(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_stiffness_ang_z(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Stiffness on the Z rotational axis"""
        ...
    @spring_stiffness_ang_z.setter
    def spring_stiffness_ang_z(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the X axis"""
        ...
    @spring_damping_x.setter
    def spring_damping_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the Y axis"""
        ...
    @spring_damping_y.setter
    def spring_damping_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_z(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the Z axis"""
        ...
    @spring_damping_z.setter
    def spring_damping_z(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_ang_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the X rotational axis"""
        ...
    @spring_damping_ang_x.setter
    def spring_damping_ang_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_ang_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the Y rotational axis"""
        ...
    @spring_damping_ang_y.setter
    def spring_damping_ang_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_damping_ang_z(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Damping on the Z rotational axis"""
        ...
    @spring_damping_ang_z.setter
    def spring_damping_ang_z(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def motor_lin_target_velocity(self) -> Annotated[float, "subtype=''", "unit='VELOCITY'", "step=1.0", "precision=3"]:
        """Target linear motor velocity"""
        ...
    @motor_lin_target_velocity.setter
    def motor_lin_target_velocity(self, value: Annotated[float, "subtype=''", "unit='VELOCITY'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def motor_lin_max_impulse(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Maximum linear motor impulse"""
        ...
    @motor_lin_max_impulse.setter
    def motor_lin_max_impulse(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def motor_ang_target_velocity(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Target angular motor velocity"""
        ...
    @motor_ang_target_velocity.setter
    def motor_ang_target_velocity(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def motor_ang_max_impulse(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Maximum angular motor impulse"""
        ...
    @motor_ang_max_impulse.setter
    def motor_ang_max_impulse(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...