# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskSplinePointUW.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MaskSplinePointUW(bpy_struct):

    u: Annotated[float, "step=10.0", "precision=3"]
    """U coordinate of point along spline segment"""
    weight: Annotated[float, "step=10.0", "precision=3"]
    """Weight of feather point"""
    select: bool
    """Selection status"""