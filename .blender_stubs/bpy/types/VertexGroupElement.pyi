# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VertexGroupElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class VertexGroupElement(bpy_struct):

    @property
    def group(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @property
    def weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Vertex Weight"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...