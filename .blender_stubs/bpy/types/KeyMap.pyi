# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyMap.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .EnumPropertyItem import EnumPropertyItem
from .KeyMapItem import KeyMapItem
from .KeyMapItems import KeyMapItems
from .bpy_prop_collection import bpy_prop_collection

class KeyMap(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the key map"""
        ...
    @property
    def bl_owner_id(self) -> Annotated[str, "is_animatable=False"]:
        """Internal owner"""
        ...
    @bl_owner_id.setter
    def bl_owner_id(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def space_type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Optional space type keymap is associated with"""
        ...
    @property
    def region_type(self) -> Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']:
        """Optional region type keymap is associated with"""
        ...
    @property
    def keymap_items(self) -> Annotated['KeyMapItems', "is_animatable=False"]:
        """Items in the keymap, linking an operator to an input event"""
        ...
    @property
    def is_user_modified(self) -> bool:
        """Keymap is defined by the user"""
        ...
    @is_user_modified.setter
    def is_user_modified(self, value: bool):
        ...
    @property
    def is_modal(self) -> bool:
        """Indicates that a keymap is used for translate modal events for an operator"""
        ...
    @property
    def show_expanded_items(self) -> bool:
        """Expanded in the user interface"""
        ...
    @show_expanded_items.setter
    def show_expanded_items(self, value: bool):
        ...
    @property
    def show_expanded_children(self) -> bool:
        """Children expanded in the user interface"""
        ...
    @show_expanded_children.setter
    def show_expanded_children(self, value: bool):
        ...
    @property
    def modal_event_values(self) -> Annotated[bpy_prop_collection['EnumPropertyItem'], "is_animatable=False"]:
        """Give access to the possible event values of this modal keymap's items (#KeyMapItem.propvalue), for API introspection"""
        ...
    def active(self, *args, **kwargs) -> Any: ...
    def restore_to_default(self, *args, **kwargs) -> Any: ...
    def restore_item_to_default(self, *args, **kwargs) -> Any: ...