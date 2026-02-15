# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilDashModifierSegment.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class GreasePencilDashModifierSegment(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Name of the dash segment"""
    dash: Annotated[int, "step=1"]
    """The number of consecutive points from the original stroke to include in this segment"""
    gap: Annotated[int, "step=1"]
    """The number of points skipped after this segment"""
    radius: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """The factor to apply to the original point's radius for the new points"""
    opacity: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """The factor to apply to the original point's opacity for the new points"""
    material_index: Annotated[int, "step=1"]
    """Use this index on generated segment. -1 means using the existing material."""
    use_cyclic: bool
    """Enable cyclic on individual stroke dashes"""