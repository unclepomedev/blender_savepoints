# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TexMapping.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TexMapping(bpy_struct):

    @property
    def vector_type(self) -> Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']:
        """Type of vector that the mapping transforms"""
        ...
    @vector_type.setter
    def vector_type(self, value: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']):
        ...
    @property
    def translation(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:

        ...
    @translation.setter
    def translation(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]:

        ...
    @rotation.setter
    def rotation(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]):
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def min(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Minimum value for clipping"""
        ...
    @min.setter
    def min(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def max(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Maximum value for clipping"""
        ...
    @max.setter
    def max(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_min(self) -> bool:
        """Whether to use minimum clipping value"""
        ...
    @use_min.setter
    def use_min(self, value: bool):
        ...
    @property
    def use_max(self) -> bool:
        """Whether to use maximum clipping value"""
        ...
    @use_max.setter
    def use_max(self, value: bool):
        ...
    @property
    def mapping_x(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_x.setter
    def mapping_x(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping_y(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_y.setter
    def mapping_y(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping_z(self) -> Literal['NONE', 'X', 'Y', 'Z']:

        ...
    @mapping_z.setter
    def mapping_z(self, value: Literal['NONE', 'X', 'Y', 'Z']):
        ...
    @property
    def mapping(self) -> Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']:

        ...
    @mapping.setter
    def mapping(self, value: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']):
        ...