# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ArmatureEditBones.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .EditBone import EditBone

class ArmatureEditBones(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['EditBone'], "is_animatable=False"]:
        """Armatures active edit bone"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['EditBone'], "is_animatable=False"]):
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['EditBone']: ...
    def __getitem__(self, key: Union[str, int]) -> 'EditBone': ...
    def __len__(self) -> int: ...