# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpreadsheetRowFilter.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SpreadsheetRowFilter(bpy_struct):

    enabled: bool

    show_expanded: bool

    column_name: Annotated[str, "is_animatable=False"]

    operation: Literal['EQUAL', 'GREATER', 'LESS']

    value_float: Annotated[float, "step=10.0", "precision=3"]

    value_float2: Annotated[list[float], "step=10.0", "precision=3"]

    value_float3: Annotated[list[float], "step=10.0", "precision=3"]

    value_color: Annotated[list[float], "step=10.0", "precision=3"]

    value_string: Annotated[str, "is_animatable=False"]

    threshold: Annotated[float, "step=10.0", "precision=3"]
    """How close float values need to be to be equal"""
    value_int: Annotated[int, "step=1"]

    value_int8: Annotated[int, "step=1"]

    value_int2: Annotated[list[int], "step=1"]

    value_int3: Annotated[list[int], "step=1"]

    value_boolean: bool
