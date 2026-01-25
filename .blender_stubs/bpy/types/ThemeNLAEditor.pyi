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
class ThemeNLAEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: list[float]
    active_action: list[float]
    active_action_unset: list[float]
    strips: list[float]
    strips_selected: list[float]
    transition_strips: list[float]
    transition_strips_selected: list[float]
    meta_strips: list[float]
    meta_strips_selected: list[float]
    sound_strips: list[float]
    sound_strips_selected: list[float]
    tweak: list[float]
    tweak_duplicate: list[float]
    keyframe_border: list[float]
    keyframe_border_selected: list[float]