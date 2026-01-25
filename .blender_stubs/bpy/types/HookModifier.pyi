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
class HookModifier(Modifier):
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
    strength: float
    falloff_type: str
    falloff_radius: float
    falloff_curve: 'CurveMapping'
    center: float
    matrix_inverse: float
    object: 'Object'
    subtarget: str
    use_falloff_uniform: bool
    vertex_group: str
    vertex_indices: int
    invert_vertex_group: bool
    def vertex_indices_set(self, *args, **kwargs) -> Any: ...