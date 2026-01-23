# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .NodeSocketStandard import NodeSocketStandard
from .Node import Node
class NodeSocketVector4D(NodeSocketStandard):
    name: str
    label: str
    identifier: str
    description: str
    is_output: bool
    select: bool
    hide: bool
    enabled: bool
    link_limit: int
    is_linked: bool
    is_unavailable: bool
    is_multi_input: bool
    show_expanded: bool
    is_inactive: bool
    is_icon_visible: bool
    hide_value: bool
    pin_gizmo: bool
    node: 'Node'
    type: str
    display_shape: str
    inferred_structure_type: str
    bl_idname: str
    bl_label: str
    bl_subtype_label: str
    default_value: float
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_color(self, *args, **kwargs) -> Any: ...
    def draw_color_simple(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_color(self, *args, **kwargs) -> Any: ...
    def draw_color_simple(self, *args, **kwargs) -> Any: ...