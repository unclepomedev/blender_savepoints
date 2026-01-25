# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .NodeTreeInterfaceSocket import NodeTreeInterfaceSocket
from .NodeTreeInterfacePanel import NodeTreeInterfacePanel
class NodeTreeInterfaceSocketVectorTranslation2D(NodeTreeInterfaceSocket):
    item_type: str
    parent: 'NodeTreeInterfacePanel'
    position: int
    index: int
    name: str
    identifier: str
    description: str
    socket_type: str
    in_out: str
    hide_value: bool
    hide_in_modifier: bool
    force_non_field: bool
    is_inspect_output: bool
    is_panel_toggle: bool
    layer_selection_field: bool
    menu_expanded: bool
    optional_label: bool
    attribute_domain: str
    default_attribute_name: str
    structure_type: str
    default_input: str
    bl_socket_idname: str
    subtype: str
    dimensions: int
    default_value: float
    min_value: float
    max_value: float
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def init_socket(self, *args, **kwargs) -> Any: ...
    def from_socket(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def init_socket(self, *args, **kwargs) -> Any: ...
    def from_socket(self, *args, **kwargs) -> Any: ...