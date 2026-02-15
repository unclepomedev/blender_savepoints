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
class FloatColorAttributeValue(bpy_struct):
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """RGBA color in scene linear color space"""
    color_srgb: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """RGBA color in sRGB color space"""