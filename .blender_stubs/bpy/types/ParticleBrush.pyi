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

    size: Annotated[int, "subtype='PIXEL'", "step=10", "is_animatable=False"]
    """Radius of the brush in pixels"""
    strength: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Brush strength"""
    count: Annotated[int, "step=10", "is_animatable=False"]
    """Particle count"""
    steps: Annotated[int, "step=10", "is_animatable=False"]
    """Brush steps"""
    puff_mode: Annotated[Literal['ADD', 'SUB'], "is_animatable=False"]

    use_puff_volume: Annotated[bool, "is_animatable=False"]
    """Apply puff to unselected end-points (helps maintain hair volume when puffing root)"""
    length_mode: Annotated[Literal['GROW', 'SHRINK'], "is_animatable=False"]

    @property
    def curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:

        ...