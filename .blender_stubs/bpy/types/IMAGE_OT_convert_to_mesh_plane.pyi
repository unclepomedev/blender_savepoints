# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .MaterialProperties_MixIn import MaterialProperties_MixIn
from .TextureProperties_MixIn import TextureProperties_MixIn
from .Operator import Operator
from .Macro import Macro
from .OperatorOptions import OperatorOptions
from .OperatorProperties import OperatorProperties
from .UILayout import UILayout
class IMAGE_OT_convert_to_mesh_plane(MaterialProperties_MixIn, TextureProperties_MixIn, Operator):
    """Convert selected reference images to textured mesh plane"""
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
    bl_idname: Annotated[str, "is_animatable=False"]
    bl_label: Annotated[str, "is_animatable=False"]
    bl_translation_context: Annotated[str, "is_animatable=False"]
    bl_description: Annotated[str, "is_animatable=False"]
    bl_undo_group: Annotated[str, "is_animatable=False"]
    bl_options: set[str]
    """Options for this operator type"""
    bl_cursor_pending: Literal['DEFAULT', 'NONE', 'WAIT', 'CROSSHAIR', 'MOVE_X', 'MOVE_Y', 'KNIFE', 'TEXT', 'PAINT_BRUSH', 'PAINT_CROSS', 'DOT', 'ERASER', 'HAND', 'HAND_POINT', 'HAND_CLOSED', 'SCROLL_X', 'SCROLL_Y', 'SCROLL_XY', 'EYEDROPPER', 'PICK_AREA', 'STOP', 'COPY', 'CROSS', 'MUTE', 'ZOOM_IN', 'ZOOM_OUT']
    """Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set)"""
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