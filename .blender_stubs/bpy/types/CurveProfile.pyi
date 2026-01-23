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
from .CurveProfilePoint import CurveProfilePoint
class CurveProfile(bpy_struct):
    preset: str
    use_clip: bool
    use_sample_straight_edges: bool
    use_sample_even_lengths: bool
    points: bpy_prop_collection['CurveProfilePoint']
    segments: bpy_prop_collection['CurveProfilePoint']
    def update(self, *args, **kwargs) -> Any: ...
    def reset_view(self, *args, **kwargs) -> Any: ...
    def initialize(self, *args, **kwargs) -> Any: ...
    def evaluate(self, *args, **kwargs) -> Any: ...