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
from .ID import ID
from .PropertyGroup import PropertyGroup
class PropertyGroupItem(bpy_struct):
    string: Annotated[str, "is_animatable=False"]
    int: Annotated[int, "step=1"]
    int_array: Annotated[list[int], "step=1"]
    float: Annotated[float, "step=10.0", "precision=3"]
    float_array: Annotated[list[float], "step=10.0", "precision=3"]
    double: Annotated[float, "step=10.0", "precision=3"]
    double_array: Annotated[list[float], "step=10.0", "precision=3"]
    bool: bool
    bool_array: list[bool]
    enum: Literal['DEFAULT']
    @property
    def group(self) -> Annotated[Optional['PropertyGroup'], "is_animatable=False"]:
        ...
    @property
    def collection(self) -> Annotated[bpy_prop_collection['PropertyGroup'], "is_animatable=False"]:
        ...
    @property
    def idp_array(self) -> Annotated[bpy_prop_collection['PropertyGroup'], "is_animatable=False"]:
        ...
    id: Annotated[Optional['ID'], "is_animatable=False"]