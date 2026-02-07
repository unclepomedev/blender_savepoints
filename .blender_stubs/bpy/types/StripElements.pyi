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
from .StripElement import StripElement
class StripElements(bpy_struct):
    def append(self, *args, **kwargs) -> Any: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['StripElement']: ...
    def __getitem__(self, key: Union[str, int]) -> 'StripElement': ...
    def __len__(self) -> int: ...