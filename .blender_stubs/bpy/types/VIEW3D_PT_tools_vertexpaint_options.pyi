# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Panel import Panel
from .View3DPaintPanel import View3DPaintPanel
from .Constraint import Constraint
from .UILayout import UILayout
class VIEW3D_PT_tools_vertexpaint_options(Panel, View3DPaintPanel):
    layout: 'UILayout'
    text: str
    custom_data: 'Constraint'
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_category: str
    bl_owner_id: str
    bl_space_type: str
    bl_region_type: str
    bl_context: str
    bl_options: str
    bl_parent_id: str
    bl_ui_units_x: int
    bl_order: int
    use_pin: bool
    is_popover: bool
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_header(self, *args, **kwargs) -> Any: ...
    def draw_header_preset(self, *args, **kwargs) -> Any: ...