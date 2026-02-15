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
from .VertexGroupElement import VertexGroupElement
class LatticePoint(bpy_struct):
    select: bool
    """Selection status"""
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Original undeformed location used to calculate the strength of the deform effect (edit/animate the Deformed Location instead)"""
        ...
    co_deform: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    weight_softbody: Annotated[float, "step=10.0", "precision=3"]
    """Softbody goal weight"""
    @property
    def groups(self) -> Annotated[bpy_prop_collection['VertexGroupElement'], "is_animatable=False"]:
        """Weights for the vertex groups this point is member of"""
        ...