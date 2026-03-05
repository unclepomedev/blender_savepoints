# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurveMapping.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMap import CurveMap
from .bpy_prop_collection import bpy_prop_collection

class CurveMapping(bpy_struct):

    @property
    def tone(self) -> Literal['STANDARD', 'FILMLIKE']:
        """Tone of the curve"""
        ...
    @tone.setter
    def tone(self, value: Literal['STANDARD', 'FILMLIKE']) -> None:
        ...
    @property
    def use_clip(self) -> bool:
        """Force the curve view to fit a defined boundary"""
        ...
    @use_clip.setter
    def use_clip(self, value: bool) -> None:
        ...
    @property
    def clip_min_x(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @clip_min_x.setter
    def clip_min_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_min_y(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @clip_min_y.setter
    def clip_min_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_max_x(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @clip_max_x.setter
    def clip_max_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_max_y(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @clip_max_y.setter
    def clip_max_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def extend(self) -> Literal['HORIZONTAL', 'EXTRAPOLATED']:
        """Extrapolate the curve or extend it horizontally"""
        ...
    @extend.setter
    def extend(self, value: Literal['HORIZONTAL', 'EXTRAPOLATED']) -> None:
        ...
    @property
    def curves(self) -> Annotated[bpy_prop_collection['CurveMap'], "is_animatable=False"]:

        ...
    @property
    def black_level(self) -> Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]:
        """For RGB curves, the color that black is mapped to"""
        ...
    @black_level.setter
    def black_level(self, value: Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def white_level(self) -> Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]:
        """For RGB curves, the color that white is mapped to"""
        ...
    @white_level.setter
    def white_level(self, value: Annotated[list[float], "subtype='COLOR'", "step=1.0", "precision=3"]) -> None:
        ...
    def update(self, *args, **kwargs) -> Any: ...
    def reset_view(self, *args, **kwargs) -> Any: ...
    def initialize(self, *args, **kwargs) -> Any: ...
    def evaluate(self, *args, **kwargs) -> Any: ...