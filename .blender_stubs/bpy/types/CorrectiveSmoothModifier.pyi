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
class CorrectiveSmoothModifier(Modifier):
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
    factor: float
    iterations: int
    scale: float
    rest_source: str
    smooth_type: str
    invert_vertex_group: bool
    vertex_group: str
    is_bind: bool
    use_only_smooth: bool
    use_pin_boundary: bool