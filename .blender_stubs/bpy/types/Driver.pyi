# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Driver.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ChannelDriverVariables import ChannelDriverVariables
from .DriverVariable import DriverVariable
from .bpy_prop_collection import bpy_prop_collection

class Driver(bpy_struct):

    type: Literal['AVERAGE', 'SUM', 'SCRIPTED', 'MIN', 'MAX']
    """Driver type"""
    expression: Annotated[str, "is_animatable=False"]
    """Expression to use for Scripted Expression"""
    @property
    def variables(self) -> Annotated['ChannelDriverVariables', "is_animatable=False"]:
        """Properties acting as inputs for this driver"""
        ...
    use_self: bool
    """Include a 'self' variable in the name-space, so drivers can easily reference the data being modified (object, bone, etc...)"""
    is_valid: bool
    """Driver could not be evaluated in past, so should be skipped"""
    @property
    def is_simple_expression(self) -> bool:
        """The scripted expression can be evaluated without using the full Python interpreter"""
        ...