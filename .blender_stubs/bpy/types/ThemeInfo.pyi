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
class ThemeInfo(bpy_struct):
    space: 'ThemeSpaceGeneric'
    info_selected: float
    info_selected_text: float
    info_error_text: float
    info_warning_text: float
    info_info_text: float
    info_debug: float
    info_debug_text: float
    info_property: float
    info_property_text: float
    info_operator: float
    info_operator_text: float