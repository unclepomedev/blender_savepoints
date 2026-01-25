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
class UDIMTile(bpy_struct):
    label: str
    number: int
    size: list[int]
    channels: int
    generated_type: str
    generated_width: int
    generated_height: int
    use_generated_float: bool
    is_generated_tile: bool
    generated_color: list[float]