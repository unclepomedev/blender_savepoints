# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Float4x4AttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Float4x4AttributeValue(bpy_struct):

    @property
    def value(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Matrix"""
        ...
    @value.setter
    def value(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...