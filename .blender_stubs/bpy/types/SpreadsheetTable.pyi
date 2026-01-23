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
from .SpreadsheetColumn import SpreadsheetColumn
from .SpreadsheetTableID import SpreadsheetTableID
class SpreadsheetTable(bpy_struct):
    id: 'SpreadsheetTableID'
    columns: bpy_prop_collection['SpreadsheetColumn']