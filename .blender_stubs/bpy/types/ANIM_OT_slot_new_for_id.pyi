# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Operator import Operator
from .Macro import Macro
from .OperatorOptions import OperatorOptions
from .OperatorProperties import OperatorProperties
from .UILayout import UILayout
class ANIM_OT_slot_new_for_id(Operator):
    """Create a new Action Slot for an ID.

    Note that _which_ ID should get this slot must be set in the 'animated_id' context pointer, using:

    >>> layout.context_pointer_set("animated_id", animated_id)

    When the ID already has a slot assigned, the newly-created slot will be
    named after it (ensuring uniqueness with a numerical suffix) and any
    animation data of the assigned slot will be duplicated for the new slot.
    """
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