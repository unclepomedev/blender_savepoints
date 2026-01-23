# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleGeometryModifier import LineStyleGeometryModifier
class LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier):
    name: str
    type: str
    use: bool
    expanded: bool
    amplitude: float
    scale: float
    octaves: int
    smooth: bool
    use_pure_random: bool