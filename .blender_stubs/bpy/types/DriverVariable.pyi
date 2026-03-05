# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DriverVariable.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .DriverTarget import DriverTarget
from .bpy_prop_collection import bpy_prop_collection

class DriverVariable(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name to use in scripted expressions/functions (no spaces or dots are allowed, and must start with a letter)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['SINGLE_PROP', 'TRANSFORMS', 'ROTATION_DIFF', 'LOC_DIFF', 'CONTEXT_PROP']:
        """Driver variable type"""
        ...
    @type.setter
    def type(self, value: Literal['SINGLE_PROP', 'TRANSFORMS', 'ROTATION_DIFF', 'LOC_DIFF', 'CONTEXT_PROP']):
        ...
    @property
    def targets(self) -> Annotated[bpy_prop_collection['DriverTarget'], "is_animatable=False"]:
        """Sources of input data for evaluating this variable"""
        ...
    @property
    def is_name_valid(self) -> bool:
        """Is this a valid name for a driver variable"""
        ...