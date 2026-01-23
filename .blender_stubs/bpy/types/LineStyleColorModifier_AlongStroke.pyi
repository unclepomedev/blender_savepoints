# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleColorModifier import LineStyleColorModifier
from .ColorRamp import ColorRamp
class LineStyleColorModifier_AlongStroke(LineStyleColorModifier):
    name: str
    type: str
    blend: str
    influence: float
    use: bool
    expanded: bool
    color_ramp: 'ColorRamp'