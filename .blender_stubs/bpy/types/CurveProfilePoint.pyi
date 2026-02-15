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
class CurveProfilePoint(bpy_struct):
    location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """X/Y coordinates of the path point"""
    handle_type_1: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
    """Path interpolation at this point"""
    handle_type_2: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
    """Path interpolation at this point"""
    select: bool
    """Selection state of the path point"""