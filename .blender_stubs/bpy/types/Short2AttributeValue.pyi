# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Short2AttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Short2AttributeValue(bpy_struct):

    @property
    def value(self) -> Annotated[list[int], "step=1"]:
        """2D vector"""
        ...
    @value.setter
    def value(self, value: Annotated[list[int], "step=1"]) -> None:
        ...