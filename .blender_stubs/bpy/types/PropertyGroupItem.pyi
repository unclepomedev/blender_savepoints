# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ID import ID
from .PropertyGroup import PropertyGroup
class PropertyGroupItem(bpy_struct):
    string: str
    int: int
    int_array: int
    float: float
    float_array: float
    double: float
    double_array: float
    bool: bool
    bool_array: bool
    enum: str
    group: 'PropertyGroup'
    collection: bpy_prop_collection['PropertyGroup']
    idp_array: bpy_prop_collection['PropertyGroup']
    id: 'ID'