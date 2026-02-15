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
from .NodeTreeInterfacePanel import NodeTreeInterfacePanel
class NodeTreeInterfaceItem(bpy_struct):
    @property
    def item_type(self) -> Literal['SOCKET', 'PANEL']:
        """Type of interface item"""
        ...
    @property
    def parent(self) -> Annotated[Optional['NodeTreeInterfacePanel'], "is_animatable=False"]:
        """Panel that contains the item"""
        ...
    @property
    def position(self) -> Annotated[int, "step=1"]:
        """Position of the item in its parent panel"""
        ...
    @property
    def index(self) -> Annotated[int, "step=1"]:
        """Global index of the item among all items in the interface"""
        ...