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
from .Object import Object
class ShrinkwrapModifier(Modifier):
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
    wrap_method: str
    wrap_mode: str
    cull_face: str
    target: 'Object'
    auxiliary_target: 'Object'
    vertex_group: str
    offset: float
    project_limit: float
    use_project_x: bool
    use_project_y: bool
    use_project_z: bool
    subsurf_levels: int
    use_negative_direction: bool
    use_positive_direction: bool
    use_invert_cull: bool
    invert_vertex_group: bool