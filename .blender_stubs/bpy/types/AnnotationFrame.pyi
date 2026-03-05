# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnnotationFrame.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnnotationStroke import AnnotationStroke
from .bpy_prop_collection import bpy_prop_collection

class AnnotationFrame(bpy_struct):

    @property
    def strokes(self) -> Annotated[bpy_prop_collection['AnnotationStroke'], "is_animatable=False"]:
        """Freehand curves defining the sketch on this frame"""
        ...
    @property
    def frame_number(self) -> Annotated[int, "step=1"]:
        """The frame on which this sketch appears"""
        ...
    @frame_number.setter
    def frame_number(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def select(self) -> bool:
        """Frame is selected for editing in the Dope Sheet"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...