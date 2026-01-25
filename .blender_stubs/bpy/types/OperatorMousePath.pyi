# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .PropertyGroup import PropertyGroup
class OperatorMousePath(PropertyGroup):
    name: str
    loc: float
    time: float
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...