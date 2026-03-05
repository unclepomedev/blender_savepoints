# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Scopes.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Histogram import Histogram

class Scopes(bpy_struct):

    @property
    def use_full_resolution(self) -> bool:
        """Sample every pixel of the image"""
        ...
    @use_full_resolution.setter
    def use_full_resolution(self, value: bool) -> None:
        ...
    @property
    def accuracy(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1"]:
        """Proportion of original image source pixel lines to sample"""
        ...
    @accuracy.setter
    def accuracy(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1"]) -> None:
        ...
    @property
    def histogram(self) -> Annotated[Optional['Histogram'], "is_animatable=False"]:
        """Histogram for viewing image statistics"""
        ...
    @property
    def waveform_mode(self) -> Literal['LUMA', 'PARADE', 'YCBCR601', 'YCBCR709', 'YCBCRJPG', 'RGB']:

        ...
    @waveform_mode.setter
    def waveform_mode(self, value: Literal['LUMA', 'PARADE', 'YCBCR601', 'YCBCR709', 'YCBCRJPG', 'RGB']) -> None:
        ...
    @property
    def waveform_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the points"""
        ...
    @waveform_alpha.setter
    def waveform_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def vectorscope_mode(self) -> Literal['LUMA', 'RGB']:

        ...
    @vectorscope_mode.setter
    def vectorscope_mode(self, value: Literal['LUMA', 'RGB']) -> None:
        ...
    @property
    def vectorscope_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the points"""
        ...
    @vectorscope_alpha.setter
    def vectorscope_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...