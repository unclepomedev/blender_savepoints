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
from .Texture import Texture
class WaveModifier(Modifier):
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
    use_x: bool
    use_y: bool
    use_cyclic: bool
    use_normal: bool
    use_normal_x: bool
    use_normal_y: bool
    use_normal_z: bool
    time_offset: float
    lifetime: float
    damping_time: float
    falloff_radius: float
    start_position_x: float
    start_position_y: float
    start_position_object: 'Object'
    vertex_group: str
    invert_vertex_group: bool
    speed: float
    height: float
    width: float
    narrowness: float
    texture: 'Texture'
    texture_coords: str
    uv_layer: str
    texture_coords_object: 'Object'
    texture_coords_bone: str