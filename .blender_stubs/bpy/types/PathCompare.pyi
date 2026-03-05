# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PathCompare.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class PathCompare(bpy_struct):

    @property
    def path(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:

        ...
    @path.setter
    def path(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def use_glob(self) -> bool:
        """Enable wildcard globbing"""
        ...
    @use_glob.setter
    def use_glob(self, value: bool) -> None:
        ...