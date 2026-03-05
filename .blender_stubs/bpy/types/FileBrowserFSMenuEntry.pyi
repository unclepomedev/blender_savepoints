# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FileBrowserFSMenuEntry.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FileBrowserFSMenuEntry(bpy_struct):

    @property
    def path(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:

        ...
    @path.setter
    def path(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]) -> None:
        ...
    @property
    def icon(self) -> Annotated[int, "step=1"]:

        ...
    @icon.setter
    def icon(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_save(self) -> bool:
        """Whether this path is saved in bookmarks, or generated from OS"""
        ...