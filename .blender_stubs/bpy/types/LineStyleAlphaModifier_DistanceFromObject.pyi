# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleAlphaModifier import LineStyleAlphaModifier
from .CurveMapping import CurveMapping
from .Object import Object
class LineStyleAlphaModifier_DistanceFromObject(LineStyleAlphaModifier):
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
    target: 'Object'