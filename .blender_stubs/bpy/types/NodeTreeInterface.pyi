# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .NodeTreeInterfaceItem import NodeTreeInterfaceItem
class NodeTreeInterface(bpy_struct):
    @property
    def items_tree(self) -> Annotated[bpy_prop_collection['NodeTreeInterfaceItem'], "is_animatable=False"]:
        """Items in the node interface"""
        ...
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Index of the active item"""
    active: Annotated[Optional['NodeTreeInterfaceItem'], "is_animatable=False"]
    """Active item"""
    def new_socket(self, *args, **kwargs) -> Any: ...
    def new_panel(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def move_to_parent(self, *args, **kwargs) -> Any: ...