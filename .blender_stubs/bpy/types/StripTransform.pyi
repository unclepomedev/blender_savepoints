# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripTransform.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StripTransform(bpy_struct):

    scale_x: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]
    """Scale along X axis"""
    scale_y: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]
    """Scale along Y axis"""
    offset_x: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]
    """Move along X axis"""
    offset_y: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=3"]
    """Move along Y axis"""
    rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotate around image center"""
    origin: Annotated[list[float], "step=1.0", "precision=3"]
    """Origin of image for transformation"""
    filter: Literal['AUTO', 'NEAREST', 'BILINEAR', 'CUBIC_MITCHELL', 'CUBIC_BSPLINE', 'BOX']
    """Type of filter to use for image transformation"""