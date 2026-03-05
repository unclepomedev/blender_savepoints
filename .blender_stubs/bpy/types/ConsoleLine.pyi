# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ConsoleLine.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ConsoleLine(bpy_struct):

    @property
    def body(self) -> Annotated[str, "is_animatable=False"]:
        """Text in the line"""
        ...
    @body.setter
    def body(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def current_character(self) -> Annotated[int, "step=1"]:

        ...
    @current_character.setter
    def current_character(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def type(self) -> Literal['OUTPUT', 'INPUT', 'INFO', 'ERROR']:
        """Console line type when used in scrollback"""
        ...
    @type.setter
    def type(self, value: Literal['OUTPUT', 'INPUT', 'INFO', 'ERROR']):
        ...