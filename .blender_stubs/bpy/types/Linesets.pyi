# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .FreestyleLineSet import FreestyleLineSet
class Linesets(bpy_struct):
    active: 'FreestyleLineSet'
    active_index: int
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['FreestyleLineSet']: ...
    def __getitem__(self, key: Union[str, int]) -> 'FreestyleLineSet': ...
    def __len__(self) -> int: ...