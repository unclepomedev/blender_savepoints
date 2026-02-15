# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class UnitSettings(bpy_struct):
    system: Annotated[Literal['NONE', 'METRIC', 'IMPERIAL'], "is_animatable=False"]
    """The unit system to use for user interface controls"""
    system_rotation: Annotated[Literal['DEGREES', 'RADIANS'], "is_animatable=False"]
    """Unit to use for displaying/editing rotation values"""
    scale_length: Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=6", "is_animatable=False"]
    """Scale to use when converting between Blender units and dimensions. When working at microscopic or astronomical scale, a small or large unit scale respectively can be used to avoid numerical precision problems"""
    use_separate: Annotated[bool, "is_animatable=False"]
    """Display units in pairs (e.g. 1m 0cm)"""
    length_unit: Annotated[Literal['DEFAULT'], "is_animatable=False"]
    """Unit that will be used to display length values"""
    mass_unit: Annotated[Literal['DEFAULT'], "is_animatable=False"]
    """Unit that will be used to display mass values"""
    time_unit: Annotated[Literal['DEFAULT'], "is_animatable=False"]
    """Unit that will be used to display time values"""
    temperature_unit: Annotated[Literal['DEFAULT'], "is_animatable=False"]
    """Unit that will be used to display temperature values"""