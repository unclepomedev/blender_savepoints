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
class MeshEdge(bpy_struct):
    vertices: Annotated[list[int], "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Vertex indices"""
    select: Annotated[bool, "is_animatable=False"]
    hide: Annotated[bool, "is_animatable=False"]
    use_seam: bool
    """Seam edge for UV unwrapping"""
    use_edge_sharp: bool
    """Sharp edge for shading"""
    @property
    def is_loose(self) -> bool:
        """Edge is not connected to any faces"""
        ...
    @property
    def index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index of this edge"""
        ...