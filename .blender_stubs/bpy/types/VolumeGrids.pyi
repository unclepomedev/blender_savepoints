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
from .VolumeGrid import VolumeGrid
class VolumeGrids(bpy_struct):
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index of active volume grid"""
    @property
    def error_message(self) -> Annotated[str, "is_animatable=False"]:
        """If loading grids failed, error message with details"""
        ...
    @property
    def is_loaded(self) -> bool:
        """List of grids and metadata are loaded in memory"""
        ...
    @property
    def frame(self) -> Annotated[int, "step=1"]:
        """Frame number that volume grids will be loaded at, based on scene time and volume parameters"""
        ...
    @property
    def frame_filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Volume file used for loading the volume at the current frame. Empty if the volume has not be loaded or the frame only exists in memory."""
        ...
    def load(self, *args, **kwargs) -> Any: ...
    def unload(self, *args, **kwargs) -> Any: ...
    def save(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['VolumeGrid']: ...
    def __getitem__(self, key: Union[str, int]) -> 'VolumeGrid': ...
    def __len__(self) -> int: ...