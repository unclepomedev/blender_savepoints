# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodesModifierBakeDataBlocks.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .NodesModifierDataBlock import NodesModifierDataBlock

class NodesModifierBakeDataBlocks(bpy_struct):

    @property
    def active_index(self) -> Annotated[int, "step=1"]:

        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "step=1"]) -> None:
        ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['NodesModifierDataBlock']: ...
    def __getitem__(self, key: Union[str, int]) -> 'NodesModifierDataBlock': ...
    def __len__(self) -> int: ...