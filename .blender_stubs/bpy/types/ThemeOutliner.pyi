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
    match: float
    selected_highlight: float
    active: float
    selected_object: float
    active_object: float
    edited_object: float
    row_alternate: float