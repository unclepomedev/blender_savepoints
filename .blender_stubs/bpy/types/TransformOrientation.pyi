# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TransformOrientation.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TransformOrientation(bpy_struct):

    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @matrix.setter
    def matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the custom transform orientation"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...