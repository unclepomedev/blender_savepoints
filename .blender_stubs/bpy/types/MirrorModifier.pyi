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
class MirrorModifier(Modifier):
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
    use_axis: bool
    use_bisect_axis: bool
    use_bisect_flip_axis: bool
    use_clip: bool
    use_mirror_vertex_groups: bool
    use_mirror_merge: bool
    use_mirror_u: bool
    use_mirror_v: bool
    use_mirror_udim: bool
    mirror_offset_u: float
    mirror_offset_v: float
    offset_u: float
    offset_v: float
    merge_threshold: float
    bisect_threshold: float
    mirror_object: 'Object'