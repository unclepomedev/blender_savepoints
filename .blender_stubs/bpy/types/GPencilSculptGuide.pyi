# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GPencilSculptGuide.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class GPencilSculptGuide(bpy_struct):

    @property
    def use_guide(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable speed guides"""
        ...
    @use_guide.setter
    def use_guide(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snapping(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable snapping to guides angle or spacing options"""
        ...
    @use_snapping.setter
    def use_snapping(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def reference_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object used for reference point"""
        ...
    @reference_object.setter
    def reference_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def reference_point(self) -> Annotated[Literal['CURSOR', 'CUSTOM', 'OBJECT'], "is_animatable=False"]:
        """Type of speed guide"""
        ...
    @reference_point.setter
    def reference_point(self, value: Annotated[Literal['CURSOR', 'CUSTOM', 'OBJECT'], "is_animatable=False"]):
        ...
    @property
    def type(self) -> Annotated[Literal['CIRCULAR', 'RADIAL', 'PARALLEL', 'GRID', 'ISO'], "is_animatable=False"]:
        """Type of speed guide"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['CIRCULAR', 'RADIAL', 'PARALLEL', 'GRID', 'ISO'], "is_animatable=False"]):
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Direction of lines"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def angle_snap(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Angle snapping"""
        ...
    @angle_snap.setter
    def angle_snap(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def spacing(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Guide spacing"""
        ...
    @spacing.setter
    def spacing(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def location(self) -> Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Custom reference point for guides"""
        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...