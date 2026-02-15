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
from .AnnotationStroke import AnnotationStroke
class AnnotationFrame(bpy_struct):
    @property
    def strokes(self) -> Annotated[bpy_prop_collection['AnnotationStroke'], "is_animatable=False"]:
        """Freehand curves defining the sketch on this frame"""
        ...
    frame_number: Annotated[int, "step=1"]
    """The frame on which this sketch appears"""
    select: bool
    """Frame is selected for editing in the Dope Sheet"""