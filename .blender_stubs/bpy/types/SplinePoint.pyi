# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SplinePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SplinePoint(bpy_struct):

    select: bool
    """Selection status"""
    hide: bool
    """Visibility status"""
    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Point coordinates"""
    weight: Annotated[float, "step=10.0", "precision=3"]
    """NURBS weight"""
    tilt: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Tilt in 3D View"""
    weight_softbody: Annotated[float, "step=10.0", "precision=3"]
    """Softbody goal weight"""
    radius: Annotated[float, "step=10.0", "precision=3"]
    """Radius for beveling"""