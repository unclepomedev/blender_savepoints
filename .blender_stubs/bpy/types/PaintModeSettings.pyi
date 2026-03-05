# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PaintModeSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Image import Image

class PaintModeSettings(bpy_struct):

    @property
    def canvas_source(self) -> Annotated[Literal['COLOR_ATTRIBUTE', 'MATERIAL', 'IMAGE'], "is_animatable=False"]:
        """Source to select canvas from"""
        ...
    @canvas_source.setter
    def canvas_source(self, value: Annotated[Literal['COLOR_ATTRIBUTE', 'MATERIAL', 'IMAGE'], "is_animatable=False"]):
        ...
    @property
    def canvas_image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image used as painting target"""
        ...
    @canvas_image.setter
    def canvas_image(self, value: Annotated[Optional['Image'], "is_animatable=False"]):
        ...