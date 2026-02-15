# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodeTreeInterfacePanel.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .NodeTreeInterfaceItem import NodeTreeInterfaceItem
from .bpy_prop_collection import bpy_prop_collection

class NodeTreeInterfacePanel(NodeTreeInterfaceItem):

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
    name: Annotated[str, "is_animatable=False"]
    """Panel name"""
    description: Annotated[str, "is_animatable=False"]
    """Panel description"""
    default_closed: Annotated[bool, "is_animatable=False"]
    """Panel is closed by default on new nodes"""
    @property
    def interface_items(self) -> Annotated[bpy_prop_collection['NodeTreeInterfaceItem'], "is_animatable=False"]:
        """Items in the node panel"""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Unique identifier for this panel within this node tree"""
        ...