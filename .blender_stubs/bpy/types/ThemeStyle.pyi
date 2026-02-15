# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeStyle.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeFontStyle import ThemeFontStyle

class ThemeStyle(bpy_struct):

    @property
    def panel_title(self) -> Annotated['ThemeFontStyle', "is_animatable=False"]:

        ...
    @property
    def widget(self) -> Annotated['ThemeFontStyle', "is_animatable=False"]:

        ...
    @property
    def tooltip(self) -> Annotated['ThemeFontStyle', "is_animatable=False"]:

        ...