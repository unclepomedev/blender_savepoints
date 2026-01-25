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
    lift: list[float]
    gamma: list[float]
    gain: list[float]
    slope: list[float]
    offset: list[float]
    power: list[float]
    invert_lift: bool
    invert_gamma: bool
    invert_gain: bool
    invert_slope: bool
    invert_offset: bool
    invert_power: bool