# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UVProjector.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class UVProjector(bpy_struct):

    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to use as projector transform"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...