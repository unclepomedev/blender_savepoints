# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskSplinePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MaskParent import MaskParent
from .MaskSplinePointUW import MaskSplinePointUW
from .bpy_prop_collection import bpy_prop_collection

class MaskSplinePoint(bpy_struct):

    @property
    def handle_left(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Coordinates of the first handle"""
        ...
    @handle_left.setter
    def handle_left(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Coordinates of the control point"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def handle_right(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Coordinates of the second handle"""
        ...
    @handle_right.setter
    def handle_right(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def handle_type(self) -> Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']:
        """Handle type"""
        ...
    @handle_type.setter
    def handle_type(self, value: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']) -> None:
        ...
    @property
    def handle_left_type(self) -> Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']:
        """Handle type"""
        ...
    @handle_left_type.setter
    def handle_left_type(self, value: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']) -> None:
        ...
    @property
    def handle_right_type(self) -> Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']:
        """Handle type"""
        ...
    @handle_right_type.setter
    def handle_right_type(self, value: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']) -> None:
        ...
    @property
    def weight(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Weight of the point"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def select(self) -> bool:
        """Selection status of the control point. (Deprecated: use Select Control Point instead)"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def select_left_handle(self) -> bool:
        """Selection status of the left handle"""
        ...
    @select_left_handle.setter
    def select_left_handle(self, value: bool) -> None:
        ...
    @property
    def select_control_point(self) -> bool:
        """Selection status of the control point"""
        ...
    @select_control_point.setter
    def select_control_point(self, value: bool) -> None:
        ...
    @property
    def select_right_handle(self) -> bool:
        """Selection status of the right handle"""
        ...
    @select_right_handle.setter
    def select_right_handle(self, value: bool) -> None:
        ...
    @property
    def select_single_handle(self) -> bool:
        """Selection status of the Aligned Single handle"""
        ...
    @select_single_handle.setter
    def select_single_handle(self, value: bool) -> None:
        ...
    @property
    def parent(self) -> Annotated[Optional['MaskParent'], "is_animatable=False"]:

        ...
    @property
    def feather_points(self) -> Annotated[bpy_prop_collection['MaskSplinePointUW'], "is_animatable=False"]:
        """Points defining feather"""
        ...