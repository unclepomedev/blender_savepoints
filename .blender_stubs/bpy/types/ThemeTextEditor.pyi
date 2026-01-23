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
class ThemeTextEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    line_numbers: float
    line_numbers_background: float
    selected_text: float
    cursor: float
    syntax_builtin: float
    syntax_symbols: float
    syntax_special: float
    syntax_preprocessor: float
    syntax_reserved: float
    syntax_comment: float
    syntax_string: float
    syntax_numbers: float