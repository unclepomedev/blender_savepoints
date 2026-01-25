"""
Online Documentation:
https://docs.blender.org/api/current/bpy.utils.toolsystem.html
"""

# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


import sys
import typing
from typing import Any, Union, Callable, Iterator

class ToolDef:
    """ToolDef(idname, label, description, icon, cursor, widget_properties, widget, keymap, brush_type, data_block, operator, draw_settings, draw_cursor, options)"""
    """
    Online Documentation:
    https://docs.blender.org/api/current/bpy.utils.toolsystem.html
    """
    def __init__(self, /, *args, **kwargs) -> Any: ...
    brush_type: Any
    def count(self, value, /) -> Any: ...
    cursor: Any
    data_block: Any
    description: Any
    draw_cursor: Any
    draw_settings: Any
    def from_dict(kw_args) -> Any: ...
    def from_fn(fn) -> Any: ...
    icon: Any
    idname: Any
    def index(self, value, start=0, stop=9223372036854775807, /) -> Any: ...
    keymap: Any
    label: Any
    operator: Any
    options: Any
    widget: Any
    widget_properties: Any
