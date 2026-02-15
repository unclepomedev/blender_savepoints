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
from .FreestyleLineSet import FreestyleLineSet
class Linesets(bpy_struct):
    @property
    def active(self) -> Annotated[Optional['FreestyleLineSet'], "is_animatable=False"]:
        """Active line set being displayed"""
        ...
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active line set slot"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['FreestyleLineSet']: ...
    def __getitem__(self, key: Union[str, int]) -> 'FreestyleLineSet': ...
    def __len__(self) -> int: ...