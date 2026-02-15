# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OperatorStrokeElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .PropertyGroup import PropertyGroup

class OperatorStrokeElement(PropertyGroup):

    name: Annotated[str, "is_animatable=False"]
    """Unique name used in the code and scripting"""
    location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]

    mouse: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]

    mouse_event: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]

    pressure: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Tablet pressure"""
    size: Annotated[float, "step=10.0", "precision=3"]
    """Brush size in screen space"""
    x_tilt: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Pen tilt from left (-1.0) to right (+1.0)"""
    y_tilt: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Pen tilt from backward (-1.0) to forward (+1.0)"""
    time: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]

    is_start: bool

    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...