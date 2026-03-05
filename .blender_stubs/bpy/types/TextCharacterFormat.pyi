# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TextCharacterFormat.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TextCharacterFormat(bpy_struct):

    @property
    def use_bold(self) -> bool:

        ...
    @use_bold.setter
    def use_bold(self, value: bool):
        ...
    @property
    def use_italic(self) -> bool:

        ...
    @use_italic.setter
    def use_italic(self, value: bool):
        ...
    @property
    def use_underline(self) -> bool:

        ...
    @use_underline.setter
    def use_underline(self, value: bool):
        ...
    @property
    def use_small_caps(self) -> bool:

        ...
    @use_small_caps.setter
    def use_small_caps(self, value: bool):
        ...
    @property
    def material_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Material slot index of this character"""
        ...
    @material_index.setter
    def material_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def kerning(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Spacing between characters"""
        ...
    @kerning.setter
    def kerning(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...