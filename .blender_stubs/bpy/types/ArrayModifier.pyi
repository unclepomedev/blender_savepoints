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
class ArrayModifier(Modifier):
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
    fit_type: str
    count: int
    fit_length: float
    curve: 'Object'
    use_constant_offset: bool
    constant_offset_displace: float
    use_relative_offset: bool
    relative_offset_displace: float
    use_merge_vertices: bool
    use_merge_vertices_cap: bool
    merge_threshold: float
    use_object_offset: bool
    offset_object: 'Object'
    start_cap: 'Object'
    end_cap: 'Object'
    offset_u: float
    offset_v: float