# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Gizmo.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def alpha(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def color_highlight(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @color_highlight.setter
    def color_highlight(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def alpha_highlight(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @alpha_highlight.setter
    def alpha_highlight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def matrix_space(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:

        ...
    @matrix_space.setter
    def matrix_space(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def matrix_basis(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:

        ...
    @matrix_basis.setter
    def matrix_basis(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def matrix_offset(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:

        ...
    @matrix_offset.setter
    def matrix_offset(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def matrix_world(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:

        ...
    @property
    def scale_basis(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @scale_basis.setter
    def scale_basis(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def line_width(self) -> Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]:

        ...
    @line_width.setter
    def line_width(self, value: Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def select_bias(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Depth bias used for selection"""
        ...
    @select_bias.setter
    def select_bias(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def hide(self) -> bool:

        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def hide_select(self) -> bool:

        ...
    @hide_select.setter
    def hide_select(self, value: bool) -> None:
        ...
    @property
    def hide_keymap(self) -> bool:
        """Ignore the key-map for this gizmo"""
        ...
    @hide_keymap.setter
    def hide_keymap(self, value: bool) -> None:
        ...
    @property
    def use_grab_cursor(self) -> bool:

        ...
    @use_grab_cursor.setter
    def use_grab_cursor(self, value: bool) -> None:
        ...
    @property
    def use_draw_hover(self) -> bool:

        ...
    @use_draw_hover.setter
    def use_draw_hover(self, value: bool) -> None:
        ...
    @property
    def use_draw_modal(self) -> bool:
        """Show while dragging"""
        ...
    @use_draw_modal.setter
    def use_draw_modal(self, value: bool) -> None:
        ...
    @property
    def use_draw_value(self) -> bool:
        """Show an indicator for the current value while dragging"""
        ...
    @use_draw_value.setter
    def use_draw_value(self, value: bool) -> None:
        ...
    @property
    def use_draw_offset_scale(self) -> bool:
        """Scale the offset matrix (use to apply screen-space offset)"""
        ...
    @use_draw_offset_scale.setter
    def use_draw_offset_scale(self, value: bool) -> None:
        ...
    @property
    def use_draw_scale(self) -> bool:
        """Use scale when calculating the matrix"""
        ...
    @use_draw_scale.setter
    def use_draw_scale(self, value: bool) -> None:
        ...
    @property
    def use_select_background(self) -> bool:
        """Don't write into the depth buffer"""
        ...
    @use_select_background.setter
    def use_select_background(self, value: bool) -> None:
        ...
    @property
    def use_operator_tool_properties(self) -> bool:
        """Merge active tool properties on activation (does not overwrite existing)"""
        ...
    @use_operator_tool_properties.setter
    def use_operator_tool_properties(self, value: bool) -> None:
        ...
    @property
    def use_event_handle_all(self) -> bool:
        """When highlighted, do not pass events through to be handled by other keymaps"""
        ...
    @use_event_handle_all.setter
    def use_event_handle_all(self, value: bool) -> None:
        ...
    @property
    def use_tooltip(self) -> bool:
        """Use tooltips when hovering over this gizmo"""
        ...
    @use_tooltip.setter
    def use_tooltip(self, value: bool) -> None:
        ...
    @property
    def is_highlight(self) -> bool:

        ...
    @property
    def is_modal(self) -> bool:

        ...
    @property
    def select(self) -> bool:

        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
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