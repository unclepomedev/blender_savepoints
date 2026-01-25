# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .GizmoGroup import GizmoGroup
from .GizmoProperties import GizmoProperties
class Gizmo(bpy_struct):
    properties: 'GizmoProperties'
    bl_idname: str
    group: 'GizmoGroup'
    color: float
    alpha: float
    color_highlight: float
    alpha_highlight: float
    matrix_space: float
    matrix_basis: float
    matrix_offset: float
    matrix_world: float
    scale_basis: float
    line_width: float
    select_bias: float
    hide: bool
    hide_select: bool
    hide_keymap: bool
    use_grab_cursor: bool
    use_draw_hover: bool
    use_draw_modal: bool
    use_draw_value: bool
    use_draw_offset_scale: bool
    use_draw_scale: bool
    use_select_background: bool
    use_operator_tool_properties: bool
    use_event_handle_all: bool
    use_tooltip: bool
    is_highlight: bool
    is_modal: bool
    select: bool
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_select(self, *args, **kwargs) -> Any: ...
    def test_select(self, *args, **kwargs) -> Any: ...
    def modal(self, *args, **kwargs) -> Any: ...
    def setup(self, *args, **kwargs) -> Any: ...
    def invoke(self, *args, **kwargs) -> Any: ...
    def exit(self, *args, **kwargs) -> Any: ...
    def select_refresh(self, *args, **kwargs) -> Any: ...
    def draw_preset_box(self, *args, **kwargs) -> Any: ...
    def draw_preset_arrow(self, *args, **kwargs) -> Any: ...
    def draw_preset_circle(self, *args, **kwargs) -> Any: ...
    def target_set_prop(self, *args, **kwargs) -> Any: ...
    def target_set_operator(self, *args, **kwargs) -> Any: ...
    def target_is_valid(self, *args, **kwargs) -> Any: ...