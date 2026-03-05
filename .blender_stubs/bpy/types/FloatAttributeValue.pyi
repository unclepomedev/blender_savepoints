# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FloatAttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FloatAttributeValue(bpy_struct):

    @property
    def value(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @value.setter
    def value(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...