# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BrushCapabilities.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class BrushCapabilities(bpy_struct):

    @property
    def has_overlay(self) -> bool:

        ...
    @property
    def has_random_texture_angle(self) -> bool:

        ...
    @property
    def has_spacing(self) -> bool:

        ...
    @property
    def has_smooth_stroke(self) -> bool:

        ...