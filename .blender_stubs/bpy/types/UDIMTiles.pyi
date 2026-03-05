# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UDIMTiles.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .UDIMTile import UDIMTile

class UDIMTiles(bpy_struct):

    @property
    def active_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Active index in tiles array"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def active(self) -> Annotated['UDIMTile', "is_animatable=False"]:
        """Active Image Tile"""
        ...
    @active.setter
    def active(self, value: Annotated['UDIMTile', "is_animatable=False"]) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['UDIMTile']: ...
    def __getitem__(self, key: Union[str, int]) -> 'UDIMTile': ...
    def __len__(self) -> int: ...