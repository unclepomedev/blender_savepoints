# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.EQCurveMappingData.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping

class EQCurveMappingData(bpy_struct):

    @property
    def curve_mapping(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:

        ...