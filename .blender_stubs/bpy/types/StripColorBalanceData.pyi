# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class StripColorBalanceData(bpy_struct):
    correction_method: str
    lift: float
    gamma: float
    gain: float
    slope: float
    offset: float
    power: float
    invert_lift: bool
    invert_gamma: bool
    invert_gain: bool
    invert_slope: bool
    invert_offset: bool
    invert_power: bool