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
from .Object import Object
class DataTransferModifier(Modifier):
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
    object: 'Object'
    use_object_transform: bool
    use_vert_data: bool
    use_edge_data: bool
    use_loop_data: bool
    use_poly_data: bool
    data_types_verts: set[str]
    data_types_edges: set[str]
    data_types_loops: set[str]
    data_types_polys: set[str]
    vert_mapping: str
    edge_mapping: str
    loop_mapping: str
    poly_mapping: str
    use_max_distance: bool
    max_distance: float
    ray_radius: float
    islands_precision: float
    layers_vgroup_select_src: str
    layers_vcol_vert_select_src: str
    layers_vcol_loop_select_src: str
    layers_uv_select_src: str
    layers_vgroup_select_dst: str
    layers_vcol_vert_select_dst: str
    layers_vcol_loop_select_dst: str
    layers_uv_select_dst: str
    mix_mode: str
    mix_factor: float
    vertex_group: str
    invert_vertex_group: bool