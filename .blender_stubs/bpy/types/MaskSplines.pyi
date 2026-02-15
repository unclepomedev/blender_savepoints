# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .MaskSpline import MaskSpline
from .MaskSplinePoint import MaskSplinePoint
class MaskSplines(bpy_struct):
    active: Annotated[Optional['MaskSpline'], "is_animatable=False"]
    """Active spline of masking layer"""
    active_point: Annotated[Optional['MaskSplinePoint'], "is_animatable=False"]
    """Active point of masking layer"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MaskSpline']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MaskSpline': ...
    def __len__(self) -> int: ...