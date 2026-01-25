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
class EditBone(bpy_struct, _GenericBone):
    collections: bpy_prop_collection['BoneCollection']
    parent: 'EditBone'
    roll: float
    head: float
    tail: float
    length: float
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
    bbone_custom_handle_start: 'EditBone'
    bbone_handle_use_scale_start: bool
    bbone_handle_use_ease_start: bool
    bbone_handle_type_end: str
    bbone_custom_handle_end: 'EditBone'
    bbone_handle_use_scale_end: bool
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
    bbone_scalein: float
    bbone_scaleout: float
    hide: bool
    lock: bool
    select: bool
    select_head: bool
    select_tail: bool
    matrix: float
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def align_roll(self, *args, **kwargs) -> Any: ...