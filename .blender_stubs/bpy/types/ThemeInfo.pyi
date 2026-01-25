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
class ThemeInfo(bpy_struct):
    space: 'ThemeSpaceGeneric'
    info_selected: list[float]
    info_selected_text: list[float]
    info_error_text: list[float]
    info_warning_text: list[float]
    info_info_text: list[float]
    info_debug: list[float]
    info_debug_text: list[float]
    info_property: list[float]
    info_property_text: list[float]
    info_operator: list[float]
    info_operator_text: list[float]