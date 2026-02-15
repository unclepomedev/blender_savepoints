# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodeInternalSocketTemplate.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class NodeInternalSocketTemplate(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the socket"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Identifier of the socket"""
        ...
    @property
    def type(self) -> Literal['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'MENU', 'BUNDLE', 'CLOSURE']:
        """Data type of the socket"""
        ...