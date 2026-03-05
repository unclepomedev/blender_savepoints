# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OperatorMousePath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .PropertyGroup import PropertyGroup

class OperatorMousePath(PropertyGroup):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def loc(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Mouse location"""
        ...
    @loc.setter
    def loc(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def time(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time of mouse location"""
        ...
    @time.setter
    def time(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...