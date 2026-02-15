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
class NodeSocket(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Socket name"""
    @property
    def label(self) -> Annotated[str, "is_animatable=False"]:
        """Custom dynamic defined socket label"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique identifier for mapping sockets"""
        ...
    description: Annotated[str, "is_animatable=False"]
    """Socket tooltip"""
    @property
    def is_output(self) -> bool:
        """True if the socket is an output, otherwise input"""
        ...
    @property
    def select(self) -> bool:
        """True if the socket is selected"""
        ...
    hide: bool
    """Hide the socket"""
    enabled: bool
    """Enable the socket"""
    link_limit: Annotated[int, "step=1"]
    """Max number of links allowed for this socket"""
    @property
    def is_linked(self) -> bool:
        """True if the socket is connected"""
        ...
    @property
    def is_unavailable(self) -> bool:
        """True if the socket is unavailable"""
        ...
    @property
    def is_multi_input(self) -> bool:
        """True if the socket can accept multiple ordered input links"""
        ...
    show_expanded: bool
    """Socket links are expanded in the user interface"""
    @property
    def is_inactive(self) -> bool:
        """Socket is grayed out because it has been detected to not have any effect on the output"""
        ...
    @property
    def is_icon_visible(self) -> bool:
        """Socket is drawn as interactive icon in the node editor"""
        ...
    hide_value: bool
    """Hide the socket input value"""
    pin_gizmo: Annotated[bool, "is_animatable=False"]
    """Keep gizmo visible even when the node is not selected"""
    @property
    def node(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        """Node owning this socket"""
        ...
    type: Literal['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'MENU', 'BUNDLE', 'CLOSURE']
    """Data type"""
    display_shape: Literal['CIRCLE', 'SQUARE', 'DIAMOND', 'CIRCLE_DOT', 'SQUARE_DOT', 'DIAMOND_DOT', 'LINE', 'VOLUME_GRID', 'LIST']
    """Socket shape"""
    @property
    def inferred_structure_type(self) -> Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']:
        """Best known structure type of the socket. This may not match the socket shape, e.g. for unlinked input sockets"""
        ...
    bl_idname: Annotated[str, "is_animatable=False"]
    bl_label: Annotated[str, "is_animatable=False"]
    """Label to display for the socket type in the UI"""
    bl_subtype_label: Annotated[str, "is_animatable=False"]
    """Label to display for the socket subtype in the UI"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_color(self, *args, **kwargs) -> Any: ...
    def draw_color_simple(self, *args, **kwargs) -> Any: ...