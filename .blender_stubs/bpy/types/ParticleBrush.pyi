# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleBrush.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class ParticleBrush(bpy_struct):

    @property
    def size(self) -> Annotated[int, "subtype='PIXEL'", "step=10", "is_animatable=False"]:
        """Radius of the brush in pixels"""
        ...
    @size.setter
    def size(self, value: Annotated[int, "subtype='PIXEL'", "step=10", "is_animatable=False"]) -> None:
        ...
    @property
    def strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Brush strength"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def count(self) -> Annotated[int, "step=10", "is_animatable=False"]:
        """Particle count"""
        ...
    @count.setter
    def count(self, value: Annotated[int, "step=10", "is_animatable=False"]) -> None:
        ...
    @property
    def steps(self) -> Annotated[int, "step=10", "is_animatable=False"]:
        """Brush steps"""
        ...
    @steps.setter
    def steps(self, value: Annotated[int, "step=10", "is_animatable=False"]) -> None:
        ...
    @property
    def puff_mode(self) -> Annotated[Literal['ADD', 'SUB'], "is_animatable=False"]:

        ...
    @puff_mode.setter
    def puff_mode(self, value: Annotated[Literal['ADD', 'SUB'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_puff_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """Apply puff to unselected end-points (helps maintain hair volume when puffing root)"""
        ...
    @use_puff_volume.setter
    def use_puff_volume(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def length_mode(self) -> Annotated[Literal['GROW', 'SHRINK'], "is_animatable=False"]:

        ...
    @length_mode.setter
    def length_mode(self, value: Annotated[Literal['GROW', 'SHRINK'], "is_animatable=False"]) -> None:
        ...
    @property
    def curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:

        ...