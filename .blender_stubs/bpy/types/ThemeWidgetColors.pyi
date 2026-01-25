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
class ThemeWidgetColors(bpy_struct):
    outline: list[float]
    outline_sel: list[float]
    inner: list[float]
    inner_sel: list[float]
    item: list[float]
    text: list[float]
    text_sel: list[float]
    show_shaded: bool
    shadetop: int
    shadedown: int
    roundness: float