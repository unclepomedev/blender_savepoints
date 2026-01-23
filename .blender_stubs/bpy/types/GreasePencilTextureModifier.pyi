# Blender Probe Generated Stub for Blender 5.1.0 Alpha
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
class GreasePencilTextureModifier(Modifier):
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
    uv_offset: float
    uv_scale: float
    alignment_rotation: float
    fill_rotation: float
    fill_offset: list[float]
    fill_scale: float
    fit_method: str
    mode: str