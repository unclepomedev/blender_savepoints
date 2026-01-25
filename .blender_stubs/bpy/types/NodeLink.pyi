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
from .Node import Node
from .NodeSocket import NodeSocket
class NodeLink(bpy_struct):
    is_valid: bool
    is_muted: bool
    from_node: 'Node'
    to_node: 'Node'
    from_socket: 'NodeSocket'
    to_socket: 'NodeSocket'
    is_hidden: bool
    multi_input_sort_id: int
    def swap_multi_input_sort_id(self, *args, **kwargs) -> Any: ...