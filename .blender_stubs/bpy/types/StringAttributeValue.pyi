# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StringAttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StringAttributeValue(bpy_struct):

    @property
    def value(self) -> Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]:

        ...
    @value.setter
    def value(self, value: Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]):
        ...