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
class ThemeNLAEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: float
    active_action: float
    active_action_unset: float
    strips: float
    strips_selected: float
    transition_strips: float
    transition_strips_selected: float
    meta_strips: float
    meta_strips_selected: float
    sound_strips: float
    sound_strips_selected: float
    tweak: float
    tweak_duplicate: float
    keyframe_border: float
    keyframe_border_selected: float