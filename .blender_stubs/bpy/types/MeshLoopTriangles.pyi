# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshLoopTriangles.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MeshLoopTriangle import MeshLoopTriangle

class MeshLoopTriangles(bpy_struct):

    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['MeshLoopTriangle']: ...
    def __getitem__(self, key: Union[str, int]) -> 'MeshLoopTriangle': ...
    def __len__(self) -> int: ...