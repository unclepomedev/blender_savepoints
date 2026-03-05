# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Addon.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AddonPreferences import AddonPreferences

class Addon(bpy_struct):

    @property
    def module(self) -> Annotated[str, "is_animatable=False"]:
        """Module name"""
        ...
    @module.setter
    def module(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def preferences(self) -> Annotated[Optional['AddonPreferences'], "is_animatable=False"]:

        ...