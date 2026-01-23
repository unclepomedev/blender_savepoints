# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping
class ParticleBrush(bpy_struct):
    size: int
    strength: float
    count: int
    steps: int
    puff_mode: str
    use_puff_volume: bool
    length_mode: str
    curve: 'CurveMapping'