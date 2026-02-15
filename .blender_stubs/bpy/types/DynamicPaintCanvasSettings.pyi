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
from .DynamicPaintSurface import DynamicPaintSurface
from .DynamicPaintSurfaces import DynamicPaintSurfaces
class DynamicPaintCanvasSettings(bpy_struct):
    @property
    def canvas_surfaces(self) -> Annotated['DynamicPaintSurfaces', "is_animatable=False"]:
        """Paint surface list"""
        ...