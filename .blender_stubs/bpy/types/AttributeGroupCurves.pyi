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
from .Attribute import Attribute
class AttributeGroupCurves(bpy_struct):
    active: Annotated[Optional['Attribute'], "is_animatable=False"]
    """Active attribute"""
    active_index: Annotated[int, "step=1", "is_animatable=False"]
    """Active attribute index or -1 when none are active"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def domain_size(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Attribute']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Attribute': ...
    def __len__(self) -> int: ...