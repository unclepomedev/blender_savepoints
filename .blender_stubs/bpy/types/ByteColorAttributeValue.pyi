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

    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """RGBA color in scene linear color space"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def color_srgb(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """RGBA color in sRGB color space"""
        ...
    @color_srgb.setter
    def color_srgb(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...