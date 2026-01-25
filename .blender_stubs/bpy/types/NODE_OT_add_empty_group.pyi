# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .NodeAddOperator import NodeAddOperator
from .Operator import Operator
from .Macro import Macro
from .OperatorOptions import OperatorOptions
from .OperatorProperties import OperatorProperties
from .UILayout import UILayout
class NODE_OT_add_empty_group(NodeAddOperator, Operator):
    name: str
    properties: 'OperatorProperties'
    has_reports: bool
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_undo_group: str
    bl_options: str
    bl_cursor_pending: str
    layout: 'UILayout'
    options: 'OperatorOptions'
    macros: bpy_prop_collection['Macro']
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