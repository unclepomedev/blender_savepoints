# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilLayerMask.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class GreasePencilLayerMask(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Mask layer name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def hide(self) -> bool:
        """Set mask Visibility"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def invert(self) -> bool:
        """Invert mask"""
        ...
    @invert.setter
    def invert(self, value: bool):
        ...