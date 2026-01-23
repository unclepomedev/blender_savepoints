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
class SubsurfModifier(Modifier):
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
    subdivision_type: str
    levels: int
    render_levels: int
    show_only_control_edges: bool
    use_creases: bool
    use_custom_normals: bool
    use_limit_surface: bool
    use_adaptive_subdivision: bool
    adaptive_space: str
    adaptive_pixel_size: float
    adaptive_object_edge_length: float
    open_adaptive_subdivision_panel: bool
    open_advanced_panel: bool