# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SplinePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SplinePoint(bpy_struct):

    @property
    def select(self) -> bool:
        """Selection status"""
        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def hide(self) -> bool:
        """Visibility status"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Point coordinates"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
        ...
    @property
    def weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """NURBS weight"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def tilt(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Tilt in 3D View"""
        ...
    @tilt.setter
    def tilt(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def weight_softbody(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Softbody goal weight"""
        ...
    @weight_softbody.setter
    def weight_softbody(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def radius(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Radius for beveling"""
        ...
    @radius.setter
    def radius(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...