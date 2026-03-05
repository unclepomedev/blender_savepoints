# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectLineArt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ObjectLineArt(bpy_struct):

    @property
    def usage(self) -> Annotated[Literal['INHERIT', 'INCLUDE', 'OCCLUSION_ONLY', 'EXCLUDE', 'INTERSECTION_ONLY', 'NO_INTERSECTION', 'FORCE_INTERSECTION'], "is_animatable=False"]:
        """How to use this object in Line Art calculation"""
        ...
    @usage.setter
    def usage(self, value: Annotated[Literal['INHERIT', 'INCLUDE', 'OCCLUSION_ONLY', 'EXCLUDE', 'INTERSECTION_ONLY', 'NO_INTERSECTION', 'FORCE_INTERSECTION'], "is_animatable=False"]):
        ...
    @property
    def use_crease_override(self) -> Annotated[bool, "is_animatable=False"]:
        """Use this object's crease setting to overwrite scene global"""
        ...
    @use_crease_override.setter
    def use_crease_override(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def crease_threshold(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1", "is_animatable=False"]:
        """Angles smaller than this will be treated as creases"""
        ...
    @crease_threshold.setter
    def crease_threshold(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1", "is_animatable=False"]):
        ...
    @property
    def use_intersection_priority_override(self) -> Annotated[bool, "is_animatable=False"]:
        """Use this object's intersection priority to override collection setting"""
        ...
    @use_intersection_priority_override.setter
    def use_intersection_priority_override(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def intersection_priority(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The intersection line will be included into the object with the higher intersection priority value"""
        ...
    @intersection_priority.setter
    def intersection_priority(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...