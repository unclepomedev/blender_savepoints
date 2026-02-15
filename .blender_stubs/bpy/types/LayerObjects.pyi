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
from .Object import Object
class LayerObjects(bpy_struct):
    active: Annotated[Optional['Object'], "is_animatable=False"]
    """Active object for this layer"""
    @property
    def selected(self) -> Annotated[bpy_prop_collection['Object'], "is_animatable=False"]:
        """All the selected objects of this layer"""
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Object']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Object': ...
    def __len__(self) -> int: ...