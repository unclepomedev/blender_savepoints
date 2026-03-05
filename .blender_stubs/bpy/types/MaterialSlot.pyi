# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaterialSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Material import Material

class MaterialSlot(bpy_struct):

    @property
    def link(self) -> Annotated[Literal['OBJECT', 'DATA'], "is_animatable=False"]:
        """Link material to object or the object's data"""
        ...
    @link.setter
    def link(self, value: Annotated[Literal['OBJECT', 'DATA'], "is_animatable=False"]) -> None:
        ...
    @property
    def material(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material data-block used by this material slot"""
        ...
    @material.setter
    def material(self, value: Annotated[Optional['Material'], "is_animatable=False"]) -> None:
        ...
    @property
    def slot_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:

        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Material slot name"""
        ...