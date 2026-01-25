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
class WarpModifier(Modifier):
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
    object_from: 'Object'
    bone_from: str
    object_to: 'Object'
    bone_to: str
    strength: float
    falloff_type: str
    falloff_radius: float
    falloff_curve: 'CurveMapping'
    use_volume_preserve: bool
    vertex_group: str
    invert_vertex_group: bool
    texture: 'Texture'
    texture_coords: str
    uv_layer: str
    texture_coords_object: 'Object'
    texture_coords_bone: str