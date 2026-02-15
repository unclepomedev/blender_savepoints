# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .GizmoGroup import GizmoGroup
from .GizmoProperties import GizmoProperties
class Gizmo(bpy_struct):
    @property
    def properties(self) -> Annotated['GizmoProperties', "is_animatable=False"]:
        ...
    bl_idname: Annotated[str, "is_animatable=False"]
    @property
    def group(self) -> Annotated[Optional['GizmoGroup'], "is_animatable=False"]:
        """Gizmo group this gizmo is a member of"""
        ...
    color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    alpha: Annotated[float, "step=10.0", "precision=3"]
    color_highlight: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    alpha_highlight: Annotated[float, "step=10.0", "precision=3"]
    matrix_space: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    matrix_basis: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    matrix_offset: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    @property
    def matrix_world(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        ...
    scale_basis: Annotated[float, "step=10.0", "precision=3"]
    line_width: Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]
    select_bias: Annotated[float, "step=10.0", "precision=3"]
    """Depth bias used for selection"""
    hide: bool
    hide_select: bool
    hide_keymap: bool
    """Ignore the key-map for this gizmo"""
    use_grab_cursor: bool
    use_draw_hover: bool
    use_draw_modal: bool
    """Show while dragging"""
    use_draw_value: bool
    """Show an indicator for the current value while dragging"""
    use_draw_offset_scale: bool
    """Scale the offset matrix (use to apply screen-space offset)"""
    use_draw_scale: bool
    """Use scale when calculating the matrix"""
    use_select_background: bool
    """Don't write into the depth buffer"""
    use_operator_tool_properties: bool
    """Merge active tool properties on activation (does not overwrite existing)"""
    use_event_handle_all: bool
    """When highlighted, do not pass events through to be handled by other keymaps"""
    use_tooltip: bool
    """Use tooltips when hovering over this gizmo"""
    @property
    def is_highlight(self) -> bool:
        ...
    @property
    def is_modal(self) -> bool:
        ...
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