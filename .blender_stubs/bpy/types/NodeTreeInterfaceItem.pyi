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
from .NodeTreeInterfacePanel import NodeTreeInterfacePanel
class NodeTreeInterfaceItem(bpy_struct):
    item_type: str
    parent: 'NodeTreeInterfacePanel'
    position: int
    index: int