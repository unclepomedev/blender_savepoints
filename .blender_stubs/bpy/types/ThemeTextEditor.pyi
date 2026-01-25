# Blender Probe Generated Stub for Blender 5.0.1
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
class ThemeTextEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    line_numbers: list[float]
    line_numbers_background: list[float]
    selected_text: list[float]
    cursor: list[float]
    syntax_builtin: list[float]
    syntax_symbols: list[float]
    syntax_special: list[float]
    syntax_preprocessor: list[float]
    syntax_reserved: list[float]
    syntax_comment: list[float]
    syntax_string: list[float]
    syntax_numbers: list[float]