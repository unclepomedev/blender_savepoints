# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ColorRampElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ColorRampElement(bpy_struct):

    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Set color of selected color stop"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def alpha(self) -> Annotated[float, "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Set alpha of selected color stop"""
        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def position(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Set position of selected color stop"""
        ...
    @position.setter
    def position(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...