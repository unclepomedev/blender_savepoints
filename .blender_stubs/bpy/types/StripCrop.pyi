# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripCrop.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class StripCrop(bpy_struct):

    max_y: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to crop from the top"""
    min_y: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to crop from the bottom"""
    min_x: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to crop from the left side"""
    max_x: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Number of pixels to crop from the right side"""