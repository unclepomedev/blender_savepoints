# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NODE_OT_new_geometry_node_group_tool.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Operator import Operator
from .Macro import Macro
from .OperatorOptions import OperatorOptions
from .OperatorProperties import OperatorProperties
from .UILayout import UILayout
from .bpy_prop_collection import bpy_prop_collection

class NODE_OT_new_geometry_node_group_tool(Operator):
    """Create a new geometry node group for a tool"""
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @property
    def properties(self) -> Annotated['OperatorProperties', "is_animatable=False"]:

        ...
    @property
    def has_reports(self) -> bool:
        """Operator has a set of reports (warnings and errors) from last execution"""
        ...
    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def bl_translation_context(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_translation_context.setter
    def bl_translation_context(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def bl_description(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def bl_undo_group(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_undo_group.setter
    def bl_undo_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def bl_options(self) -> set[str]:
        """Options for this operator type"""
        ...
    @bl_options.setter
    def bl_options(self, value: set[str]) -> None:
        ...
    @property
    def bl_cursor_pending(self) -> Literal['DEFAULT', 'NONE', 'WAIT', 'CROSSHAIR', 'MOVE_X', 'MOVE_Y', 'KNIFE', 'TEXT', 'PAINT_BRUSH', 'PAINT_CROSS', 'DOT', 'ERASER', 'HAND', 'HAND_POINT', 'HAND_CLOSED', 'SCROLL_X', 'SCROLL_Y', 'SCROLL_XY', 'EYEDROPPER', 'PICK_AREA', 'STOP', 'COPY', 'CROSS', 'MUTE', 'ZOOM_IN', 'ZOOM_OUT']:
        """Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set)"""
        ...
    @bl_cursor_pending.setter
    def bl_cursor_pending(self, value: Literal['DEFAULT', 'NONE', 'WAIT', 'CROSSHAIR', 'MOVE_X', 'MOVE_Y', 'KNIFE', 'TEXT', 'PAINT_BRUSH', 'PAINT_CROSS', 'DOT', 'ERASER', 'HAND', 'HAND_POINT', 'HAND_CLOSED', 'SCROLL_X', 'SCROLL_Y', 'SCROLL_XY', 'EYEDROPPER', 'PICK_AREA', 'STOP', 'COPY', 'CROSS', 'MUTE', 'ZOOM_IN', 'ZOOM_OUT']) -> None:
        ...
    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:

        ...
    @property
    def options(self) -> Annotated['OperatorOptions', "is_animatable=False"]:
        """Runtime options"""
        ...
    @property
    def macros(self) -> Annotated[bpy_prop_collection['Macro'], "is_animatable=False"]:

        ...
    def report(self, *args, **kwargs) -> Any: ...
    def is_repeat(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def execute(self, *args, **kwargs) -> Any: ...
    def check(self, *args, **kwargs) -> Any: ...
    def invoke(self, *args, **kwargs) -> Any: ...
    def modal(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def cancel(self, *args, **kwargs) -> Any: ...
    def description(self, *args, **kwargs) -> Any: ...