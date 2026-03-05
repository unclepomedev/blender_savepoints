# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TransformOrientationSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .TransformOrientation import TransformOrientation

class TransformOrientationSlot(bpy_struct):

    @property
    def type(self) -> Annotated[Literal['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW', 'CURSOR', 'PARENT'], "is_animatable=False"]:
        """Transformation orientation"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW', 'CURSOR', 'PARENT'], "is_animatable=False"]):
        ...
    @property
    def custom_orientation(self) -> Annotated[Optional['TransformOrientation'], "is_animatable=False"]:

        ...
    @property
    def use(self) -> Annotated[bool, "is_animatable=False"]:
        """Use scene orientation instead of a custom setting"""
        ...
    @use.setter
    def use(self, value: Annotated[bool, "is_animatable=False"]):
        ...