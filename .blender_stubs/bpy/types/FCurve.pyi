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
from .ActionGroup import ActionGroup
from .Driver import Driver
from .FCurveSample import FCurveSample
from .FModifier import FModifier
from .Keyframe import Keyframe
class FCurve(bpy_struct):
    extrapolation: str
    driver: 'Driver'
    group: 'ActionGroup'
    data_path: str
    array_index: int
    color_mode: str
    color: list[float]
    select: bool
    lock: bool
    mute: bool
    hide: bool
    auto_smoothing: str
    is_valid: bool
    is_empty: bool
    sampled_points: bpy_prop_collection['FCurveSample']
    keyframe_points: bpy_prop_collection['Keyframe']
    modifiers: bpy_prop_collection['FModifier']
    def evaluate(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def range(self, *args, **kwargs) -> Any: ...
    def update_autoflags(self, *args, **kwargs) -> Any: ...
    def convert_to_samples(self, *args, **kwargs) -> Any: ...
    def convert_to_keyframes(self, *args, **kwargs) -> Any: ...
    def bake(self, *args, **kwargs) -> Any: ...