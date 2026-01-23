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
class SpreadsheetRowFilter(bpy_struct):
    enabled: bool
    show_expanded: bool
    column_name: str
    operation: str
    value_float: float
    value_float2: list[float]
    value_float3: list[float]
    value_color: list[float]
    value_string: str
    threshold: float
    value_int: int
    value_int8: int
    value_int2: list[int]
    value_int3: list[int]
    value_boolean: bool