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
from .OperatorProperties import OperatorProperties
class Macro(bpy_struct):
    name: str
    properties: 'OperatorProperties'
    has_reports: bool
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_undo_group: str
    bl_options: set[str]
    bl_cursor_pending: str
    def report(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...