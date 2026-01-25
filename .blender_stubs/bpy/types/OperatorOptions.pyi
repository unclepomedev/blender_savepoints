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
class OperatorOptions(bpy_struct):
    is_grab_cursor: bool
    is_invoke: bool
    is_repeat: bool
    is_repeat_last: bool
    use_cursor_region: bool