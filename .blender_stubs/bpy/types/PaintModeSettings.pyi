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
from .Image import Image
class PaintModeSettings(bpy_struct):
    canvas_source: Annotated[Literal['COLOR_ATTRIBUTE', 'MATERIAL', 'IMAGE'], "is_animatable=False"]
    """Source to select canvas from"""
    canvas_image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image used as painting target"""