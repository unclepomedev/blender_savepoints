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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeGraphEditor(bpy_struct):
    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex_size: Annotated[int, "subtype='PIXEL'", "step=1"]