# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BezierSplinePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class BezierSplinePoint(bpy_struct):

    @property
    def select_left_handle(self) -> bool:
        """Handle 1 selection status"""
        ...
    @select_left_handle.setter
    def select_left_handle(self, value: bool):
        ...
    @property
    def select_right_handle(self) -> bool:
        """Handle 2 selection status"""
        ...
    @select_right_handle.setter
    def select_right_handle(self, value: bool):
        ...
    @property
    def select_control_point(self) -> bool:
        """Control point selection status"""
        ...
    @select_control_point.setter
    def select_control_point(self, value: bool):
        ...
    @property
    def hide(self) -> bool:
        """Visibility status"""
        ...
    @hide.setter
    def hide(self, value: bool):
        ...
    @property
    def handle_left_type(self) -> Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']:
        """Handle types"""
        ...
    @handle_left_type.setter
    def handle_left_type(self, value: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']):
        ...
    @property
    def handle_right_type(self) -> Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']:
        """Handle types"""
        ...
    @handle_right_type.setter
    def handle_right_type(self, value: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']):
        ...
    @property
    def handle_left(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Coordinates of the first handle"""
        ...
    @handle_left.setter
    def handle_left(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Coordinates of the control point"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
        ...
    @property
    def handle_right(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Coordinates of the second handle"""
        ...
    @handle_right.setter
    def handle_right(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]):
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