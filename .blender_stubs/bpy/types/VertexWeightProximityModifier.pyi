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
from .Object import Object
from .Texture import Texture
class VertexWeightProximityModifier(Modifier):
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
    vertex_group: str
    proximity_mode: str
    proximity_geometry: set[str]
    target: 'Object'
    min_dist: float
    max_dist: float
    falloff_type: str
    invert_falloff: bool
    normalize: bool
    map_curve: 'CurveMapping'
    mask_constant: float
    mask_vertex_group: str
    invert_mask_vertex_group: bool
    mask_texture: 'Texture'
    mask_tex_use_channel: str
    mask_tex_mapping: str
    mask_tex_uv_layer: str
    mask_tex_map_object: 'Object'
    mask_tex_map_bone: str