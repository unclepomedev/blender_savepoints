# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
from .CurveProfile import CurveProfile
class BevelModifier(Modifier):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_on_cage: bool
    show_expanded: bool
    is_active: bool
    use_pin_to_last: bool
    is_override_data: bool
    use_apply_on_spline: bool
    execution_time: float
    persistent_uid: int
    width: float
    width_pct: float
    segments: int
    affect: str
    limit_method: str
    edge_weight: str
    vertex_weight: str
    angle_limit: float
    vertex_group: str
    invert_vertex_group: bool
    use_clamp_overlap: bool
    offset_type: str
    profile_type: str
    profile: float
    material: int
    loop_slide: bool
    mark_seam: bool
    mark_sharp: bool
    harden_normals: bool
    face_strength_mode: str
    miter_outer: str
    miter_inner: str
    spread: float
    custom_profile: 'CurveProfile'
    vmesh_method: str