# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from ._GenericBone import _GenericBone
from .Bone import Bone
from .BoneColor import BoneColor
from .Constraint import Constraint
from .MotionPath import MotionPath
from .Object import Object
class PoseBone(bpy_struct, _GenericBone):
    constraints: bpy_prop_collection['Constraint']
    name: str
    motion_path: 'MotionPath'
    bone: 'Bone'
    parent: 'PoseBone'
    child: 'PoseBone'
    location: list[float]
    scale: list[float]
    rotation_quaternion: list[float]
    rotation_axis_angle: list[float]
    rotation_euler: list[float]
    rotation_mode: str
    bbone_rollin: float
    bbone_rollout: float
    bbone_curveinx: float
    bbone_curveinz: float
    bbone_curveoutx: float
    bbone_curveoutz: float
    bbone_easein: float
    bbone_easeout: float
    bbone_scalein: list[float]
    bbone_scaleout: list[float]
    bbone_custom_handle_start: 'PoseBone'
    bbone_custom_handle_end: 'PoseBone'
    matrix_channel: list[float]
    matrix_basis: list[float]
    matrix: list[float]
    head: list[float]
    tail: list[float]
    length: float
    is_in_ik_chain: bool
    lock_ik_x: bool
    lock_ik_y: bool
    lock_ik_z: bool
    use_ik_limit_x: bool
    use_ik_limit_y: bool
    use_ik_limit_z: bool
    use_ik_rotation_control: bool
    use_ik_linear_control: bool
    ik_min_x: float
    ik_max_x: float
    ik_min_y: float
    ik_max_y: float
    ik_min_z: float
    ik_max_z: float
    ik_stiffness_x: float
    ik_stiffness_y: float
    ik_stiffness_z: float
    ik_stretch: float
    ik_rotation_weight: float
    ik_linear_weight: float
    custom_shape: 'Object'
    custom_shape_scale_xyz: list[float]
    custom_shape_translation: list[float]
    custom_shape_rotation_euler: list[float]
    use_transform_at_custom_shape: bool
    use_transform_around_custom_shape: bool
    use_custom_shape_bone_size: bool
    hide: bool
    select: bool
    custom_shape_transform: 'PoseBone'
    custom_shape_wire_width: float
    color: 'BoneColor'
    lock_location: list[bool]
    lock_rotation: list[bool]
    lock_rotation_w: bool
    lock_rotations_4d: bool
    lock_scale: list[bool]
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def evaluate_envelope(self, *args, **kwargs) -> Any: ...
    def bbone_segment_index(self, *args, **kwargs) -> Any: ...
    def bbone_segment_matrix(self, *args, **kwargs) -> Any: ...
    def compute_bbone_handles(self, *args, **kwargs) -> Any: ...