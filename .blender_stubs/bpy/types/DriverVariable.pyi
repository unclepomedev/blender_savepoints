# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .DriverTarget import DriverTarget
class DriverVariable(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name to use in scripted expressions/functions (no spaces or dots are allowed, and must start with a letter)"""
    type: Literal['SINGLE_PROP', 'TRANSFORMS', 'ROTATION_DIFF', 'LOC_DIFF', 'CONTEXT_PROP']
    """Driver variable type"""
    @property
    def targets(self) -> Annotated[bpy_prop_collection['DriverTarget'], "is_animatable=False"]:
        """Sources of input data for evaluating this variable"""
        ...
    @property
    def is_name_valid(self) -> bool:
        """Is this a valid name for a driver variable"""
        ...