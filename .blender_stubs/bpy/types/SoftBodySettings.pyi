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
from .Collection import Collection
from .EffectorWeights import EffectorWeights
class SoftBodySettings(bpy_struct):
    friction: float
    mass: float
    vertex_group_mass: str
    gravity: float
    speed: float
    vertex_group_goal: str
    goal_min: float
    goal_max: float
    goal_default: float
    goal_spring: float
    goal_friction: float
    pull: float
    push: float
    damping: float
    spring_length: int
    aero: int
    plastic: int
    bend: float
    shear: float
    vertex_group_spring: str
    collision_type: str
    ball_size: float
    ball_stiff: float
    ball_damp: float
    error_threshold: float
    step_min: int
    step_max: int
    choke: int
    fuzzy: int
    use_auto_step: bool
    use_diagnose: bool
    use_estimate_matrix: bool
    location_mass_center: list[float]
    rotation_estimate: list[float]
    scale_estimate: list[float]
    use_goal: bool
    use_edges: bool
    use_stiff_quads: bool
    use_edge_collision: bool
    use_face_collision: bool
    aerodynamics_type: str
    use_self_collision: bool
    collision_collection: 'Collection'
    effector_weights: 'EffectorWeights'