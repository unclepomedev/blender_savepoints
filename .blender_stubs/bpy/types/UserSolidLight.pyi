# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UserSolidLight.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UserSolidLight(bpy_struct):

    @property
    def use(self) -> bool:
        """Enable this light in solid shading mode"""
        ...
    @use.setter
    def use(self, value: bool):
        ...
    @property
    def smooth(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Smooth the lighting from this light"""
        ...
    @smooth.setter
    def smooth(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def direction(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]:
        """Direction that the light is shining"""
        ...
    @direction.setter
    def direction(self, value: Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]):
        ...
    @property
    def specular_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the light's specular highlight"""
        ...
    @specular_color.setter
    def specular_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def diffuse_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the light's diffuse highlight"""
        ...
    @diffuse_color.setter
    def diffuse_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...