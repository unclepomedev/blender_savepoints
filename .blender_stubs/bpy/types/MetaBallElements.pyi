# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MetaBallElements.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MetaElement import MetaElement

class MetaBallElements(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['MetaElement'], "is_animatable=False"]:
        """Last selected element"""
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MetaElement']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MetaElement': ...
    def __len__(self) -> int: ...