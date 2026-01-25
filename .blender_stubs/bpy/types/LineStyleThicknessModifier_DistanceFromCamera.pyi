# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleThicknessModifier import LineStyleThicknessModifier
from .CurveMapping import CurveMapping
class LineStyleThicknessModifier_DistanceFromCamera(LineStyleThicknessModifier):
    name: str
    type: str
    blend: str
    influence: float
    use: bool
    expanded: bool
    mapping: str
    invert: bool
    curve: 'CurveMapping'
    range_min: float
    range_max: float
    value_min: float
    value_max: float