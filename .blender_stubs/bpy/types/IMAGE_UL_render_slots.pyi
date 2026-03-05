# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.IMAGE_UL_render_slots.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .UIList import UIList

class IMAGE_UL_render_slots(UIList):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and bl_idname is not set by the script, then bl_idname = "OBJECT_UL_vgroups")"""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def list_id(self) -> Annotated[str, "is_animatable=False"]:
        """Identifier of the list, if any was passed to the "list_id" parameter of "template_list()" """
        ...
    @property
    def layout_type(self) -> Literal['DEFAULT', 'COMPACT']:

        ...
    @property
    def use_filter_show(self) -> bool:
        """Show filtering options"""
        ...
    @use_filter_show.setter
    def use_filter_show(self, value: bool) -> None:
        ...
    @property
    def filter_name(self) -> Annotated[str, "is_animatable=False"]:
        """Only show items matching this name (use '*' as wildcard)"""
        ...
    @filter_name.setter
    def filter_name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_filter_invert(self) -> bool:
        """Invert filtering (show hidden items, and vice versa)"""
        ...
    @use_filter_invert.setter
    def use_filter_invert(self, value: bool) -> None:
        ...
    @property
    def use_filter_sort_alpha(self) -> bool:
        """Sort items by their name"""
        ...
    @use_filter_sort_alpha.setter
    def use_filter_sort_alpha(self, value: bool) -> None:
        ...
    @property
    def use_filter_sort_reverse(self) -> bool:
        """Reverse the order of shown items"""
        ...
    @use_filter_sort_reverse.setter
    def use_filter_sort_reverse(self, value: bool) -> None:
        ...
    @property
    def use_filter_sort_lock(self) -> bool:
        """Lock the order of shown items (user cannot change it)"""
        ...
    @use_filter_sort_lock.setter
    def use_filter_sort_lock(self, value: bool) -> None:
        ...
    @property
    def bitflag_filter_item(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """The value of the reserved bitflag 'FILTER_ITEM' (in filter_flags values)"""
        ...
    @property
    def bitflag_item_never_show(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Skip the item from displaying in the list"""
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw_item(self, *args, **kwargs) -> Any: ...
    def draw_filter(self, *args, **kwargs) -> Any: ...
    def filter_items(self, *args, **kwargs) -> Any: ...