# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FreestyleModuleSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Text import Text

class FreestyleModuleSettings(bpy_struct):

    @property
    def script(self) -> Annotated[Optional['Text'], "is_animatable=False"]:
        """Python script to define a style module"""
        ...
    @script.setter
    def script(self, value: Annotated[Optional['Text'], "is_animatable=False"]):
        ...
    @property
    def use(self) -> bool:
        """Enable or disable this style module during stroke rendering"""
        ...
    @use.setter
    def use(self, value: bool):
        ...