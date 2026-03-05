# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskParent.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID

class MaskParent(bpy_struct):

    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """ID-block to which masking element would be parented to or to its property"""
        ...
    @id.setter
    def id(self, value: Annotated[Optional['ID'], "is_animatable=False"]):
        ...
    @property
    def id_type(self) -> Literal['MOVIECLIP']:
        """Type of ID-block that can be used"""
        ...
    @id_type.setter
    def id_type(self, value: Literal['MOVIECLIP']):
        ...
    @property
    def type(self) -> Literal['POINT_TRACK', 'PLANE_TRACK']:
        """Parent Type"""
        ...
    @type.setter
    def type(self, value: Literal['POINT_TRACK', 'PLANE_TRACK']):
        ...
    @property
    def parent(self) -> Annotated[str, "is_animatable=False"]:
        """Name of parent object in specified data-block to which parenting happens"""
        ...
    @parent.setter
    def parent(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def sub_parent(self) -> Annotated[str, "is_animatable=False"]:
        """Name of parent sub-object in specified data-block to which parenting happens"""
        ...
    @sub_parent.setter
    def sub_parent(self, value: Annotated[str, "is_animatable=False"]):
        ...