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
from .Material import Material
from .Object import Object
class GreasePencilBuildModifier(Modifier):
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
    tree_node_filter: str
    use_layer_pass_filter: bool
    layer_pass_filter: int
    invert_layer_filter: bool
    invert_layer_pass_filter: bool
    use_layer_group_filter: bool
    material_filter: 'Material'
    use_material_pass_filter: bool
    material_pass_filter: int
    invert_material_filter: bool
    invert_material_pass_filter: bool
    open_influence_panel: bool
    open_frame_range_panel: bool
    open_fading_panel: bool
    mode: str
    transition: str
    start_delay: float
    length: float
    concurrent_time_alignment: str
    time_mode: str
    speed_factor: float
    speed_maxgap: float
    use_restrict_frame_range: bool
    use_percentage: bool
    percentage_factor: float
    frame_start: float
    frame_end: float
    use_fading: bool
    fade_factor: float
    target_vertex_group: str
    fade_opacity_strength: float
    fade_thickness_strength: float
    object: 'Object'