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
from .CurveMap import CurveMap
class CurveMapping(bpy_struct):
    tone: str
    use_clip: bool
    clip_min_x: float
    clip_min_y: float
    clip_max_x: float
    clip_max_y: float
    extend: str
    curves: bpy_prop_collection['CurveMap']
    black_level: float
    white_level: float
    def update(self, *args, **kwargs) -> Any: ...
    def reset_view(self, *args, **kwargs) -> Any: ...
    def initialize(self, *args, **kwargs) -> Any: ...
    def evaluate(self, *args, **kwargs) -> Any: ...