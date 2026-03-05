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

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the dash segment"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def dash(self) -> Annotated[int, "step=1"]:
        """The number of consecutive points from the original stroke to include in this segment"""
        ...
    @dash.setter
    def dash(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def gap(self) -> Annotated[int, "step=1"]:
        """The number of points skipped after this segment"""
        ...
    @gap.setter
    def gap(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def radius(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]:
        """The factor to apply to the original point's radius for the new points"""
        ...
    @radius.setter
    def radius(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]:
        """The factor to apply to the original point's opacity for the new points"""
        ...
    @opacity.setter
    def opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def material_index(self) -> Annotated[int, "step=1"]:
        """Use this index on generated segment. -1 means using the existing material."""
        ...
    @material_index.setter
    def material_index(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_cyclic(self) -> bool:
        """Enable cyclic on individual stroke dashes"""
        ...
    @use_cyclic.setter
    def use_cyclic(self, value: bool):
        ...