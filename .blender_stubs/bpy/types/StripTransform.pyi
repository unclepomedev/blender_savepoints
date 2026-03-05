# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripTransform.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StripTransform(bpy_struct):

    @property
    def scale_x(self) -> Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]:
        """Scale along X axis"""
        ...
    @scale_x.setter
    def scale_x(self, value: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]):
        ...
    @property
    def scale_y(self) -> Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]:
        """Scale along Y axis"""
        ...
    @scale_y.setter
    def scale_y(self, value: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]):
        ...
    @property
    def offset_x(self) -> Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]:
        """Move along X axis"""
        ...
    @offset_x.setter
    def offset_x(self, value: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]):
        ...
    @property
    def offset_y(self) -> Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]:
        """Move along Y axis"""
        ...
    @offset_y.setter
    def offset_y(self, value: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]):
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotate around image center"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def origin(self) -> Annotated[list[float], "step=1.0", "precision=3"]:
        """Origin of image for transformation"""
        ...
    @origin.setter
    def origin(self, value: Annotated[list[float], "step=1.0", "precision=3"]):
        ...
    @property
    def filter(self) -> Literal['AUTO', 'NEAREST', 'BILINEAR', 'CUBIC_MITCHELL', 'CUBIC_BSPLINE', 'BOX']:
        """Type of filter to use for image transformation"""
        ...
    @filter.setter
    def filter(self, value: Literal['AUTO', 'NEAREST', 'BILINEAR', 'CUBIC_MITCHELL', 'CUBIC_BSPLINE', 'BOX']):
        ...