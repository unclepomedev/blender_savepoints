# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FloatVectorAttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FloatVectorAttributeValue(bpy_struct):

    @property
    def vector(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """3D vector"""
        ...
    @vector.setter
    def vector(self, value: Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]):
        ...