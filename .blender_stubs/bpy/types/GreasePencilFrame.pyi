# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .GreasePencilDrawing import GreasePencilDrawing
class GreasePencilFrame(bpy_struct):
    drawing: 'GreasePencilDrawing'
    frame_number: int
    select: bool
    keyframe_type: str