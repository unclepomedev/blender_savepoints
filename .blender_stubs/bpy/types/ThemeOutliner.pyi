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
class ThemeOutliner(bpy_struct):
    space: 'ThemeSpaceGeneric'
    match: list[float]
    selected_highlight: list[float]
    active: list[float]
    selected_object: list[float]
    active_object: list[float]
    edited_object: list[float]
    row_alternate: list[float]