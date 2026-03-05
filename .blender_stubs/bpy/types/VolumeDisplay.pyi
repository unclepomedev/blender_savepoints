# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VolumeDisplay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class VolumeDisplay(bpy_struct):

    @property
    def density(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Thickness of volume display in the viewport"""
        ...
    @density.setter
    def density(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def wireframe_type(self) -> Literal['NONE', 'BOUNDS', 'BOXES', 'POINTS']:
        """Type of wireframe display"""
        ...
    @wireframe_type.setter
    def wireframe_type(self, value: Literal['NONE', 'BOUNDS', 'BOXES', 'POINTS']) -> None:
        ...
    @property
    def wireframe_detail(self) -> Literal['COARSE', 'FINE']:
        """Amount of detail for wireframe display"""
        ...
    @wireframe_detail.setter
    def wireframe_detail(self, value: Literal['COARSE', 'FINE']) -> None:
        ...
    @property
    def interpolation_method(self) -> Literal['LINEAR', 'CUBIC', 'CLOSEST']:
        """Interpolation method to use for volumes in solid mode"""
        ...
    @interpolation_method.setter
    def interpolation_method(self, value: Literal['LINEAR', 'CUBIC', 'CLOSEST']) -> None:
        ...
    @property
    def use_slice(self) -> bool:
        """Perform a single slice of the domain object"""
        ...
    @use_slice.setter
    def use_slice(self, value: bool) -> None:
        ...
    @property
    def slice_axis(self) -> Literal['AUTO', 'X', 'Y', 'Z']:

        ...
    @slice_axis.setter
    def slice_axis(self, value: Literal['AUTO', 'X', 'Y', 'Z']) -> None:
        ...
    @property
    def slice_depth(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Position of the slice"""
        ...
    @slice_depth.setter
    def slice_depth(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...