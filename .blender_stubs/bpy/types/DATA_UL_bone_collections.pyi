# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .UIList import UIList
class DATA_UL_bone_collections(UIList):
    bl_idname: str
    list_id: str
    layout_type: str
    use_filter_show: bool
    filter_name: str
    use_filter_invert: bool
    use_filter_sort_alpha: bool
    use_filter_sort_reverse: bool
    use_filter_sort_lock: bool
    bitflag_filter_item: int
    bitflag_item_never_show: int
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw_item(self, *args, **kwargs) -> Any: ...
    def draw_filter(self, *args, **kwargs) -> Any: ...
    def filter_items(self, *args, **kwargs) -> Any: ...