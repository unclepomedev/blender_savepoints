# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectDisplay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ObjectDisplay(bpy_struct):

    @property
    def show_shadows(self) -> Annotated[bool, "is_animatable=False"]:
        """Object cast shadows in the 3D viewport"""
        ...
    @show_shadows.setter
    def show_shadows(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...