# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .NodeTreeInterfaceItem import NodeTreeInterfaceItem
class NodeTreeInterfacePanel(NodeTreeInterfaceItem):
    item_type: str
    parent: 'NodeTreeInterfacePanel'
    position: int
    index: int
    name: str
    description: str
    default_closed: bool
    select: bool
    interface_items: bpy_prop_collection['NodeTreeInterfaceItem']
    persistent_uid: int