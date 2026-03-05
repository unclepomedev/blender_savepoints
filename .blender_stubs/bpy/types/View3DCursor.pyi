# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.View3DCursor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class View3DCursor(bpy_struct):

    @property
    def location(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=10.0", "precision=4", "is_animatable=False"]:

        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=10.0", "precision=4", "is_animatable=False"]):
        ...
    @property
    def rotation_quaternion(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Rotation in quaternions (keep normalized)"""
        ...
    @rotation_quaternion.setter
    def rotation_quaternion(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def rotation_axis_angle(self) -> Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Angle of Rotation for Axis-Angle rotation representation"""
        ...
    @rotation_axis_angle.setter
    def rotation_axis_angle(self, value: Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def rotation_euler(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5", "is_animatable=False"]:
        """3D rotation"""
        ...
    @rotation_euler.setter
    def rotation_euler(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5", "is_animatable=False"]):
        ...
    @property
    def rotation_mode(self) -> Annotated[Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], "is_animatable=False"]:
        """The kind of rotation to apply, values from other rotation modes are not used"""
        ...
    @rotation_mode.setter
    def rotation_mode(self, value: Annotated[Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], "is_animatable=False"]):
        ...
    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Matrix combining location and rotation of the cursor"""
        ...
    @matrix.setter
    def matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...