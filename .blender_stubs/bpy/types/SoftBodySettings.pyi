# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SoftBodySettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .EffectorWeights import EffectorWeights

class SoftBodySettings(bpy_struct):

    @property
    def friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """General media friction for point movements"""
        ...
    @friction.setter
    def friction(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mass(self) -> Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]:
        """General Mass value"""
        ...
    @mass.setter
    def mass(self, value: Annotated[float, "subtype=''", "unit='MASS'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def vertex_group_mass(self) -> Annotated[str, "is_animatable=False"]:
        """Control point mass values"""
        ...
    @vertex_group_mass.setter
    def vertex_group_mass(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def gravity(self) -> Annotated[float, "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]:
        """Apply gravitation to point movement"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[float, "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def speed(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Tweak timing for physics to control frequency and speed"""
        ...
    @speed.setter
    def speed(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def vertex_group_goal(self) -> Annotated[str, "is_animatable=False"]:
        """Control point weight values"""
        ...
    @vertex_group_goal.setter
    def vertex_group_goal(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def goal_min(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Goal minimum, vertex weights are scaled to match this range"""
        ...
    @goal_min.setter
    def goal_min(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def goal_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Goal maximum, vertex weights are scaled to match this range"""
        ...
    @goal_max.setter
    def goal_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def goal_default(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Default Goal (vertex target position) value"""
        ...
    @goal_default.setter
    def goal_default(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def goal_spring(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Goal (vertex target position) spring stiffness"""
        ...
    @goal_spring.setter
    def goal_spring(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def goal_friction(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Goal (vertex target position) friction"""
        ...
    @goal_friction.setter
    def goal_friction(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pull(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Edge spring stiffness when longer than rest length"""
        ...
    @pull.setter
    def pull(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def push(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Edge spring stiffness when shorter than rest length"""
        ...
    @push.setter
    def push(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def damping(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Edge spring friction"""
        ...
    @damping.setter
    def damping(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def spring_length(self) -> Annotated[int, "step=1"]:
        """Alter spring length to shrink/blow up (unit %) 0 to disable"""
        ...
    @spring_length.setter
    def spring_length(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def aero(self) -> Annotated[int, "step=1"]:
        """Make edges 'sail'"""
        ...
    @aero.setter
    def aero(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def plastic(self) -> Annotated[int, "step=1"]:
        """Permanent deform"""
        ...
    @plastic.setter
    def plastic(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def bend(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bending Stiffness"""
        ...
    @bend.setter
    def bend(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def shear(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Shear Stiffness"""
        ...
    @shear.setter
    def shear(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def vertex_group_spring(self) -> Annotated[str, "is_animatable=False"]:
        """Control point spring strength values"""
        ...
    @vertex_group_spring.setter
    def vertex_group_spring(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def collision_type(self) -> Annotated[Literal['MANUAL', 'AVERAGE', 'MINIMAL', 'MAXIMAL', 'MINMAX'], "is_animatable=False"]:
        """Choose Collision Type"""
        ...
    @collision_type.setter
    def collision_type(self, value: Annotated[Literal['MANUAL', 'AVERAGE', 'MINIMAL', 'MAXIMAL', 'MINMAX'], "is_animatable=False"]) -> None:
        ...
    @property
    def ball_size(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Absolute ball size or factor if not manually adjusted"""
        ...
    @ball_size.setter
    def ball_size(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def ball_stiff(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Ball inflating pressure"""
        ...
    @ball_stiff.setter
    def ball_stiff(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ball_damp(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Blending to inelastic collision"""
        ...
    @ball_damp.setter
    def ball_damp(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def error_threshold(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The Runge-Kutta ODE solver error limit, low value gives more precision, high values speed"""
        ...
    @error_threshold.setter
    def error_threshold(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def step_min(self) -> Annotated[int, "step=1"]:
        """Minimal # solver steps/frame"""
        ...
    @step_min.setter
    def step_min(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def step_max(self) -> Annotated[int, "step=1"]:
        """Maximal # solver steps/frame"""
        ...
    @step_max.setter
    def step_max(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def choke(self) -> Annotated[int, "step=1"]:
        """'Viscosity' inside collision target"""
        ...
    @choke.setter
    def choke(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def fuzzy(self) -> Annotated[int, "step=1"]:
        """Fuzziness while on collision, high values make collision handling faster but less stable"""
        ...
    @fuzzy.setter
    def fuzzy(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_auto_step(self) -> bool:
        """Use velocities for automagic step sizes"""
        ...
    @use_auto_step.setter
    def use_auto_step(self, value: bool) -> None:
        ...
    @property
    def use_diagnose(self) -> bool:
        """Turn on SB diagnose console prints"""
        ...
    @use_diagnose.setter
    def use_diagnose(self, value: bool) -> None:
        ...
    @property
    def use_estimate_matrix(self) -> bool:
        """Store the estimated transforms in the soft body settings"""
        ...
    @use_estimate_matrix.setter
    def use_estimate_matrix(self, value: bool) -> None:
        ...
    @property
    def location_mass_center(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of center of mass"""
        ...
    @location_mass_center.setter
    def location_mass_center(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def rotation_estimate(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Estimated rotation matrix"""
        ...
    @rotation_estimate.setter
    def rotation_estimate(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def scale_estimate(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Estimated scale matrix"""
        ...
    @scale_estimate.setter
    def scale_estimate(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_goal(self) -> Annotated[bool, "is_animatable=False"]:
        """Define forces for vertices to stick to animated position"""
        ...
    @use_goal.setter
    def use_goal(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_edges(self) -> Annotated[bool, "is_animatable=False"]:
        """Use Edges as springs"""
        ...
    @use_edges.setter
    def use_edges(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stiff_quads(self) -> Annotated[bool, "is_animatable=False"]:
        """Add diagonal springs on 4-gons"""
        ...
    @use_stiff_quads.setter
    def use_stiff_quads(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_edge_collision(self) -> bool:
        """Edges collide too"""
        ...
    @use_edge_collision.setter
    def use_edge_collision(self, value: bool) -> None:
        ...
    @property
    def use_face_collision(self) -> bool:
        """Faces collide too, can be very slow"""
        ...
    @use_face_collision.setter
    def use_face_collision(self, value: bool) -> None:
        ...
    @property
    def aerodynamics_type(self) -> Literal['SIMPLE', 'LIFT_FORCE']:
        """Method of calculating aerodynamic interaction"""
        ...
    @aerodynamics_type.setter
    def aerodynamics_type(self, value: Literal['SIMPLE', 'LIFT_FORCE']) -> None:
        ...
    @property
    def use_self_collision(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable naive vertex ball self collision"""
        ...
    @use_self_collision.setter
    def use_self_collision(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def collision_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit colliders to this collection"""
        ...
    @collision_collection.setter
    def collision_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...