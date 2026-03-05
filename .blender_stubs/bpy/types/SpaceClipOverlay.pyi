# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceClipOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SpaceClipOverlay(bpy_struct):

    @property
    def show_overlays(self) -> bool:
        """Display overlays like cursor and annotations"""
        ...
    @show_overlays.setter
    def show_overlays(self, value: bool):
        ...
    @property
    def show_cursor(self) -> bool:
        """Display 2D cursor"""
        ...
    @show_cursor.setter
    def show_cursor(self, value: bool):
        ...