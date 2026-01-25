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
class ScrewModifier(Modifier):
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
    object: 'Object'
    steps: int
    render_steps: int
    iterations: int
    axis: str
    angle: float
    screw_offset: float
    merge_threshold: float
    use_normal_flip: bool
    use_normal_calculate: bool
    use_object_screw_offset: bool
    use_merge_vertices: bool
    use_smooth_shade: bool
    use_stretch_u: bool
    use_stretch_v: bool