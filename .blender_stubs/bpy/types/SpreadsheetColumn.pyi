# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpreadsheetColumn.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .SpreadsheetColumnID import SpreadsheetColumnID

class SpreadsheetColumn(bpy_struct):

    @property
    def data_type(self) -> Literal['INT32', 'FLOAT', 'BOOLEAN', 'INSTANCES']:
        """The data type of the corresponding column visible in the spreadsheet"""
        ...
    @property
    def id(self) -> Annotated[Optional['SpreadsheetColumnID'], "is_animatable=False"]:
        """Data used to identify the corresponding data from the data source"""
        ...