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
from .SpreadsheetTable import SpreadsheetTable
class SpreadsheetTables(bpy_struct):
    @property
    def active(self) -> Annotated[Optional['SpreadsheetTable'], "is_animatable=False"]:
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['SpreadsheetTable']: ...
    def __getitem__(self, key: Union[str, int]) -> 'SpreadsheetTable': ...
    def __len__(self) -> int: ...