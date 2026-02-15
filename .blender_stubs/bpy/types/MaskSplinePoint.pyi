# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .MaskParent import MaskParent
from .MaskSplinePointUW import MaskSplinePointUW
class MaskSplinePoint(bpy_struct):
    handle_left: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Coordinates of the first handle"""
    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Coordinates of the control point"""
    handle_right: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Coordinates of the second handle"""
    handle_type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']
    """Handle type"""
    handle_left_type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']
    """Handle type"""
    handle_right_type: Literal['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE']
    """Handle type"""
    weight: Annotated[float, "step=10.0", "precision=3"]
    """Weight of the point"""
    select: bool
    """Selection status of the control point. (Deprecated: use Select Control Point instead)"""
    select_left_handle: bool
    """Selection status of the left handle"""
    select_control_point: bool
    """Selection status of the control point"""
    select_right_handle: bool
    """Selection status of the right handle"""
    select_single_handle: bool
    """Selection status of the Aligned Single handle"""
    @property
    def parent(self) -> Annotated[Optional['MaskParent'], "is_animatable=False"]:
        ...
    @property
    def feather_points(self) -> Annotated[bpy_prop_collection['MaskSplinePointUW'], "is_animatable=False"]:
        """Points defining feather"""
        ...