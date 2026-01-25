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
from .NodeTreeInterfaceItem import NodeTreeInterfaceItem
class NodeTreeInterface(bpy_struct):
    items_tree: bpy_prop_collection['NodeTreeInterfaceItem']
    active_index: int
    active: 'NodeTreeInterfaceItem'
    def new_socket(self, *args, **kwargs) -> Any: ...
    def new_panel(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def move_to_parent(self, *args, **kwargs) -> Any: ...