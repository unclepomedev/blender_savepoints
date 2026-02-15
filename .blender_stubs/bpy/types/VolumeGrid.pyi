# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VolumeGrid.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class VolumeGrid(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Volume grid name"""
        ...
    @property
    def data_type(self) -> Literal['BOOLEAN', 'FLOAT', 'DOUBLE', 'INT', 'INT64', 'MASK', 'VECTOR_FLOAT', 'VECTOR_DOUBLE', 'VECTOR_INT', 'POINTS', 'UNKNOWN']:
        """Data type of voxel values"""
        ...
    @property
    def channels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of dimensions of the grid data type"""
        ...
    @property
    def matrix_object(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Transformation matrix from voxel index to object space"""
        ...
    @property
    def is_loaded(self) -> bool:
        """Grid tree is loaded in memory"""
        ...
    def load(self, *args, **kwargs) -> Any: ...
    def unload(self, *args, **kwargs) -> Any: ...