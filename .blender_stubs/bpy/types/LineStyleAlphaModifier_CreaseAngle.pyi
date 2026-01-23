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
class LineStyleAlphaModifier_CreaseAngle(LineStyleAlphaModifier):
    name: str
    type: str
    blend: str
    influence: float
    use: bool
    expanded: bool
    mapping: str
    invert: bool
    curve: 'CurveMapping'
    angle_min: float
    angle_max: float