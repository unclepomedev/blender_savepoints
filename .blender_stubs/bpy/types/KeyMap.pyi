# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .EnumPropertyItem import EnumPropertyItem
from .KeyMapItem import KeyMapItem
class KeyMap(bpy_struct):
    name: str
    bl_owner_id: str
    space_type: str
    region_type: str
    keymap_items: bpy_prop_collection['KeyMapItem']
    is_user_modified: bool
    is_modal: bool
    show_expanded_items: bool
    show_expanded_children: bool
    modal_event_values: bpy_prop_collection['EnumPropertyItem']
    def active(self, *args, **kwargs) -> Any: ...
    def restore_to_default(self, *args, **kwargs) -> Any: ...
    def restore_item_to_default(self, *args, **kwargs) -> Any: ...