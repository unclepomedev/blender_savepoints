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
class ConsoleLine(bpy_struct):
    body: Annotated[str, "is_animatable=False"]
    """Text in the line"""
    current_character: Annotated[int, "step=1"]
    type: Literal['OUTPUT', 'INPUT', 'INFO', 'ERROR']
    """Console line type when used in scrollback"""