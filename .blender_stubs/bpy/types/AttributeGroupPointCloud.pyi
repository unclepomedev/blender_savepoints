# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AttributeGroupPointCloud.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Attribute import Attribute

class AttributeGroupPointCloud(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['Attribute'], "is_animatable=False"]:
        """Active attribute"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['Attribute'], "is_animatable=False"]) -> None:
        ...
    @property
    def active_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Active attribute index or -1 when none are active"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def domain_size(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Attribute']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Attribute': ...
    def __len__(self) -> int: ...