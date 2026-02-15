# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .PropertyGroup import PropertyGroup
class OperatorMousePath(PropertyGroup):
    name: Annotated[str, "is_animatable=False"]
    """Unique name used in the code and scripting"""
    loc: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Mouse location"""
    time: Annotated[float, "step=10.0", "precision=3"]
    """Time of mouse location"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...