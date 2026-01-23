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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeConsole(bpy_struct):
    space: 'ThemeSpaceGeneric'
    line_output: list[float]
    line_input: list[float]
    line_info: list[float]
    line_error: list[float]
    cursor: list[float]
    select: list[float]