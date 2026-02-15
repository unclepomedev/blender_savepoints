# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .CurveMap import CurveMap
class CurveMapping(bpy_struct):
    tone: Literal['STANDARD', 'FILMLIKE']
    """Tone of the curve"""
    use_clip: bool
    """Force the curve view to fit a defined boundary"""
    clip_min_x: Annotated[float, "step=10.0", "precision=3"]
    clip_min_y: Annotated[float, "step=10.0", "precision=3"]
    clip_max_x: Annotated[float, "step=10.0", "precision=3"]
    clip_max_y: Annotated[float, "step=10.0", "precision=3"]
    extend: Literal['HORIZONTAL', 'EXTRAPOLATED']
    """Extrapolate the curve or extend it horizontally"""
    @property
    def curves(self) -> Annotated[bpy_prop_collection['CurveMap'], "is_animatable=False"]:
        ...
    black_level: Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]
    """For RGB curves, the color that black is mapped to"""
    white_level: Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]
    """For RGB curves, the color that white is mapped to"""
    def update(self, *args, **kwargs) -> Any: ...
    def reset_view(self, *args, **kwargs) -> Any: ...
    def initialize(self, *args, **kwargs) -> Any: ...
    def evaluate(self, *args, **kwargs) -> Any: ...