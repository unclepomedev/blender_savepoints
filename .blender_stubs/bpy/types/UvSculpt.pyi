# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UvSculpt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class UvSculpt(bpy_struct):

    size: Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1", "is_animatable=False"]

    strength: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]

    @property
    def curve_distance_falloff(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:

        ...
    curve_distance_falloff_preset: Annotated[Literal['CUSTOM', 'SMOOTH', 'SMOOTHER', 'SPHERE', 'ROOT', 'SHARP', 'LIN', 'POW4', 'INVSQUARE', 'CONSTANT'], "is_animatable=False"]
