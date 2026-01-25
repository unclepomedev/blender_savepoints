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
from .CurveMapping import CurveMapping
from .Material import Material
from .Object import Object
class GreasePencilHookModifier(Modifier):
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
    vertex_group_name: str
    invert_vertex_group: bool
    use_custom_curve: bool
    custom_curve: 'CurveMapping'
    open_influence_panel: bool
    open_falloff_panel: bool
    object: 'Object'
    subtarget: str
    strength: float
    falloff_type: str
    falloff_radius: float
    center: float
    matrix_inverse: float
    use_falloff_uniform: bool