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
from .SpreadsheetColumn import SpreadsheetColumn
from .SpreadsheetTableID import SpreadsheetTableID
class SpreadsheetTable(bpy_struct):
    @property
    def id(self) -> Annotated[Optional['SpreadsheetTableID'], "is_animatable=False"]:
        """Data used to identify the table"""
        ...
    @property
    def columns(self) -> Annotated[bpy_prop_collection['SpreadsheetColumn'], "is_animatable=False"]:
        """Columns within the table"""
        ...