# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshStatVis.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MeshStatVis(bpy_struct):

    @property
    def type(self) -> Annotated[Literal['OVERHANG', 'THICKNESS', 'INTERSECT', 'DISTORT', 'SHARP'], "is_animatable=False"]:
        """Type of data to visualize/check"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['OVERHANG', 'THICKNESS', 'INTERSECT', 'DISTORT', 'SHARP'], "is_animatable=False"]) -> None:
        ...
    @property
    def overhang_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Minimum angle to display"""
        ...
    @overhang_min.setter
    def overhang_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def overhang_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum angle to display"""
        ...
    @overhang_max.setter
    def overhang_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def overhang_axis(self) -> Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]:

        ...
    @overhang_axis.setter
    def overhang_axis(self, value: Annotated[Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], "is_animatable=False"]) -> None:
        ...
    @property
    def thickness_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """Minimum for measuring thickness"""
        ...
    @thickness_min.setter
    def thickness_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def thickness_max(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """Maximum for measuring thickness"""
        ...
    @thickness_max.setter
    def thickness_max(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def thickness_samples(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Number of samples to test per face"""
        ...
    @thickness_samples.setter
    def thickness_samples(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def distort_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Minimum angle to display"""
        ...
    @distort_min.setter
    def distort_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def distort_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum angle to display"""
        ...
    @distort_max.setter
    def distort_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def sharp_min(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Minimum angle to display"""
        ...
    @sharp_min.setter
    def sharp_min(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def sharp_max(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum angle to display"""
        ...
    @sharp_max.setter
    def sharp_max(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...