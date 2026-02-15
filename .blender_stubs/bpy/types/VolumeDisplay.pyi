# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VolumeDisplay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class VolumeDisplay(bpy_struct):

    density: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Thickness of volume display in the viewport"""
    wireframe_type: Literal['NONE', 'BOUNDS', 'BOXES', 'POINTS']
    """Type of wireframe display"""
    wireframe_detail: Literal['COARSE', 'FINE']
    """Amount of detail for wireframe display"""
    interpolation_method: Literal['LINEAR', 'CUBIC', 'CLOSEST']
    """Interpolation method to use for volumes in solid mode"""
    use_slice: bool
    """Perform a single slice of the domain object"""
    slice_axis: Literal['AUTO', 'X', 'Y', 'Z']

    slice_depth: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Position of the slice"""