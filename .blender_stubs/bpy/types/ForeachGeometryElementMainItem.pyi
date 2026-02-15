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
class ForeachGeometryElementMainItem(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    socket_type: Annotated[Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE'], "is_animatable=False"]
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the corresponding socket type in the node editor"""
        ...