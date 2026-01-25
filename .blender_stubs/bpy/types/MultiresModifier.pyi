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
class MultiresModifier(Modifier):
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
    uv_smooth: str
    quality: int
    boundary_smooth: str
    levels: int
    sculpt_levels: int
    render_levels: int
    total_levels: int
    is_external: bool
    filepath: str
    show_only_control_edges: bool
    use_creases: bool
    use_custom_normals: bool
    use_sculpt_base_mesh: bool