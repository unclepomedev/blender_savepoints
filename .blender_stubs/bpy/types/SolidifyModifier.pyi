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
class SolidifyModifier(Modifier):
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
    solidify_mode: str
    thickness: float
    thickness_clamp: float
    use_thickness_angle_clamp: bool
    thickness_vertex_group: float
    offset: float
    edge_crease_inner: float
    edge_crease_outer: float
    edge_crease_rim: float
    material_offset: int
    material_offset_rim: int
    vertex_group: str
    shell_vertex_group: str
    rim_vertex_group: str
    use_rim: bool
    use_even_offset: bool
    use_quality_normals: bool
    invert_vertex_group: bool
    use_flat_faces: bool
    use_flip_normals: bool
    use_rim_only: bool
    nonmanifold_thickness_mode: str
    nonmanifold_boundary_mode: str
    nonmanifold_merge_threshold: float
    bevel_convex: float