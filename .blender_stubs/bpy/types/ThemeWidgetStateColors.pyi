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
class ThemeWidgetStateColors(bpy_struct):
    error: list[float]
    warning: list[float]
    info: list[float]
    success: list[float]
    inner_anim: list[float]
    inner_anim_sel: list[float]
    inner_key: list[float]
    inner_key_sel: list[float]
    inner_driven: list[float]
    inner_driven_sel: list[float]
    inner_overridden: list[float]
    inner_overridden_sel: list[float]
    inner_changed: list[float]
    inner_changed_sel: list[float]
    blend: float