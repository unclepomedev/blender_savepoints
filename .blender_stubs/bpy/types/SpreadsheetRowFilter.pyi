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

    @property
    def enabled(self) -> bool:

        ...
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:

        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def column_name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @column_name.setter
    def column_name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def operation(self) -> Literal['EQUAL', 'GREATER', 'LESS']:

        ...
    @operation.setter
    def operation(self, value: Literal['EQUAL', 'GREATER', 'LESS']) -> None:
        ...
    @property
    def value_float(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @value_float.setter
    def value_float(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def value_float2(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @value_float2.setter
    def value_float2(self, value: Annotated[list[float], "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def value_float3(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @value_float3.setter
    def value_float3(self, value: Annotated[list[float], "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def value_color(self) -> Annotated[list[float], "step=10.0", "precision=3"]:

        ...
    @value_color.setter
    def value_color(self, value: Annotated[list[float], "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def value_string(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @value_string.setter
    def value_string(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def threshold(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How close float values need to be to be equal"""
        ...
    @threshold.setter
    def threshold(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def value_int(self) -> Annotated[int, "step=1"]:

        ...
    @value_int.setter
    def value_int(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def value_int8(self) -> Annotated[int, "step=1"]:

        ...
    @value_int8.setter
    def value_int8(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def value_int2(self) -> Annotated[list[int], "step=1"]:

        ...
    @value_int2.setter
    def value_int2(self, value: Annotated[list[int], "step=1"]) -> None:
        ...
    @property
    def value_int3(self) -> Annotated[list[int], "step=1"]:

        ...
    @value_int3.setter
    def value_int3(self, value: Annotated[list[int], "step=1"]) -> None:
        ...
    @property
    def value_boolean(self) -> bool:

        ...
    @value_boolean.setter
    def value_boolean(self, value: bool) -> None:
        ...