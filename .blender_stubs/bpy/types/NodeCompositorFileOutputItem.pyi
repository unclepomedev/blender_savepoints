# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodeCompositorFileOutputItem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ImageFormatSettings import ImageFormatSettings

class NodeCompositorFileOutputItem(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def socket_type(self) -> Annotated[Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE'], "is_animatable=False"]:

        ...
    @socket_type.setter
    def socket_type(self, value: Annotated[Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE'], "is_animatable=False"]):
        ...
    @property
    def vector_socket_dimensions(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Dimensions of the vector socket"""
        ...
    @vector_socket_dimensions.setter
    def vector_socket_dimensions(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the corresponding socket type in the node editor"""
        ...
    @property
    def override_node_format(self) -> bool:
        """Use a different format instead of the node format for this file"""
        ...
    @override_node_format.setter
    def override_node_format(self, value: bool):
        ...
    @property
    def save_as_render(self) -> bool:
        """Apply render part of display transform when saving byte image"""
        ...
    @save_as_render.setter
    def save_as_render(self, value: bool):
        ...
    @property
    def format(self) -> Annotated[Optional['ImageFormatSettings'], "is_animatable=False"]:

        ...