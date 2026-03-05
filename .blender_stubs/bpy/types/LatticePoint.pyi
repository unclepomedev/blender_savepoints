# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LatticePoint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .VertexGroupElement import VertexGroupElement
from .bpy_prop_collection import bpy_prop_collection

class LatticePoint(bpy_struct):

    @property
    def select(self) -> bool:
        """Selection status"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Original undeformed location used to calculate the strength of the deform effect (edit/animate the Deformed Location instead)"""
        ...
    @property
    def co_deform(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:

        ...
    @co_deform.setter
    def co_deform(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def weight_softbody(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Softbody goal weight"""
        ...
    @weight_softbody.setter
    def weight_softbody(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def groups(self) -> Annotated[bpy_prop_collection['VertexGroupElement'], "is_animatable=False"]:
        """Weights for the vertex groups this point is member of"""
        ...