# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectBase.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class ObjectBase(bpy_struct):

    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object this base links to"""
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:
        """Object base selection state"""
        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def hide_viewport(self) -> Annotated[bool, "is_animatable=False"]:
        """Temporarily hide in viewport"""
        ...
    @hide_viewport.setter
    def hide_viewport(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...