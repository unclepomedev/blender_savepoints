# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeGradientColors.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeGradientColors(bpy_struct):

    @property
    def background_type(self) -> Literal['SINGLE_COLOR', 'LINEAR', 'RADIAL']:
        """Type of background in the 3D viewport"""
        ...
    @background_type.setter
    def background_type(self, value: Literal['SINGLE_COLOR', 'LINEAR', 'RADIAL']):
        ...
    @property
    def high_gradient(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @high_gradient.setter
    def high_gradient(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def gradient(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gradient.setter
    def gradient(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...