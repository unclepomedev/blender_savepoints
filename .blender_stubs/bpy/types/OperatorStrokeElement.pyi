# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .PropertyGroup import PropertyGroup
class OperatorStrokeElement(PropertyGroup):
    name: str
    location: float
    mouse: float
    mouse_event: float
    pressure: float
    size: float
    x_tilt: float
    y_tilt: float
    time: float
    is_start: bool
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...