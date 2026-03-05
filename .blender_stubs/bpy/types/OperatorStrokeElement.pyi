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

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mouse(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @mouse.setter
    def mouse(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mouse_event(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @mouse_event.setter
    def mouse_event(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pressure(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Tablet pressure"""
        ...
    @pressure.setter
    def pressure(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Brush size in screen space"""
        ...
    @size.setter
    def size(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def x_tilt(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Pen tilt from left (-1.0) to right (+1.0)"""
        ...
    @x_tilt.setter
    def x_tilt(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def y_tilt(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Pen tilt from backward (-1.0) to forward (+1.0)"""
        ...
    @y_tilt.setter
    def y_tilt(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def time(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:

        ...
    @time.setter
    def time(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def is_start(self) -> bool:

        ...
    @is_start.setter
    def is_start(self, value: bool) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...