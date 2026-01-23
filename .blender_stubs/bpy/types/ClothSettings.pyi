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
from .EffectorWeights import EffectorWeights
from .ShapeKey import ShapeKey
class ClothSettings(bpy_struct):
    goal_min: float
    goal_max: float
    goal_default: float
    goal_spring: float
    goal_friction: float
    internal_friction: float
    collider_friction: float
    density_target: float
    density_strength: float
    mass: float
    vertex_group_mass: str
    gravity: float
    air_damping: float
    pin_stiffness: float
    quality: int
    time_scale: float
    vertex_group_shrink: str
    shrink_min: float
    shrink_max: float
    voxel_cell_size: float
    tension_damping: float
    compression_damping: float
    shear_damping: float
    tension_stiffness: float
    tension_stiffness_max: float
    compression_stiffness: float
    compression_stiffness_max: float
    shear_stiffness: float
    shear_stiffness_max: float
    sewing_force_max: float
    vertex_group_structural_stiffness: str
    vertex_group_shear_stiffness: str
    bending_stiffness: float
    bending_stiffness_max: float
    bending_damping: float
    use_sewing_springs: bool
    vertex_group_bending: str
    effector_weights: 'EffectorWeights'
    rest_shape_key: 'ShapeKey'
    use_dynamic_mesh: bool
    bending_model: str
    use_internal_springs: bool
    internal_spring_normal_check: bool
    internal_spring_max_length: float
    internal_spring_max_diversion: float
    internal_tension_stiffness: float
    internal_tension_stiffness_max: float
    internal_compression_stiffness: float
    internal_compression_stiffness_max: float
    vertex_group_intern: str
    use_pressure: bool
    use_pressure_volume: bool
    uniform_pressure_force: float
    target_volume: float
    pressure_factor: float
    fluid_density: float
    vertex_group_pressure: str