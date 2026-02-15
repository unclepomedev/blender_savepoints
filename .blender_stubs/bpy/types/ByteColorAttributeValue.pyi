# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ByteColorAttributeValue.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ByteColorAttributeValue(bpy_struct):

    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """RGBA color in scene linear color space"""
    color_srgb: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """RGBA color in sRGB color space"""