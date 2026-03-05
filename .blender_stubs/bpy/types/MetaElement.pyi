# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MetaElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MetaElement(bpy_struct):

    @property
    def type(self) -> Literal['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE']:
        """Metaball type"""
        ...
    @type.setter
    def type(self, value: Literal['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE']) -> None:
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:
        """Normalized quaternion rotation"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def radius(self) -> Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @radius.setter
    def radius(self, value: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Size of element, use of components depends on element type"""
        ...
    @size_x.setter
    def size_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Size of element, use of components depends on element type"""
        ...
    @size_y.setter
    def size_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def size_z(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Size of element, use of components depends on element type"""
        ...
    @size_z.setter
    def size_z(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def stiffness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Stiffness defines how much of the element to fill"""
        ...
    @stiffness.setter
    def stiffness(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_negative(self) -> bool:
        """Set metaball as negative one"""
        ...
    @use_negative.setter
    def use_negative(self, value: bool) -> None:
        ...
    @property
    def use_scale_stiffness(self) -> bool:
        """Scale stiffness instead of radius"""
        ...
    @use_scale_stiffness.setter
    def use_scale_stiffness(self, value: bool) -> None:
        ...
    @property
    def select(self) -> bool:
        """Select element"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def hide(self) -> bool:
        """Hide element"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...