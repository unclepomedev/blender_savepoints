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
class StripElement(bpy_struct):
    filename: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]
    """Name of the source file"""
    @property
    def orig_width(self) -> Annotated[int, "step=1"]:
        """Original image width"""
        ...
    @property
    def orig_height(self) -> Annotated[int, "step=1"]:
        """Original image height"""
        ...
    @property
    def orig_fps(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Original frames per second"""
        ...