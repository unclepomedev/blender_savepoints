# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodeSocketVectorTranslation4D.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .NodeSocketStandard import NodeSocketStandard
from .Node import Node

class NodeSocketVectorTranslation4D(NodeSocketStandard):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Socket name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def label(self) -> Annotated[str, "is_animatable=False"]:
        """Custom dynamic defined socket label"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique identifier for mapping sockets"""
        ...
    @property
    def description(self) -> Annotated[str, "is_animatable=False"]:
        """Socket tooltip"""
        ...
    @description.setter
    def description(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def is_output(self) -> bool:
        """True if the socket is an output, otherwise input"""
        ...
    @property
    def select(self) -> bool:
        """True if the socket is selected"""
        ...
    @property
    def hide(self) -> bool:
        """Hide the socket"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def enabled(self) -> bool:
        """Enable the socket"""
        ...
    @enabled.setter
    def enabled(self, value: bool):
        ...
    @property
    def link_limit(self) -> Annotated[int, "step=1"]:
        """Max number of links allowed for this socket"""
        ...
    @link_limit.setter
    def link_limit(self, value: Annotated[int, "step=1"]):
        ...
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
    @property
    def show_expanded(self) -> bool:
        """Socket links are expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_inactive(self) -> bool:
        """Socket is grayed out because it has been detected to not have any effect on the output"""
        ...
    @property
    def is_icon_visible(self) -> bool:
        """Socket is drawn as interactive icon in the node editor"""
        ...
    @property
    def hide_value(self) -> bool:
        """Hide the socket input value"""
        ...
    @hide_value.setter
    def hide_value(self, value: bool):
        ...
    @property
    def pin_gizmo(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep gizmo visible even when the node is not selected"""
        ...
    @pin_gizmo.setter
    def pin_gizmo(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def node(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        """Node owning this socket"""
        ...
    @property
    def type(self) -> Literal['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'MENU', 'BUNDLE', 'CLOSURE']:
        """Data type"""
        ...
    @type.setter
    def type(self, value: Literal['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'MENU', 'BUNDLE', 'CLOSURE']):
        ...
    @property
    def display_shape(self) -> Literal['CIRCLE', 'SQUARE', 'DIAMOND', 'CIRCLE_DOT', 'SQUARE_DOT', 'DIAMOND_DOT', 'LINE', 'VOLUME_GRID', 'LIST']:
        """Socket shape"""
        ...
    @display_shape.setter
    def display_shape(self, value: Literal['CIRCLE', 'SQUARE', 'DIAMOND', 'CIRCLE_DOT', 'SQUARE_DOT', 'DIAMOND_DOT', 'LINE', 'VOLUME_GRID', 'LIST']):
        ...
    @property
    def inferred_structure_type(self) -> Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']:
        """Best known structure type of the socket. This may not match the socket shape, e.g. for unlinked input sockets"""
        ...
    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:
        """Label to display for the socket type in the UI"""
        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_subtype_label(self) -> Annotated[str, "is_animatable=False"]:
        """Label to display for the socket subtype in the UI"""
        ...
    @bl_subtype_label.setter
    def bl_subtype_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def default_value(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Input value used for unconnected socket"""
        ...
    @default_value.setter
    def default_value(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_color(self, *args, **kwargs) -> Any: ...
    def draw_color_simple(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_color(self, *args, **kwargs) -> Any: ...
    def draw_color_simple(self, *args, **kwargs) -> Any: ...