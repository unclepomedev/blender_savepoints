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

    use_guide: Annotated[bool, "is_animatable=False"]
    """Enable speed guides"""
    use_snapping: Annotated[bool, "is_animatable=False"]
    """Enable snapping to guides angle or spacing options"""
    reference_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object used for reference point"""
    reference_point: Annotated[Literal['CURSOR', 'CUSTOM', 'OBJECT'], "is_animatable=False"]
    """Type of speed guide"""
    type: Annotated[Literal['CIRCULAR', 'RADIAL', 'PARALLEL', 'GRID', 'ISO'], "is_animatable=False"]
    """Type of speed guide"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Direction of lines"""
    angle_snap: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Angle snapping"""
    spacing: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Guide spacing"""
    location: Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Custom reference point for guides"""