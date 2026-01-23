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
class ThemeClipEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: list[float]
    marker_outline: list[float]
    marker: list[float]
    active_marker: list[float]
    selected_marker: list[float]
    disabled_marker: list[float]
    locked_marker: list[float]
    path_before: list[float]
    path_after: list[float]
    path_keyframe_before: list[float]
    path_keyframe_after: list[float]
    metadatabg: list[float]
    metadatatext: list[float]