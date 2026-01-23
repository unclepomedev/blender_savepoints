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
class UnitSettings(bpy_struct):
    system: str
    system_rotation: str
    scale_length: float
    use_separate: bool
    length_unit: str
    mass_unit: str
    time_unit: str
    temperature_unit: str