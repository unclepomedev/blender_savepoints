# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AreaSpaces.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Space import Space

class AreaSpaces(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['Space'], "is_animatable=False"]:
        """Space currently being displayed in this area"""
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Space']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Space': ...
    def __len__(self) -> int: ...