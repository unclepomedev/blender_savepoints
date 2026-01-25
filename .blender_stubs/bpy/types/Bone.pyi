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
from .BoneCollection import BoneCollection
from .BoneColor import BoneColor
class Bone(bpy_struct, _GenericBone):
    parent: 'Bone'
    children: bpy_prop_collection['Bone']
    collections: bpy_prop_collection['BoneCollection']
    name: str
    color: 'BoneColor'
    display_type: str
    use_connect: bool
    use_inherit_rotation: bool
    use_envelope_multiply: bool
    use_deform: bool
    inherit_scale: str
    use_local_location: bool
    use_relative_parent: bool
    show_wire: bool
    use_cyclic_offset: bool
    hide_select: bool
    envelope_distance: float
    envelope_weight: float
    head_radius: float
    tail_radius: float
    bbone_segments: int
    bbone_mapping_mode: str
    bbone_x: float
    bbone_z: float
    bbone_handle_type_start: str
    bbone_custom_handle_start: 'Bone'
    bbone_handle_use_scale_start: list[bool]
    bbone_handle_use_ease_start: bool
    bbone_handle_type_end: str
    bbone_custom_handle_end: 'Bone'
    bbone_handle_use_scale_end: list[bool]
    bbone_handle_use_ease_end: bool
    bbone_rollin: float
    bbone_rollout: float
    use_endroll_as_inroll: bool
    bbone_curveinx: float
    bbone_curveinz: float
    bbone_curveoutx: float
    bbone_curveoutz: float
    bbone_easein: float
    bbone_easeout: float
    use_scale_easing: bool
    bbone_scalein: list[float]
    bbone_scaleout: list[float]
    hide: bool
    matrix: list[float]
    matrix_local: list[float]
    tail: list[float]
    tail_local: list[float]
    head: list[float]
    head_local: list[float]
    length: float
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def evaluate_envelope(self, *args, **kwargs) -> Any: ...
    def convert_local_to_pose(self, *args, **kwargs) -> Any: ...
    def MatrixFromAxisRoll(self, *args, **kwargs) -> Any: ...
    def AxisRollFromMatrix(self, *args, **kwargs) -> Any: ...