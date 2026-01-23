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
class ColorManagedViewSettings(bpy_struct):
    look: str
    view_transform: str
    exposure: float
    gamma: float
    curve_mapping: 'CurveMapping'
    use_curve_mapping: bool
    use_white_balance: bool
    white_balance_temperature: float
    white_balance_tint: float
    white_balance_whitepoint: list[float]
    is_hdr: bool
    support_emulation: bool