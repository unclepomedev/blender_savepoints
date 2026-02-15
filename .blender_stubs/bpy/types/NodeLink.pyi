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
from .Node import Node
from .NodeSocket import NodeSocket
class NodeLink(bpy_struct):
    is_valid: bool
    """Link is valid"""
    is_muted: bool
    """Link is muted and can be ignored"""
    @property
    def from_node(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        ...
    @property
    def to_node(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        ...
    @property
    def from_socket(self) -> Annotated[Optional['NodeSocket'], "is_animatable=False"]:
        ...
    @property
    def to_socket(self) -> Annotated[Optional['NodeSocket'], "is_animatable=False"]:
        ...
    @property
    def is_hidden(self) -> bool:
        """Link is hidden due to invisible sockets"""
        ...
    @property
    def multi_input_sort_id(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Used to sort multiple links coming into the same input. The highest ID is at the top."""
        ...
    def swap_multi_input_sort_id(self, *args, **kwargs) -> Any: ...