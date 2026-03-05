# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeRegionsSidebars.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeRegionsSidebars(bpy_struct):

    @property
    def back(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @back.setter
    def back(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def tab_back(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @tab_back.setter
    def tab_back(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...