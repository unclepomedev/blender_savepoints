# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskSplines.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MaskSpline import MaskSpline
from .MaskSplinePoint import MaskSplinePoint

class MaskSplines(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['MaskSpline'], "is_animatable=False"]:
        """Active spline of masking layer"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['MaskSpline'], "is_animatable=False"]):
        ...
    @property
    def active_point(self) -> Annotated[Optional['MaskSplinePoint'], "is_animatable=False"]:
        """Active point of masking layer"""
        ...
    @active_point.setter
    def active_point(self, value: Annotated[Optional['MaskSplinePoint'], "is_animatable=False"]):
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MaskSpline']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MaskSpline': ...
    def __len__(self) -> int: ...