# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PropertyGroupItem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID
from .PropertyGroup import PropertyGroup
from .bpy_prop_collection import bpy_prop_collection

class PropertyGroupItem(bpy_struct):

    @property
    def string(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @string.setter
    def string(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def int(self) -> Annotated[int, "step=1"]:

        ...
    @int.setter
    def int(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def int_array(self) -> Annotated[list[int], "step=1"]:

        ...
    @int_array.setter
    def int_array(self, value: Annotated[list[int], "step=1"]):
        ...
    @property
    def float(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @float.setter
    def float(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def float_array(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @float_array.setter
    def float_array(self, value: Annotated[list[float], "step=10.0", "precision=3"]):
        ...
    @property
    def double(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @double.setter
    def double(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def double_array(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @double_array.setter
    def double_array(self, value: Annotated[list[float], "step=10.0", "precision=3"]):
        ...
    @property
    def bool(self) -> bool:

        ...
    @bool.setter
    def bool(self, value: bool):
        ...
    @property
    def bool_array(self) -> list[bool]:

        ...
    @bool_array.setter
    def bool_array(self, value: list[bool]):
        ...
    @property
    def enum(self) -> Literal['DEFAULT']:

        ...
    @enum.setter
    def enum(self, value: Literal['DEFAULT']):
        ...
    @property
    def group(self) -> Annotated[Optional['PropertyGroup'], "is_animatable=False"]:

        ...
    @property
    def collection(self) -> Annotated[bpy_prop_collection['PropertyGroup'], "is_animatable=False"]:

        ...
    @property
    def idp_array(self) -> Annotated[bpy_prop_collection['PropertyGroup'], "is_animatable=False"]:

        ...
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:

        ...
    @id.setter
    def id(self, value: Annotated[Optional['ID'], "is_animatable=False"]):
        ...