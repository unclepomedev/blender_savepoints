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
class MeshSkinVertex(bpy_struct):
    radius: Annotated[list[float], "subtype='UNSIGNED'", "step=1.0", "precision=3"]
    """Radius of the skin"""
    use_root: bool
    """Vertex is a root for rotation calculations and armature generation, setting this flag does not clear other roots in the same mesh island"""
    use_loose: bool
    """If vertex has multiple adjacent edges, it is hulled to them directly"""