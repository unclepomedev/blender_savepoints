# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshUVLoop.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshUVLoop(bpy_struct):

    @property
    def uv(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @uv.setter
    def uv(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pin_uv(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @pin_uv.setter
    def pin_uv(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...