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
from .VolumeGrid import VolumeGrid
class VolumeGrids(bpy_struct):
    active_index: int
    error_message: str
    is_loaded: bool
    frame: int
    frame_filepath: str
    def load(self, *args, **kwargs) -> Any: ...
    def unload(self, *args, **kwargs) -> Any: ...
    def save(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['VolumeGrid']: ...
    def __getitem__(self, key: Union[str, int]) -> 'VolumeGrid': ...
    def __len__(self) -> int: ...