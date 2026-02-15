# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .StripColorBalanceData import StripColorBalanceData
class StripColorBalance(StripColorBalanceData):
    correction_method: Literal['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE']
    lift: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Color balance lift (shadows)"""
    gamma: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Color balance gamma (midtones)"""
    gain: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Color balance gain (highlights)"""
    slope: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Correction for highlights"""
    offset: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Correction for entire tonal range"""
    power: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=0.10000000149011612", "precision=3"]
    """Correction for midtones"""
    invert_lift: bool
    """Invert the lift color"""
    invert_gamma: bool
    """Invert the gamma color"""
    invert_gain: bool
    """Invert the gain color"""
    invert_slope: bool
    """Invert the slope color"""
    invert_offset: bool
    """Invert the offset color"""
    invert_power: bool
    """Invert the power color"""