# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnnotationLayers.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnnotationLayer import AnnotationLayer

class AnnotationLayers(bpy_struct):

    @property
    def active_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of active annotation layer"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def active_note(self) -> Literal['DEFAULT']:
        """Note/Layer to add annotation strokes to"""
        ...
    @active_note.setter
    def active_note(self, value: Literal['DEFAULT']) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['AnnotationLayer']: ...
    def __getitem__(self, key: Union[str, int]) -> 'AnnotationLayer': ...
    def __len__(self) -> int: ...