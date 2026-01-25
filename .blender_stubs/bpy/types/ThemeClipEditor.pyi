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
class ThemeClipEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: float
    marker_outline: float
    marker: float
    active_marker: float
    selected_marker: float
    disabled_marker: float
    locked_marker: float
    path_before: float
    path_after: float
    path_keyframe_before: float
    path_keyframe_after: float
    metadatabg: float
    metadatatext: float